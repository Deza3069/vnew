from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def stats_buttons(_, status):
    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_1"],
            callback_data="bot_stats_sudo",
        ),
        InlineKeyboardButton(
            text=_["SA_B_2"],
            callback_data="TopOverall",
        ),
    ]
    upl = InlineKeyboardMarkup(
        [
            sudo,
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl

def back_stats_buttons(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="stats_back",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl

def execute_stats(_, status, is_sudo):
    if is_sudo:
        return stats_buttons(_, status)
    else:
        return normal_user_response()

def normal_user_response():
    return "ᴋɪᴅ ɢʀᴏᴡ ᴜᴘ ғɪʀsᴛ. ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴄᴀᴘᴀʙʟᴇ ᴇɴᴏᴜɢʜ ᴛᴏ ᴅᴏ ᴛʜɪs."
