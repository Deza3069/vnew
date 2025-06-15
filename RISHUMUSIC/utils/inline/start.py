from pyrogram.types import InlineKeyboardButton

import config
from RISHUMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
           InlineKeyboardButton(text="ᴀʙᴏᴜᴛ", callback_data="dev")
        ],

        [
            InlineKeyboardButton(text="ᴍᴜsɪᴄ", callback_data="GSONG_CP")
        ],
    ]
    return buttons
