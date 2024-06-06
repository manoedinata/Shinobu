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

def send_video(number: str, mime_type: str, base64data: str, filename: str, caption: str):
    req = requests.post(WWEB_API_SENDMESSAGE_ENDPOINT, json={
        "chatId": number,
        "contentType": "MessageMedia",
        "content": {
            "mimetype": mime_type,
            "data": base64data,
            "filename": filename
        },
        "options": {
            "caption": caption
        }
    })
    if not req.ok:
        return False

    return True
