import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]:
        return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Request Channels
REQ_CHANNEL = int(environ.get('REQ_CHANNEL', ''))

# Bot information
PORT = environ.get("PORT", "8080")
WEBHOOK = bool(environ.get("WEBHOOK", True)) # for web support on/off
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/94e78692fd52dd7e68f9a.jpg https://telegra.ph/file/429c046ad75849d176855.jpg https://telegra.ph/file/ce431bb20e91f63057b7c.jpg https://telegra.ph/file/9891096fe2728cb6768ed.jpg https://telegra.ph/file/81d9c1f107134fc5eeda1.jpg https://telegra.ph/file/9b007ddffb5de56ada1cb.jpg https://telegra.ph/file/b697394f3c02a6e4b7862.jpg https://telegra.ph/file/1ab25364a80a1203a3d46.jpg https://telegra.ph/file/5b12e431f2f3553ce5d34.jpg https://telegra.ph/file/48ef3b1d6d9479f08f43f.jpg https://telegra.ph/file/e775e81da48d0bfd8e58d.jpg https://telegra.ph/file/39cc4895f385cd35a8b3e.jpg')).split()
BOT_START_TIME = time()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = ''
DATABASE_NAME = 'Cluster0'
COLLECTION_NAME = 'Media_Files'

# maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get(
    'START_MESSAGE', '👋 Hᴇʟʟᴏ {user}\n\nMʏ Nᴀᴍᴇ Is {bot},\n I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs, Jᴜsᴛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Eɴᴊᴏʏ 😍')
BUTTON_LOCK_TEXT = environ.get(
    "BUTTON_LOCK_TEXT", "⚠️ 𝙃𝙚𝙮 {query}! 𝙏𝙝𝙖𝙩'𝙨 𝙉𝙤𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', "**Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ ᴏᴜʀ Bᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ sᴏ ʏᴏᴜ ᴅᴏɴ'ᴛ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ғɪʟᴇ...\n\nIғ ʏᴏᴜ ᴡᴀɴᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ғɪʟᴇ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ '❆ Jᴏɪɴ Oᴜʀ Bᴀᴄᴋ-Uᴘ Cʜᴀɴɴᴇʟ ❆' ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴀɴᴅ ᴊᴏɪɴ ᴏᴜʀ ʙᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ '↻ Tʀʏ Aɢᴀɪɴ' ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ...\n\nTʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ғɪʟᴇs...**")
RemoveBG_API = environ.get("RemoveBG_API", "")
WELCOM_PIC = environ.get("WELCOM_PIC", "https://telegra.ph/file/0e16dbbaca78bf117e21e.mp4")
WELCOM_TEXT = environ.get(
    "WELCOM_TEXT", "Hᴇʟʟᴏ {user} 😍,\nAɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {chat} Gʀᴏᴜᴘ ❤️")
PMFILTER = environ.get('PMFILTER', "True")
G_FILTER = bool(environ.get("G_FILTER", True))
BUTTON_LOCK = environ.get("BUTTON_LOCK", "True")

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', "-1001971176803"))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Kdramaland_Official')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
PM_IMDB = environ.get('PM_IMDB', "True")
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get(
    "CUSTOM_FILE_CAPTION", "`{file_name}`\n\n🔘 SIZE - `{file_size}`\n\n➠ 𝗝𝗼𝗶𝗻 : [R͏O͏O͏F͏T͏O͏P͏](https://t.me/+mCdsJ7mjeBEyZWQ1)")
BATCH_FILE_CAPTION = environ.get(
    "BATCH_FILE_CAPTION", "<b>{file_name}</b>\n\n🔘 SIZE - `{file_size}`\n\n➠ 𝗝𝗼𝗶𝗻 : [R͏O͏O͏F͏T͏O͏P͏](https://t.me/+mCdsJ7mjeBEyZWQ1)")
IMDB_TEMPLATE = environ.get(
    "IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10\n\n★ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [R͏O͏O͏F͏T͏O͏P͏](https://t.me/+yYhfz5JwILhmODc9)")
LONG_IMDB_DESCRIPTION = is_enabled(
    environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get(
    'FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled(
    (environ.get('PUBLIC_FILE_STORE', "True")), True)

# request force sub
REQ_SUB = bool(environ.get("REQ_SUB", True))
SESSION_STRING = environ.get("SESSION_STRING", "")
