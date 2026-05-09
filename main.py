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
app.add_handler(filters.group & filters.command("tagall"), handlers.tag_all)

print("✅ Security Bot is running...")

if __name__ == "__main__":
    asyncio.run(app.start())
    asyncio.get_event_loop().run_until_complete(app.idle())
    asyncio.run(app.stop())
