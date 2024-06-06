import requests

from ndrabot.config import WWEB_API_SENDMESSAGE_ENDPOINT

def dad_joke(body, number):
    if body[0] not in ["/dadjoke", "/dadjokes"]: return False

    print(" DAD JOKES ")
    req = requests.get(
        "https://icanhazdadjoke.com",
        headers={"Accept": "application/json"}).json()

    joke = req['joke']
    # joke = ""
    # joke += req['joke']
    # joke += "\n\n"
    # joke += f"Source: https://icanhazdadjoke.com/j/{req['id']}"

    req = requests.post(WWEB_API_SENDMESSAGE_ENDPOINT, json={
        "chatId": number,
        "contentType": "string",
        "content": joke
    })
    if not req.ok:
        return False
    return True