# Usage Guide - How to Run the Helper Script

## 🚀 Quick Start: Getting Channel IDs

### Step 1: Install Dependencies

```bash
py -m pip install -r requirements.txt
```

### Step 2: Configure Bot Token

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your bot token:
   ```env
   BOT_TOKEN=your_actual_bot_token_here
   SOURCE_CHANNEL=@source_channel
   TARGET_CHANNEL=@target_channel
   ADMIN_USER_ID=your_admin_user_id
   ```

### Step 3: Run the Helper Script

```bash
py get_channel_id.py
```

### Step 4: Follow the On-Screen Instructions

The script will:

1. Show a welcome message
2. Wait for you to forward messages from your channels
3. Display the channel IDs when detected

## 📱 Step-by-Step Process

### What You Need:

- Your bot token from [@BotFather](https://t.me/botfather)
- Access to the private channels you want to use
- Your bot added to those channels as administrator

### Running the Script:

1. **Open Command Prompt/Terminal**

   ```bash
   cd path/to/fwd-bot
   ```

2. **Run the Script**

   ```bash
   py get_channel_id.py
   ```

3. **The Script Will Display:**

   ```
   🔍 Channel ID Finder
   ==================================================
   This script helps you find private channel IDs.
   You need to:
   1. Add your bot to the private channel as admin
   2. Forward a message from that channel to this bot
   3. The script will show you the channel ID
   ==================================================

   📡 Waiting for forwarded messages...
   Forward any message from your private channel to this bot...
   (Press Ctrl+C to stop)
   ```

4. **Forward Messages to Your Bot**

   - Go to Telegram
   - Find your bot (search by its username)
   - Forward a message from your source channel to the bot
   - Forward a message from your target channel to the bot

5. **Script Will Show Results:**

   ```
   ✅ Found channel information:
   📛 Channel Name: My Private Channel
   🆔 Channel ID: -1001234567890
   🔗 Username: None (Private)
   📝 Type: Channel

   📋 Use this in your .env file:
   SOURCE_CHANNEL=-1001234567890
   TARGET_CHANNEL=-1001234567890

   💡 For private channels, the ID will be negative (e.g., -1001234567890)
   ```

## 🔧 Troubleshooting

### Common Issues:

**1. "Please set your BOT_TOKEN in .env file first!"**

- Solution: Add your bot token to the `.env` file

**2. Script doesn't detect forwarded messages**

- Make sure your bot is added to the channel as administrator
- Check that you're forwarding messages FROM the channel TO the bot
- Verify the bot token is correct

**3. "Error: ..." messages**

- Check your internet connection
- Verify the bot token is valid
- Make sure the bot is running and accessible

## 📋 Complete Workflow Example

### 1. Setup Bot Token

```bash
# Edit .env file
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
SOURCE_CHANNEL=@temp_source
TARGET_CHANNEL=@temp_target
ADMIN_USER_ID=123456789
```

### 2. Run Helper Script

```bash
py get_channel_id.py
```

### 3. Forward Messages in Telegram

- Open chat with your bot
- Forward message from source channel
- Forward message from target channel
- Note the channel IDs shown

### 4. Update .env with Real IDs

```bash
# Edit .env file with actual channel IDs
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
SOURCE_CHANNEL=-1001234567890
TARGET_CHANNEL=-1000987654321
ADMIN_USER_ID=123456789
```

### 5. Run the Main Bot

```bash
py run.py
```

## 🎯 Success Indicators

✅ **Script starts without errors**  
✅ **Shows "Waiting for forwarded messages..."**  
✅ **Detects forwarded messages**  
✅ **Displays channel information**  
✅ **Provides ready-to-use configuration**

## 🆘 Getting Help

If you encounter issues:

1. **Check the error message** - The script provides helpful error messages
2. **Verify bot permissions** - Bot must be admin in private channels
3. **Test with public channels first** - To isolate the issue
4. **Check your bot token** - Make sure it's valid and not expired

## 📞 Additional Resources

- [BotFather](https://t.me/botfather) - Create and manage your bot
- [PRIVATE_CHANNELS.md](PRIVATE_CHANNELS.md) - Detailed private channel setup
- [README.md](README.md) - Main documentation

---

**💡 Pro Tip:** Keep the helper script handy - you can use it anytime to find new channel IDs or verify existing ones!
