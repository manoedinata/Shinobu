from ndrabot.functions.handlers import sticker

def handle(media: dict, data: dict):
    # Check if message is from me
    # If yes: Skip ahead
    if data.get("fromMe"):
        return True

    # Check if sent from group
    # Just check if the data has "author" field in it
    if data.get("author"):
        # TODO: We're not supporting group command for now
        return True

    # Parse retrieved data
    sender = data["from"]
    caption = data["body"]

    b64data = media["data"]
    mimetype = media["mimetype"]

    # Media to sticker
    sticker.image2sticker(b64data, mimetype, caption, sender)
