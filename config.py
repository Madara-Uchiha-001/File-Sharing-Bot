#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20825278"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fa30f58d01b5b03b3e51cd917b5ebfe8")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002214630123"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7144504368"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002152311495"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "2"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello There! {mention}\n\nWelcome to My Premium Bot")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7144504368 5745818770").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Please verify yourself as human by joining the channel below 🤖⬇️")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "💀 WHY IN THE WORLD WILL YOU MESSAGE ME?? I'M JUST A FILE SHARE BOT 🤫"

ADMINS.append(OWNER_ID)
ADMINS.append(7144504368)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
