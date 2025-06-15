import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 25695415
API_HASH = "38a4b64f718fbe909cb54d083a7d1d46"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7651510468:AAG_sEZ7LwyvyrbLfFtxgmhy95yhqIpUjcA"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://vc:aizen@cluster0.px9pzr2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1002070231017
LOG_GROUP_ID = -1002070231017
BOT_USERNAME = "aizenxprobot"
# Get this value from  on Telegram by /id
OWNER_ID = 6806897901

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/bokuwaaizen77/new.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/soul_x_network")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/soul_x_society")

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "100"))
# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = False

# Auto Gcast/Broadcast Handler, Write:- [On / Off] During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe"
)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "3")
)  # Remember to give value in Seconds

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "10")
)  # Remember to give value in Seconds

# Get your pyrogram v2 session from @VIP_STRING_ROBOT on Telegram
STRING1 = "BQGIFLcAAvZljJnP2zhyYNaFi0M9-80sbaZs_9CvUuidlEBEIdBtGpDR8nkpE_XNOgqFCkCzpQSl_MMrvk6LMFUl8BNnLRzdNLD2fWWYy-lk7jOpfQIzzEVp3EG5_qMbqznJ5ixlFfEN2lOovq_f1UCMIXISyUhwp9l6sox_mVe1fko-YYLGEPJKJ41sHiOsbjhXNW_583B4l9POQuH8zT0bTR01QdSgU0VnHi5vH2WUUWxP5RoW6j7u-XYcxgQ-JJ7CpKwfN-4Sb2Lmghr2WEw1Ad2e6SvnxiyBfrpUXpcndw9teb60e9WfmRuB_Vuxev7y52HrC-eIhiGAkUyE4QX_9AvvFAAAAABhHF7cAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

TEMP_FOLDER = "tempdb"
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/Amn.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/1845472a641e97ac614a4.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/1845472a641e97ac614a4.jpg"
STATS_IMG_URL = "https://telegra.ph/file/1845472a641e97ac614a4.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/1845472a641e97ac614a4.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/1845472a641e97ac614a4.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/1845472a641e97ac614a4.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/1845472a641e97ac614a4.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/1845472a641e97ac614a4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/1845472a641e97ac614a4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/1845472a641e97ac614a4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/1845472a641e97ac614a4.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
