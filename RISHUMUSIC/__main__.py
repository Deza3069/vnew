import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from RISHUMUSIC import LOGGER, app, userbot
from RISHUMUSIC.core.call import RISHU
from RISHUMUSIC.misc import sudo
from RISHUMUSIC.plugins import ALL_MODULES
from RISHUMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS



async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 V2 𝐒𝐞𝐬𝐬𝐢𝐨𝐧🤬"
        )

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            if user_id not in BANNED_USERS:
                BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("RISHUMUSIC.plugins" + all_module)
    LOGGER("RISHUMUSIC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")

    await userbot.start()

    await RISHU.start()
    await RISHU.decorators()
    
    LOGGER("RISHUMUSIC").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝗥𝗜𝗦𝗛𝗨♨️\n╚═════ஜ۩۞۩ஜ════╝")
    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER("RISHUMUSIC").info(
        "                 ╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝗥𝗜𝗦𝗛𝗨♨️\n╚═════ஜ۩۞۩ஜ════╝"
    )


if __name__ == "__main__":

    asyncio.get_event_loop().run_until_complete(init())
