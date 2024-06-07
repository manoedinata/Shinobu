import requests

from ndrabot.config import WWEB_API_SENDMESSAGE_ENDPOINT

def send_message(number: str, text: str):
    req = requests.post(WWEB_API_SENDMESSAGE_ENDPOINT, json={
        "chatId": number,
        "contentType": "string",
        "content": text
    })
    if not req.ok:
        return False
    return True

def send_media(
    number: str,
    mime_type: str,
    base64data: str,
    filename: str,
    caption: str = "",
    as_sticker: bool = False,
    stickerName: str = "ndraBot's Media to Sticker",
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
            "stickerAuthor": "ndraBot",
            "stickerName": caption if caption else stickerName
        }
    })
    if not req.ok:
        return False

    return True

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
    if not req.ok:
        return False

    return True
