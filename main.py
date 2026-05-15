import asyncio

asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, filters
from config import *

app = Client(
    "TagAllBot",
    api_id=37535960,
    api_hash="e89c6a21da912026e645f4132bd4eba7",
    bot_token="8721566005:AAHvdIHLgElJRBgdr8WaVaG8UXnndUevZAE"
)

@app.on_message(filters.command("tagall"))
async def tagall(client, message):
    text = ""

    async for member in app.get_chat_members(message.chat.id):
        if not member.user.is_bot:
            text += f"[{member.user.first_name}](tg://user?id={member.user.id}) "

    await message.reply_text(text)

app.run()
