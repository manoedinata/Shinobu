from ndrabot.utils.messages import send_message

def unknown_command(number):
    req = send_message(number, "Maaf, perintah tidak dikenali. Mohon cek perintah Anda.")
    return req

def send_hi(number):
    req = send_message(
        number,
        "Halo! 👋 \n" + \
        "Aku *ndraBot*, asisten pribadi buatan Hendra Manudinata."
    )
    return req
