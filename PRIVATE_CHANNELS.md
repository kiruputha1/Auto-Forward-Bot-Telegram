# Private Channels Setup Guide

This guide provides step-by-step instructions for setting up the bot with private Telegram channels.

## 🚀 Quick Setup for Private Channels

### Step 1: Get Your Bot Token

1. Talk to [@BotFather](https://t.me/botfather) on Telegram
2. Use `/newbot` to create a new bot
3. Copy the bot token (looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 2: Add Bot to Private Channels

1. Go to your private channel settings
2. Add your bot as an **administrator**
3. Grant these permissions:
   - **Source Channel**: Read messages, Delete messages (optional)
   - **Target Channel**: Send messages, Send media, Edit messages (optional)

### Step 3: Get Channel IDs (Easy Method)

Use our helper script:

```bash
py get_channel_id.py
```

Then:

1. Forward any message from your source channel to the bot
2. Forward any message from your target channel to the bot
3. The script will show you both channel IDs

### Step 4: Configure Your Bot

1. Copy `.env.example` to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your values:
   ```env
   BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   SOURCE_CHANNEL=-1001234567890
   TARGET_CHANNEL=-1000987654321
   ADMIN_USER_ID=your_telegram_user_id
   ```

### Step 5: Start the Bot

```bash
py run.py
```

## 🔍 Alternative Methods to Get Channel IDs

### Method 1: Using @userinfobot

1. Forward any message from your private channel to [@userinfobot](https://t.me/userinfobot)
2. The bot will reply with channel information including the numeric ID

### Method 2: Using @JsonDumpBot

1. Add [@JsonDumpBot](https://t.me/JsonDumpBot) to your private channel
2. Send any message to the channel
3. The bot will reply with JSON data
4. Look for `"chat":{"id":-1001234567890,...}` in the response

### Method 3: Using Telegram Web

1. Open [web.telegram.org](https://web.telegram.org)
2. Go to your private channel
3. Check the URL for channel ID
4. Add `-100` prefix for bot usage

## 📋 Configuration Examples

### Both Channels Private

```env
BOT_TOKEN=your_bot_token_here
SOURCE_CHANNEL=-1001234567890
TARGET_CHANNEL=-1000987654321
ADMIN_USER_ID=123456789
```

### Source Private, Target Public

```env
BOT_TOKEN=your_bot_token_here
SOURCE_CHANNEL=-1001234567890
TARGET_CHANNEL=@publictargetchannel
ADMIN_USER_ID=123456789
```

### Both Channels Public

```env
BOT_TOKEN=your_bot_token_here
SOURCE_CHANNEL=@publicsource
TARGET_CHANNEL=@publictarget
ADMIN_USER_ID=123456789
```

## ⚠️ Important Notes

### Bot Permissions

- **Private channels require the bot to be an administrator**
- Regular members cannot access channel messages
- Make sure to grant appropriate permissions

### Channel ID Format

- **Private channels**: Always negative numbers (e.g., `-1001234567890`)
- **Public channels**: Always start with `@` (e.g., `@channelname`)
- **Never mix formats** - use the correct format for each channel type

### Troubleshooting

**Bot can't read messages:**

- Check if bot is an administrator
- Verify bot has "Read messages" permission
- Make sure channel ID is correct

**Bot can't send messages:**

- Check if bot is an administrator in target channel
- Verify bot has "Send messages" permission
- Make sure target channel ID is correct

**Channel ID not working:**

- Double-check the ID format (private = -100..., public = @...)
- Use the helper script to verify IDs
- Make sure bot is added to both channels

## 🆘 Getting Help

If you encounter issues:

1. **Check the logs**: Run the bot and look for error messages
2. **Verify permissions**: Ensure bot is admin in private channels
3. **Test with public channels first**: To isolate the issue
4. **Use the helper script**: `py get_channel_id.py` to verify IDs

## 🎯 Success Checklist

- [ ] Bot token obtained from BotFather
- [ ] Bot added as admin to both private channels
- [ ] Correct permissions granted
- [ ] Channel IDs obtained (negative format for private)
- [ ] `.env` file configured correctly
- [ ] Bot starts without errors
- [ ] `/forward_last` command works
- [ ] Automatic forwarding works

Once all items are checked, your private channel forwarding bot should be working perfectly! 🎉
