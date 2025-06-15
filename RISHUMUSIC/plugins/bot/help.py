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









@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)















#------------------------------------------------------------------------------------------------------------------------
# MANAGEMENT | MANAGEMENT | MANAGEMENT | MANAGEMENT | MANAGEMENT | MANAGEMENT | MANAGEMENT | MANAGEMENT | MANAGEMENT | 
#------------------------------------------------------------------------------------------------------------------------





@app.on_callback_query(filters.regex("MANAGEMENT_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_M, reply_markup=InlineKeyboardMarkup(BUTTONS.MBUTTON))
    
        
@app.on_callback_query(filters.regex('MANAGEMENT_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(
    [
    [
    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"MANAGEMENT_CP")
    ]
    ]
    )
    if cb == "MANAGEMENT":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)





#------------------------------------------------------------------------------------------------------------------------
# TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL |
#------------------------------------------------------------------------------------------------------------------------





@app.on_callback_query(filters.regex("TOOL_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_B, reply_markup=InlineKeyboardMarkup(BUTTONS.BBUTTON))


@app.on_callback_query(filters.regex('TOOL_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(
    [
    [
    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"TOOL_CP")
    ]
    ]
    )
    if cb == "TOOL":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)






#------------------------------------------------------------------------------------------------------------------------
# MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP |
#------------------------------------------------------------------------------------------------------------------------





@app.on_callback_query(filters.regex("MAIN_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_SACHIN, reply_markup=InlineKeyboardMarkup(BUTTONS.SBUTTON))

        
@app.on_callback_query(filters.regex('MAIN_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(
    [
    [
    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"MAIN_CP")
    ]
    ]
    )
    if cb == "MAIN":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)




#------------------------------------------------------------------------------------------------------------------------
# PROMOTION | PROMOTION | PROMOTION | PROMOTION | PROMOTION | PROMOTION | PROMOTION | PROMOTION | PROMOTION | PROMOTION |
#------------------------------------------------------------------------------------------------------------------------


@app.on_callback_query(filters.regex("PROMOTION_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_PROMOTION, reply_markup=InlineKeyboardMarkup(BUTTONS.PBUTTON))

        
@app.on_callback_query(filters.regex('PROMOTION_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(
    [
    [
    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"PROMOTION_CP")
    ]
    ]
    )
    if cb == "PROMOTION":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)

        
        

#------------------------------------------------------------------------------------------------------------------------
# ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | 
#------------------------------------------------------------------------------------------------------------------------



@app.on_callback_query(filters.regex("ALLBOT_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_ALLBOT, reply_markup=InlineKeyboardMarkup(BUTTONS.ABUTTON))

        
@app.on_callback_query(filters.regex('ALLBOT_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(
    [
    [
    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"ALLBOT_CP")
    ]
    ]
    )
    if cb == "ALLBOT":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)




@app.on_callback_query(filters.regex("anime_back"))
async def anime_callback(client: Client, query: CallbackQuery):
    random_image = random.choice(IMAGES)
    await query.message.edit_text(
        ANIME_STRINGS.format(random_image),  
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴀɴɪᴍᴇ", callback_data="anime"),
                    InlineKeyboardButton("ᴍᴀɴɢᴀ", callback_data="manga"),
                ],
                [
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="settingsback_helper"),
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("^(anime|manga)$"))
async def anime_manga_callback(client: Client, query: CallbackQuery):
    if query.data == "anime":
        anime_buttons = [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="anime_back")]]
        await query.message.edit_text(
            text=ANIME,
            disable_web_page_preview=False,
            reply_markup=InlineKeyboardMarkup(anime_buttons),
        )
    
    elif query.data == "manga":
        manga_buttons = [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="anime_back")]]
        await query.message.edit_text(
            text=MANGA,
            disable_web_page_preview=False,
            reply_markup=InlineKeyboardMarkup(manga_buttons),
        )






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
    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"GSONG_CP")
    ]
    ]
    )
    if cb == "GSONG":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)





#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
