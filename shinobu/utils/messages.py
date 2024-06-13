from typing import Optional

import requests

from shinobu.config import WWEB_API_SENDMESSAGE_ENDPOINT
from shinobu.config import WWEB_API_REPLYMESSAGE_ENDPOINT

def send_message(number: str, text: str, reply: Optional[bool] = False, message_id: Optional[str] = ""):
    if reply:
        req = requests.post(WWEB_API_REPLYMESSAGE_ENDPOINT, json={
            "chatId": number,
            "messageId": message_id,
            "content": text
        })
    else:
        req = requests.post(WWEB_API_SENDMESSAGE_ENDPOINT, json={
            "chatId": number,
            "contentType": "string",
            "content": text
        })
    return req.ok

def send_media(
    number: str,
    mime_type: str,
    base64data: str,
    filename: str,
    caption: str = "",
    as_sticker: bool = False,
    stickerName: str = "Shinobu's Media to Sticker",
    ):
    req = requests.post(WWEB_API_SENDMESSAGE_ENDPOINT, json={
        "chatId": number,
        "contentType": "MessageMedia",
        "content": {
            "mimetype": mime_type,
            "data": base64data,
            "filename": filename
        },
        "options": {
            "caption": caption,
            "sendMediaAsSticker": as_sticker,
            "stickerAuthor": "Shinobu",
            "stickerName": caption if caption else stickerName
        }
    })
    return req.ok

def send_media_from_url (
    number: str,
    url: str,
    caption: str = "",
    ):
    req = requests.post(WWEB_API_SENDMESSAGE_ENDPOINT, json={
        "chatId": number,
        "contentType": "MessageMediaFromURL",
        "content": url,
        "options": {
            "caption": caption
        }
    })
    return req.ok
