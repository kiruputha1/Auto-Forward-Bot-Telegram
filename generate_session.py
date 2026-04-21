"""
Run this script ONCE locally to generate a SESSION_STRING.
Copy the printed string into your .env / apply.build environment variables.
"""

import asyncio
import os
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')


async def main():
    async with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        await client.start(phone=PHONE_NUMBER)
        session_string = client.session.save()
        print("\n" + "=" * 60)
        print("Your SESSION_STRING (add this to your environment variables):")
        print("=" * 60)
        print(session_string)
        print("=" * 60 + "\n")


if __name__ == '__main__':
    asyncio.run(main())
