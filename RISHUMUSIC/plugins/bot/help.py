from typing import Union
import random
from pyrogram import Client
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton, CallbackQuery
from RISHUMUSIC import app
from RISHUMUSIC.utils.halpers import *
from RISHUMUSIC.utils import help_pannel
from RISHUMUSIC.utils.database import get_lang
from RISHUMUSIC.utils.decorators.language import LanguageStart, languageCB
from RISHUMUSIC.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers
from RISHUMUSIC.help.buttons import BUTTONS
from RISHUMUSIC.help.helper import Helper


#------------------------------------------------------------------------------------------------------------------------
# MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | 
#------------------------------------------------------------------------------------------------------------------------
#music





@app.on_callback_query(filters.regex("GSONG_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_G, reply_markup=InlineKeyboardMarkup(BUTTONS.GBUTTON))
    
        
@app.on_callback_query(filters.regex('GSONG_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(
    [
    [
    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"GSONG_CP"),
    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data=f"about_call"),
    ]
    ]
    )
    if cb == "GSONG":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)


@app.on_callback_query(filters.regex("about_call") & ~BANNED_USERS)
async def support_info_callback(client, CallbackQuery):
    about_text =(
                f"<blockquote><b>ʏᴀʀᴇ ʏᴀʀᴇ <a href='https://envs.sh/QRq.png' target='_blank'>🔱</a></b></blockquote>\n\n"
                f"<blockquote><b>ғᴀᴄɪɴɢ ɪssᴜᴇs ᴡɪᴛʜ ʙᴏᴛ?.</b>\n"
                f"<b>ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛᴏ ᴡᴏʀʀʏ. ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ ʀᴇᴀᴄʜ ᴜs ᴀɴᴅ ʀᴇᴘᴏʀᴛ ᴏᴜʀ ʙᴏᴛs!</b></blockquote>\n\n"
                f"<blockquote><b>ᴍᴀᴅᴇ ʙʏ [Aɪᴢᴇɴ](https://t.me/tfaizen)</b></blockquote>"
                )

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/soul_x_network"),
            InlineKeyboardButton("ɢʀᴏᴜᴘ", url="https://t.me/Espada_relame")
        ],
        [
            InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="settingsback_helper")
        ]
    ])

    await CallbackQuery.edit_message_text(about_text, reply_markup=buttons)


@app.on_callback_query(filters.regex("dev"))
async def dev_callback(client: Client, query: CallbackQuery):
    random_image = random.choice(IMAGES)

    buttons = [
        [InlineKeyboardButton("🔱 ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ 🔱", url=f"https://t.me/{app.username}?startgroup=true")],
        [
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url="https://t.me/soul_x_network"),
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/soul_x_society"),
        ],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="back")]
    ]

    await query.message.edit_text(
        text=SUPPORT_STRINGS.format(random_image),
        disable_web_page_preview=False,  # Prevents preview if it's an image link
        reply_markup=InlineKeyboardMarkup(buttons),
    )

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
