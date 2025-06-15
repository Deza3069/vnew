from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from RISHUMUSIC import app

class BUTTONS(object):
    BBUTTON = [
        [
            InlineKeyboardButton("ᴧɪ | ᴄʜᴧᴛɢᴘᴛ", callback_data="TOOL_BACK HELP_01"),
        ],
        [
            InlineKeyboardButton("sᴇᴀʀᴄʜ", callback_data="TOOL_BACK HELP_02"),
            InlineKeyboardButton("ᴛᴛs", callback_data="TOOL_BACK HELP_03"),
            InlineKeyboardButton("ɪɴғᴏ", callback_data="TOOL_BACK HELP_04"),
        ],
        [
            InlineKeyboardButton("ғᴏɴᴛ", callback_data="TOOL_BACK HELP_05"),
            InlineKeyboardButton("ᴍᴀᴛʜ", callback_data="TOOL_BACK HELP_06"),
            InlineKeyboardButton("ᴛᴀɢᴀʟʟ", callback_data="TOOL_BACK HELP_07"),
        ],
        [
            InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data="TOOL_BACK HELP_08"),
            InlineKeyboardButton("ʜᴀsᴛᴀɢ", callback_data="TOOL_BACK HELP_09"),
            InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="TOOL_BACK HELP_10"),
        ],
        [
            InlineKeyboardButton("ғᴜɴ", callback_data="TOOL_BACK HELP_11"),
            InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="TOOL_BACK HELP_12"),
            InlineKeyboardButton("ᴛ-ᴅ", callback_data="TOOL_BACK HELP_13"),
        ],
        [   
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"MAIN_CP"),]
        ]
    
    MBUTTON = [
                [
            InlineKeyboardButton("єxᴛʀᴧ", callback_data="MANAGEMENT_BACK HELP_25"),
        ],
        [
            InlineKeyboardButton("ʙᴀɴ", callback_data="MANAGEMENT_BACK HELP_14"),
            InlineKeyboardButton("ᴋɪᴄᴋ", callback_data="MANAGEMENT_BACK HELP_15"),
            InlineKeyboardButton("ᴍᴜᴛᴇ", callback_data="GSONG_BACK HELP_16"),
        ],
        [
            InlineKeyboardButton("ᴘɪɴ", callback_data="MANAGEMENT_BACK HELP_17"),
            InlineKeyboardButton("sᴛᴀғғ", callback_data="MANAGEMENT_BACK HELP_18"),
            InlineKeyboardButton("sᴇᴛ-ᴜᴘ", callback_data="MANAGEMENT_BACK HELP_19"),
        ],
        [
            InlineKeyboardButton("ᴢᴏᴍʙɪᴇ", callback_data="MANAGEMENT_BACK HELP_20"),
            InlineKeyboardButton("ɢᴀᴍᴇ", callback_data="MANAGEMENT_BACK HELP_21"),
            InlineKeyboardButton("ɪᴍᴘᴏsᴛᴇʀ", callback_data="MANAGEMENT_BACK HELP_22"),
        ],
        [
            InlineKeyboardButton("sɢ", callback_data="MANAGEMENT_BACK HELP_23"),
            InlineKeyboardButton("ᴛʀ", callback_data="MANAGEMENT_BACK HELP_24"),
            InlineKeyboardButton("ɢʀᴧᴘʜ", callback_data="MANAGEMENT_BACK HELP_26"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"MAIN_CP"), 
        ]
        ]
    GBUTTON = [
        [
            InlineKeyboardButton("ᴀᴅᴍɪɴ", callback_data="GSONG_BACK HELP_28"),
            InlineKeyboardButton("ᴀᴜᴛʜ", callback_data="GSONG_BACK HELP_29"),
            InlineKeyboardButton("ᴄᴘʟᴀʏ", callback_data="GSONG_BACK HELP_30"),
        ],
        [
            InlineKeyboardButton("ʟᴏᴏᴘ", callback_data="GSONG_BACK HELP_31"),
            InlineKeyboardButton("ᴘʟᴀʏ", callback_data="GSONG_BACK HELP_32"),
            InlineKeyboardButton("ᴘʟᴀʏʟɪsᴛ", callback_data="GSONG_BACK HELP_33"),
        ],
        [
            InlineKeyboardButton("sʜᴜғғʟᴇ", callback_data="GSONG_BACK HELP_34"),
            InlineKeyboardButton("sᴇᴇᴋ", callback_data="GSONG_BACK HELP_35"),
            InlineKeyboardButton("sᴘᴇᴇᴅ", callback_data="GSONG_BACK HELP_36"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"MAIN_CP"), 
        ],
        ]
    
    ABUTTON = [
        [
            InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/ur_rishu_143"),
            InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/ur_support07"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    SBUTTON = [
        [
            InlineKeyboardButton("ᴍᴜsɪᴄ", callback_data="GSONG_CP"),
            InlineKeyboardButton("ᴍᴀɴᴀɢᴇᴍᴇɴᴛ", callback_data="MANAGEMENT_CP"),
        ],
        [
            InlineKeyboardButton("ᴛᴏᴏʟs", callback_data="TOOL_CP"),
            InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs", url="https://t.me/AizenXprobot?start=help"),
        ],
        [
            InlineKeyboardButton("ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ",  callback_data="settingsback_helper"),
            
        ]
  ]
