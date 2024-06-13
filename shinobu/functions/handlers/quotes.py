import requests

from shinobu.utils.messages import send_message

def get_quote(body, number, message_id):
    if body[0] != "/quote": return False

    req = requests.get("https://api.quotable.io/random").json()
    quote = ""
    quote += f"*{req['content']}*"
    quote += "\n\n"
    quote += f"─ {req['author']}"

    req = send_message(number, quote, reply=True, message_id=message_id)
    return req
