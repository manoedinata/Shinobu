from ndrabot.utils.messages import send_message
from ndrabot.utils.messages import send_media

def image2sticker(data, mimetype, caption, number):
    send_message(number, "Memproses stiker...")

    req = send_media(
        number,
        mimetype,
        data,
        "",
        as_sticker=True,
        stickerName=caption
    )
    return req
