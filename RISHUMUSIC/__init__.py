from RISHUMUSIC.core.bot import RISHU
from RISHUMUSIC.core.dir import dirr
from RISHUMUSIC.core.git import git
from RISHUMUSIC.core.userbot import Userbot
from RISHUMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = RISHU()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "Vip_music_vc_bot"  # connect music api key "Dont change it"