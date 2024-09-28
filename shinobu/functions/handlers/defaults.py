from shinobu.utils.messages import send_message

def unknown_command(number, message_id):
    req = send_message(
        number,
        "Maaf, perintah tidak dikenali. Mohon cek perintah Anda.",
        reply=True, message_id=message_id
    )
    return req

def send_hi(body: str, number: str):
    if body.lower() in ["p", "halo", "hai"]:
        req = send_message(
            number,
            "Halo! 👋 \n" + \
            "Aku *Shinobu*, asisten pribadi buatan Hendra Manudinata."
        )
        return req
