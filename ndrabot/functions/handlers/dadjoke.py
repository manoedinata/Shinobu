import requests

from ndrabot.utils.messages import send_message

def dad_joke(body, number):
    if body[0] not in ["/dadjoke", "/dadjokes"]: return False

    req = requests.get(
        "https://icanhazdadjoke.com",
        headers={"Accept": "application/json"}).json()

    joke = req['joke']

    req = send_message(number, joke)
    return req
