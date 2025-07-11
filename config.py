import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "12565317"))
API_HASH = getenv("API_HASH", "de3e1a800e0ebdff1031232be6c38814")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7597057529:AAGwyMbRaXPxtnZtMDcv1n8Emae4dmoiYfQ")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","ll_KUZE_lll")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","SNOWY_x_musicbot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME", "snowy x music")
# ---------------------------------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002825379503))

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7926944005))


## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Gxinfinity/ANYA_MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/dark_x_knight_musiczz_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/dark_knight_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQC_u0UANv5SpgxrjB49Jly8owhGFeIKeWLqnLMAkb2rpsk38cFiByuADys3nfwYE5IMBOj-q1k5yE_wAHafIZDuR2hsLs9g5IxVxVgn7lzb-nIBYan95jbZxq49auQhwGnzqRNvToIL7Ioxy_Abf78ZEhryFb6bK2fnlgB6rXjyZ703lG3e-2CKlHDfkOXlc9-v_iI5JJbUe-GHErhZkQYwnA7gJMlbF2xIVsfYvfWrO9m5LepfbohaFF6Lsz0Ms4rK2k0uIqappdm07jroAuIQw3EJUM8VXnowTtf5st5ZjrH0eaPAa3k1UWYiJRZRrqM7x4Rq34yg0BH4KxLz3Cfk1ux-pAAAAAHlOtF5AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/6165bc89f53da9846f83b-61cca9647e63e5f7da.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/6165bc89f53da9846f83b-61cca9647e63e5f7da.jpg "
)
PLAYLIST_IMG_URL = "https://graph.org/file/6165bc89f53da9846f83b-61cca9647e63e5f7da.jpg"
STATS_IMG_URL = "https://graph.org/file/6165bc89f53da9846f83b-61cca9647e63e5f7da.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/6165bc89f53da9846f83b-61cca9647e63e5f7da.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/6165bc89f53da9846f83b-61cca9647e63e5f7da.jpg"
STREAM_IMG_URL = "https://graph.org/file/6165bc89f53da9846f83b-61cca9647e63e5f7da.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/6165bc89f53da9846f83b-61cca9647e63e5f7da.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/6165bc89f53da9846f83b-61cca9647e63e5f7da.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/6165bc89f53da9846f83b-61cca9647e63e5f7da.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/6165bc89f53da9846f83b-61cca9647e63e5f7da.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/6165bc89f53da9846f83b-61cca9647e63e5f7da.jpg"


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
