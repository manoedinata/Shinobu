import requests

def get_quote(body, number):
    if body[0] != "/quote": return False

    print(" QUOTES ")
    req = requests.get("https://api.quotable.io/random").json()
    quote = ""
    quote += f"*{req['content']}*"
    quote += "\n\n"
    quote += f"─ {req['author']}"

    req = requests.post("http://localhost:3000/client/sendMessage/ndrabot", json={
        "chatId": number,
        "contentType": "string",
        "content": quote
    })
    if not req.ok:
        return False
    return True