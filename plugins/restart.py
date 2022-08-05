import os
import sys
import asyncio
from pyrogram import Client, filters
from info import ADMINS

@Client.on_message(filters.private & filters.command(['restart']))                         
async def restart(bot, message):
    if message.from_user.id != ADMINS:
        await message.reply_text("sorry bro this bot is admin only use. Please make your owen bot.\nbot repo https://github.com/MrMKN/Eva-Forward-Bot ", disable_web_page_preview = True)                      
        return
    while True:
        try:
            msg = await message.reply_text(
            text="<i>Trying to restarting.....</i>"
            )
            await asyncio.sleep(5)
            await msg.edit("<i>Server restarted successfully ✅</i>")
            os.execl(sys.executable, sys.executable, *sys.argv)
