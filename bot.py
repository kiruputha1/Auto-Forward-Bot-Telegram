import os
import io
import logging
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import DocumentAttributeFilename

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


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

# Use StringSession for cloud/Docker deployments, fall back to file session locally
session = StringSession(SESSION_STRING) if SESSION_STRING else 'session'
client = TelegramClient(session, API_ID, API_HASH)


@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handle_new_message(event):
    message = event.message

    if not message.media:
        return

    try:
        # Extract original filename from document attributes
        filename = None
        if hasattr(message.media, 'document'):
            for attr in message.media.document.attributes:
                if isinstance(attr, DocumentAttributeFilename):
                    filename = attr.file_name
                    break

        file_bytes = await client.download_media(message, bytes)

        # Wrap in BytesIO and set the original filename so Telegram preserves it
        file_obj = io.BytesIO(file_bytes)
        file_obj.name = filename or 'file'

        await client.send_file(
            TARGET_CHANNEL,
            file_obj,
            caption=message.message or None,
            force_document=True,
        )
        logger.info(f"Sent message {message.id} ({filename}) to {TARGET_CHANNEL}")
    except Exception as e:
        logger.error(f"Error sending message {message.id}: {e}")


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

    await client.start(phone=PHONE_NUMBER)
    me = await client.get_me()
    logger.info(f"Logged in as {me.first_name} (@{me.username})")
    logger.info(f"Monitoring: {SOURCE_CHANNEL} → {TARGET_CHANNEL}")
    logger.info("Waiting for new files...")
    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
