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
            InlineKeyboardButton(text=_["S_B_3"],url=f"https://t.me/{app.username}?startgroup=true",)
        ],

        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="MAIN_CP"),
            InlineKeyboardButton(text="ᴀɴɪᴍᴇ", callback_data="anime_back"),
        ],
    ]
    return buttons
