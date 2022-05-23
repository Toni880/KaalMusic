#𝐊𝐚𝐚𝐥𝐔𝐬𝐞𝐫𝐁𝐨𝐭
import re
import os
import aiohttp
import asyncio
import logging
import requests
from os import getenv
from pyrogram.types import *
from datetime import datetime
from dotenv import load_dotenv
from pyrogram import Client, filters, idle
from apscheduler.schedulers.asyncio import AsyncIOScheduler


    
if os.path.exists("local.env"):
    load_dotenv("local.env")
    
que = {}
admins = {}
CMD_HELP = {}
START_TIME = datetime.now()
scheduler = AsyncIOScheduler()
aiohttpsession = aiohttp.ClientSession()
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/1d6f55f754c0ad3b69048.jpg")
API_ID = int(getenv("API_ID", "12380656"))
API_HASH = getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273")
DATABASE_URL = getenv("DATABASE_URL", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
LOGS_GROUP_ID = getenv("LOGS_GROUP_ID", "")
MONGO_DB_URL = getenv("MONGO_DB_URL", "")
STRING_SESSION = getenv("STRING_SESSION", "session")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5356564375").split()))

if LOGS_GROUP_ID:
    Owner = LOGS_GROUP_ID
else:
    Owner = 777000