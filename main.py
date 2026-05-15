from pyrogram import Client, filters
from config import *

API_ID = 123456
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Client(
    "tagallbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("tagall"))
async def tag_all(client, message):
    chat_id = message.chat.id

    text = "Everyone Attention!\n\n"

    async for member in app.get_chat_members(chat_id):
        user = member.user
        if not user.is_bot:
            text += f"[{user.first_name}](tg://user?id={user.id}) "

    await message.reply_text(text)

app.run()
