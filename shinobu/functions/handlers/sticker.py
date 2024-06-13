from shinobu.utils.messages import send_message
from shinobu.utils.messages import send_media

def image2sticker(data, mimetype, caption, number, message_id):
    send_message(number, "Memproses stiker...", reply=True, message_id=message_id)

    req = send_media(
        number,
        mimetype,
        data,
        "",
        as_sticker=True,
        stickerName=caption,
        reply=True,
        message_id=message_id
    )
    return req
