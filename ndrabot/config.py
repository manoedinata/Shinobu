from os import environ 
from dotenv import load_dotenv
from base64 import b64decode
from ast import literal_eval

if not environ.get("ENV"):
    # Load dotenv if not using environment variable
    load_dotenv(".env")

# WhatsApp-Web API
WWEB_API_URL = environ.get("WWEB_API_URL")
WWEB_API_SESSION_NAME = environ.get("WWEB_API_SESSION_NAME")
WWEB_API_SENDMESSAGE_ENDPOINT = f"{WWEB_API_URL}/client/sendMessage/{WWEB_API_SESSION_NAME}"

# ndraBot
NDRABOT_MAX_ATTACHMENT = int(environ.get("NDRABOT_MAX_ATTACHMENT"))

# Instaloader
INSTALOADER_SESSION_USERNAME = environ.get("INSTALOADER_SESSION_USERNAME")
INSTALOADER_SESSION_BASE64 = literal_eval(
    b64decode(environ.get("INSTALOADER_SESSION_BASE64")).decode()
)
