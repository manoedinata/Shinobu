from pytube import YouTube
from io import BytesIO
from base64 import b64encode

from ndrabot.config import NDRABOT_MAX_ATTACHMENT

from ndrabot.utils.messages import send_message
from ndrabot.utils.messages import send_video

def youtube_dl(link, number):
    yt = YouTube(link)
    title = yt.title
    caption = f"{title} | {link}"

    video = yt.streams.filter(progressive=True).get_highest_resolution()
    if not video:
        send_message(number, "Video tidak ditemukan!")
        return False

    # Limit file size
    if video.filesize_approx > NDRABOT_MAX_ATTACHMENT:
        send_message(
            number,
            "Maaf, video terlalu besar untuk diunduh. Coba video lain. \n" + \
            f"Batas ukuran video: {NDRABOT_MAX_ATTACHMENT // 1024000} MB.")
        return False

    send_message(number, "Memulai pengunduhan video...")

    # Temporary buffer to store video data
    # NOTE: If the video size is huge, we'll be damned.
    with BytesIO() as file:
        # Save video
        video.stream_to_buffer(file)
        file.seek(0)

        req = send_video(
            number,
            video.mime_type,
            b64encode(file.getvalue()).decode(),
            video.default_filename,
            caption
        )
        if not req:
            send_message(number, "Gagal mengunduh video! Harap coba lagi.")
        return req
