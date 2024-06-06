import requests

from ndrabot.utils.messages import send_message

def get_quote(body, number):
    if body[0] != "/quote": return False

    req = requests.get("https://api.quotable.io/random").json()
    quote = ""
    quote += f"*{req['content']}*"
    quote += "\n\n"
    quote += f"─ {req['author']}"

    req = send_message(quote)
    return req
