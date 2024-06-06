import requests

from ndrabot.config import WWEB_API_SENDMESSAGE_ENDPOINT

def get_quote(body, number):
    if body[0] != "/quote": return False

    req = requests.get("https://api.quotable.io/random").json()
    quote = ""
    quote += f"*{req['content']}*"
    quote += "\n\n"
    quote += f"─ {req['author']}"

    req = requests.post(WWEB_API_SENDMESSAGE_ENDPOINT, json={
        "chatId": number,
        "contentType": "string",
        "content": quote
    })
    if not req.ok:
        return False
    return True