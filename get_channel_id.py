#!/usr/bin/env python3
"""
Helper script to get channel IDs for private Telegram channels
"""

import os
from dotenv import load_dotenv
from telegram import Bot
import asyncio

async def get_channel_info():
    """Get information about a channel to find its ID"""
    load_dotenv()
    
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token or bot_token.startswith('your_'):
        print("❌ Please set your BOT_TOKEN in .env file first!")
        return
    
    bot = Bot(token=bot_token)
    
    print("🔍 Channel ID Finder")
    print("=" * 50)
    print("This script helps you find private channel IDs.")
    print("You need to:")
    print("1. Add your bot to the private channel as admin")
    print("2. Forward a message from that channel to this bot")
    print("3. The script will show you the channel ID")
    print("=" * 50)
    
    try:
        print("\n📡 Waiting for forwarded messages...")
        print("Forward any message from your private channel to this bot...")
        print("(Press Ctrl+C to stop)")
        
        # Get updates to find forwarded messages
        async for update in bot.get_updates(timeout=30):
            if update.message and update.message.forward_from_chat:
                chat = update.message.forward_from_chat
                print(f"\n✅ Found channel information:")
                print(f"📛 Channel Name: {chat.title}")
                print(f"🆔 Channel ID: {chat.id}")
                print(f"🔗 Username: @{chat.username}" if chat.username else "🔗 Username: None (Private)")
                print(f"📝 Type: {'Channel' if chat.type == 'channel' else 'Group'}")
                
                if chat.type == 'channel':
                    print(f"\n📋 Use this in your .env file:")
                    print(f"SOURCE_CHANNEL={chat.id}")
                    print(f"TARGET_CHANNEL={chat.id}")
                    print(f"\n💡 For private channels, the ID will be negative (e.g., -1001234567890)")
                
                break
            elif update.message:
                print(f"📨 Received message from chat ID: {update.message.chat.id}")
                if update.message.forward_from_chat:
                    print("   (This is a forwarded message)")
                else:
                    print("   (This is not a forwarded message)")
                    print("   Please forward a message FROM the channel you want to identify")
                    
    except KeyboardInterrupt:
        print("\n👋 Stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Troubleshooting:")
        print("1. Make sure your bot token is correct")
        print("2. Make sure you've added the bot to the channel")
        print("3. Make sure the bot is an admin in the channel")
        print("4. Try forwarding a different message")

if __name__ == '__main__':
    asyncio.run(get_channel_info())