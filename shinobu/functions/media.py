from shinobu.functions.handlers import sticker

def handle(media: dict, data: dict):
    # Parse retrieved data
    messageId = data["id"]["id"]
    sender = data["from"]
    caption = data["body"]

    b64data = media["data"]
    mimetype = media["mimetype"]

    # Media to sticker
    sticker.image2sticker(b64data, mimetype, caption, sender, messageId)
