from pyrogram.types import Message

async def delete_links(client, message: Message):
    if "http" in message.text.lower():
        await message.delete()

async def delete_nsfw(client, message: Message):
    if any(word in message.text.lower() for word in ["nsfw", "xxx", "porn"]):
        await message.delete()

async def delete_sticker(client, message: Message):
    await message.delete()

async def flood_control(client, message: Message):
    if len(message.text) > 500:
        await message.delete()

async def monitor_bans(client, message: Message):
    # Placeholder for ban monitoring
    pass

async def tag_all(client, message: Message):
    chat_members = []
    async for member in client.get_chat_members(message.chat.id, limit=20):
        chat_members.append(member.user.mention)
    await message.reply_text("👥 Tagging everyone:\n" + " ".join(chat_members))
