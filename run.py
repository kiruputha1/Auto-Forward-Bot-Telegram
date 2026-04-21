#!/usr/bin/env python3
"""
Telegram File Forward Bot - Startup Script (Telethon)
"""

import sys
import os


def check_requirements():
    try:
        import telethon
        import dotenv
        print("All required packages are installed")
        return True
    except ImportError as e:
        print(f"Missing package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False


def check_env_file():
    if not os.path.exists('.env'):
        print(".env file not found!")
        print("Copy .env.example to .env and fill in your values")
        return False

    from dotenv import load_dotenv
    load_dotenv()

    required_vars = ['API_ID', 'API_HASH', 'PHONE_NUMBER', 'SOURCE_CHANNEL', 'TARGET_CHANNEL']
    missing = [v for v in required_vars if not os.getenv(v)]

    if missing:
        print(f"Missing environment variables: {', '.join(missing)}")
        print("Please edit .env with your actual values")
        return False

    print("Environment configuration looks good")
    return True


def main():
    print("Telegram File Forward Bot - Starting Up")
    print("=" * 50)

    if not check_requirements():
        sys.exit(1)

    if not check_env_file():
        sys.exit(1)

    print("=" * 50)
    print("Starting bot...")
    print("On first run you will be asked for your phone verification code.")

    try:
        import asyncio
        from bot import main as bot_main
        asyncio.run(bot_main())
    except KeyboardInterrupt:
        print("\nBot stopped.")
    except Exception as e:
        print(f"Failed to start bot: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
