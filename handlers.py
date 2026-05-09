# handlers.py
from pyrogram import filters
from filters import link_pattern, nsfw_pattern, user_messages, admin_ban_count

# --- BioLink Delete ---
async def delete_links(client, message):
    if link_pattern.search(message.text):
        await message.delete()
        await message.reply_text("⚠️ Links are not allowed here!")

# --- Anti-NSFW ---
async def delete_nsfw(client, message):
    if nsfw_pattern.search(message.text):
        await message.delete()
        await message.reply_text("🚫 NSFW content is not allowed!")

# --- Anti-Sticker ---
async def delete_sticker(client, message):
    await message.delete()
    await message.reply_text("🚫 Stickers are restricted in this group!")

# --- Anti-Flood ---
async def flood_control(client, message):
    user_id = message.from_user.id
    user_messages[user_id].append(message.date)

    if len(user_messages[user_id]) > 5:
        user_messages[user_id] = user_messages[user_id][-5:]

    if (user_messages[user_id][-1] - user_messages[user_id][0]).seconds < 10:
        await message.delete()
        await message.reply_text("🌊 Flood detected! Please slow down.")

# --- Anti-Banall ---
async def monitor_bans(client, event):
    if event.new_chat_member.status == "kicked":
        admin_id = event.from_user.id
        admin_ban_count[admin_id] += 1

        if admin_ban_count[admin_id] >= 3:
            await client.kick_chat_member(event.chat.id, admin_id)
            await client.send_message(event.chat.id, f"⚠️ Admin {event.from_user.mention} removed for mass banning!")