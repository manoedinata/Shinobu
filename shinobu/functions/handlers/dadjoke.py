import requests

from shinobu.utils.messages import send_message

def dad_joke(body, number, message_id):
    if body[0] not in ["/dadjoke", "/dadjokes"]: return False

    req = requests.get(
        "https://icanhazdadjoke.com",
        headers={"Accept": "application/json"}).json()

    joke = req['joke']

    req = send_message(number, joke, reply=True, message_id=message_id)
    return req
