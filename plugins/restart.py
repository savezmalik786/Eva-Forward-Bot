import os
import sys
import asyncio
from pyrogram import Client, filters
from info import ADMINS

@Client.on_message(filters.private & filters.command(['restart']) & filters.user(ADMINS))                         
async def restart(bot, message):
    msg = await message.reply_text(
    text="<i>Trying to restarting.....</i>"
    )
    await msg.edit("<i>Server restarted successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)
