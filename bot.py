import os
import logging
import asyncio
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.types import DocumentAttributeFilename
from telethon.errors import FloodWaitError

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

    def log_message(self, format, *args):
        pass  # suppress access logs


def start_health_server():
    port = int(os.getenv('PORT', 8080))
    HTTPServer(('0.0.0.0', port), HealthHandler).serve_forever()


def parse_channel(value: str):
    """Return int ID if numeric, otherwise return as-is (username)."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return value


API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')
SESSION_STRING = os.getenv('SESSION_STRING')
SOURCE_CHANNEL = parse_channel(os.getenv('SOURCE_CHANNEL'))
TARGET_CHANNEL = parse_channel(os.getenv('TARGET_CHANNEL'))

try:
    session = StringSession(SESSION_STRING) if SESSION_STRING else 'session'
except ValueError:
    logger.error("SESSION_STRING is invalid. Run generate_session.py locally to get a valid one.")
    raise
client = TelegramClient(session, API_ID, API_HASH)
transfer_semaphore = asyncio.Semaphore(1)


@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handle_new_message(event):
    message = event.message

    if not message.media:
        return

    if hasattr(message.media, 'document'):
        mime_type = message.media.document.mime_type
        if mime_type != 'video/x-matroska':
            logger.info(f"Skipping non-MKV file: {message.id}")
            return

    async with transfer_semaphore:
        for attempt in range(3):
            try:
                req = ForwardMessagesRequest(
                    from_peer=message.peer_id,
                    id=[message.id],
                    to_peer=TARGET_CHANNEL,
                    drop_author=True
                )
                result = await client(req)
                logger.info(f"Forwarded message {message.id} to {TARGET_CHANNEL}")
                break
            except FloodWaitError as e:
                logger.warning(f"Flood wait {e.seconds}s, retrying...")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                logger.error(f"Error forwarding (attempt {attempt + 1}): {e}")
                if attempt < 2:
                    await asyncio.sleep(2 ** attempt)
                else:
                    logger.error(f"Giving up on message {message.id}")


async def main():
    missing = [k for k, v in {
        'API_ID': os.getenv('API_ID'),
        'API_HASH': os.getenv('API_HASH'),
        'PHONE_NUMBER': os.getenv('PHONE_NUMBER'),
        'SOURCE_CHANNEL': os.getenv('SOURCE_CHANNEL'),
        'TARGET_CHANNEL': os.getenv('TARGET_CHANNEL'),
    }.items() if not v]

    if missing:
        logger.error(f"Missing required env vars: {', '.join(missing)}")
        return

    threading.Thread(target=start_health_server, daemon=True).start()
    logger.info("Health check server started on port 8080")

    await client.start(phone=PHONE_NUMBER)
    me = await client.get_me()
    logger.info(f"Logged in as {me.first_name} (@{me.username})")
    logger.info(f"Monitoring: {SOURCE_CHANNEL} → {TARGET_CHANNEL}")
    logger.info("Waiting for new files...")
    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
