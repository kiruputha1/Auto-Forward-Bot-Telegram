# Telegram File Forward Bot

A Python-based Telegram bot that automatically forwards files (photos, videos, documents, audio, etc.) from one channel to another.

## Features

- 🔄 Automatic file forwarding between channels
- 📁 Supports all file types (photos, videos, documents, audio, voice notes, stickers)
- ⚡ Real-time forwarding
- 🔒 Secure configuration using environment variables
- 📊 Admin commands for monitoring
- 🛡️ Duplicate message prevention
- 📝 Caption preservation
- ⏮️ Manual forwarding of last 5 messages
- 🔒 Full support for private channels

## Prerequisites

- Python 3.7 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Access to both source and target channels

## Setup

### 1. Clone or Download

```bash
git clone <repository-url>
cd fwd-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create Configuration File

Copy the example configuration file:

```bash
cp .env.example .env
```

**Optional: Use Helper Script to Get Channel IDs**

```bash
py get_channel_id.py
```

This script will help you find private channel IDs by detecting forwarded messages.

Edit the `.env` file with your actual values:

```env
# Get your bot token from BotFather on Telegram
BOT_TOKEN=your_actual_bot_token_here

# Source channel ID (where files come from)
# Use @username for public channels or numeric ID for private channels
SOURCE_CHANNEL=@your_source_channel

# Target channel ID (where files will be forwarded to)
# Use @username for public channels or numeric ID for private channels
TARGET_CHANNEL=@your_target_channel

# Optional: Add admin user ID for bot control commands
ADMIN_USER_ID=your_admin_user_id
```

### 4. Get Channel IDs

**For Public Channels:**

- Use the username format: `@channelname`

**For Private Channels:**

1. Add your bot to the channel
2. Forward any message from the channel to [@userinfobot](https://t.me/userinfobot)
3. The bot will show you the channel's numeric ID

### 5. Add Bot to Channels

**For Public Channels:**

1. Add your bot to both the source and target channels
2. Make sure the bot has permission to:
   - Read messages in the source channel
   - Send messages in the target channel

**For Private Channels:**

1. Add your bot as an **administrator** to both private channels
2. Grant the following permissions:
   - **Source Channel**:
     - Read messages
     - Delete messages (optional, for cleanup)
     - Invite users (if needed)
   - **Target Channel**:
     - Send messages
     - Send media
     - Edit messages (optional)
     - Delete messages (optional)

**Important Notes for Private Channels:**

- The bot must be an administrator in private channels to access messages
- Private channel IDs are negative numbers (format: -1001234567890)
- Make sure the bot is added before trying to use the `/forward_last` command

## Usage

### Start the Bot

```bash
python bot.py
```

The bot will start running and automatically forward files from the source channel to the target channel.

### Bot Commands

- `/start` - Show welcome message and bot info
- `/status` - Show bot status and statistics (admin only)
- `/forward_last` - Manually forward the last 5 messages from source channel (admin only)

## Supported File Types

- 📷 Photos
- 🎥 Videos
- 📄 Documents
- 🎵 Audio files
- 🎤 Voice notes
- 🎬 Video notes
- 😄 Stickers

## Configuration Options

| Variable         | Required | Description                              |
| ---------------- | -------- | ---------------------------------------- |
| `BOT_TOKEN`      | Yes      | Your bot token from BotFather            |
| `SOURCE_CHANNEL` | Yes      | Channel ID to forward from               |
| `TARGET_CHANNEL` | Yes      | Channel ID to forward to                 |
| `ADMIN_USER_ID`  | No       | Your Telegram user ID for admin commands |

## Troubleshooting

### Bot Not Forwarding Files

1. **Check Bot Permissions**: Ensure the bot is added to both channels with proper permissions
2. **Verify Channel IDs**: Make sure the channel IDs in `.env` are correct
3. **Check Bot Token**: Verify your bot token is valid
4. **Review Logs**: Check the console output for error messages

### Getting Channel ID

For private channels, use [@userinfobot](https://t.me/userinfobot):

1. Forward any message from the private channel to @userinfobot
2. The bot will reply with the channel information including the numeric ID

### Bot Token Issues

1. Contact [@BotFather](https://t.me/botfather) on Telegram
2. Use `/newbot` to create a new bot
3. Copy the token provided by BotFather

## Security Notes

- Never share your bot token publicly
- Keep your `.env` file private and add it to `.gitignore`
- Only add trusted admins to your bot
- Regularly rotate your bot token if needed

## Deployment

### Running on a Server

For production deployment, consider using:

1. **Screen/Tmux**: Keep the bot running after SSH disconnect

   ```bash
   screen -S forward-bot
   python bot.py
   # Press Ctrl+A then D to detach
   ```

2. **Systemd Service**: Create a systemd service for auto-restart
3. **Docker**: Containerize the application for easy deployment

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
```

Build and run:

```bash
docker build -t telegram-forward-bot .
docker run -d --name forward-bot --restart unless-stopped telegram-forward-bot
```

## Helper Scripts

### get_channel_id.py

A helper script to easily find private channel IDs:

```bash
py get_channel_id.py
```

**How to use:**

1. Add your bot token to `.env` file
2. Run the script
3. Forward any message from your private channel to the bot
4. The script will display the channel ID and configuration

**Features:**

- 🔍 Automatically detects forwarded messages
- 📋 Shows channel name, ID, and type
- 💡 Provides ready-to-use configuration
- 🛡️ Handles errors gracefully

📖 **For detailed step-by-step instructions, see [USAGE_GUIDE.md](USAGE_GUIDE.md)**

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Feel free to use, modify, and distribute according to your needs.

## Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the logs for error messages
3. Ensure all configuration values are correct
4. Verify bot permissions in both channels

---

**Note**: This bot is designed for educational and legitimate use only. Ensure you have proper permissions and comply with Telegram's Terms of Service and applicable laws when using this bot.
