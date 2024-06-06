import requests

from ndrabot.config import WWEB_API_SENDMESSAGE_ENDPOINT

def unknown_command(number):
    print(" Unknown command ")
    req = requests.post("http://localhost:3000/client/sendMessage/ndrabot", json={
        "chatId": number,
        "contentType": "string",
        "content": "Maaf, perintah tidak dikenali. Mohon cek perintah Anda."
    })
    if not req.ok:
        return False
    return True

def send_hi(number):
    print(" Hellllooooo ")
    req = requests.post(WWEB_API_SENDMESSAGE_ENDPOINT, json={
        "chatId": number,
        "contentType": "string",
        "content": "Halo! Aku ndraBot, asisten pribadi Hendra Manudinata."
    })
    if not req.ok:
        return False
    return True