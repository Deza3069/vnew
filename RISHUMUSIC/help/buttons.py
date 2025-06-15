from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from RISHUMUSIC import app

class BUTTONS(object):
    GBUTTON = [
        [
            InlineKeyboardButton("ᴀᴅᴍɪɴ", callback_data="GSONG_BACK HELP_1"),
            InlineKeyboardButton("ᴀᴜᴛʜ", callback_data="GSONG_BACK HELP_2"),
            InlineKeyboardButton("ᴄᴘʟᴀʏ", callback_data="GSONG_BACK HELP_3"),
        ],
        [
            InlineKeyboardButton("ʟᴏᴏᴘ", callback_data="GSONG_BACK HELP_4"),
            InlineKeyboardButton("ᴘʟᴀʏ", callback_data="GSONG_BACK HELP_5"),
            InlineKeyboardButton("ᴘʟᴀʏʟɪsᴛ", callback_data="GSONG_BACK HELP_6"),
        ],
        [
            InlineKeyboardButton("sʜᴜғғʟᴇ", callback_data="GSONG_BACK HELP_7"),
            InlineKeyboardButton("sᴇᴇᴋ", callback_data="GSONG_BACK HELP_8"),
            InlineKeyboardButton("sᴘᴇᴇᴅ", callback_data="GSONG_BACK HELP_9"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data="settingsback_helper"), 
        ],
        ]
    
 
    
  
