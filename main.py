import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
import handlers

# Create bot client
app = Client(
    "SecurityBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register handlers
app.add_handler(filters.group & filters.text, handlers.delete_links)
app.add_handler(filters.group & filters.text, handlers.delete_nsfw)
app.add_handler(filters.group & filters.sticker, handlers.delete_sticker)
app.add_handler(filters.group, handlers.flood_control)
app.add_handler(filters.group, handlers.monitor_bans)

print("✅ Security Bot is running...")

if __name__ == "__main__":
    # Run bot with proper event loop
    asyncio.run(app.run())
