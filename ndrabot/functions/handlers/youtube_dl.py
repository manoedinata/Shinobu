from pytube import YouTube

from ndrabot.config import NDRABOT_MAX_ATTACHMENT

from ndrabot.utils.messages import send_message
from ndrabot.utils.messages import send_media_from_url

def youtube_dl(link, number):
    send_message(number, "Mengambil metadata video...")

    yt = YouTube(link)
    title = yt.title
    caption = f"{title} | {link}"

    video = yt.streams.filter(progressive=True).get_highest_resolution()
    if not video:
        send_message(number, "Video tidak ditemukan! Cek kembali URL Anda.")
        return False

    # Limit file size
    if video.filesize_approx > NDRABOT_MAX_ATTACHMENT:
        send_message(
            number,
            "Maaf, video terlalu besar untuk diunduh. Coba video lain. \n" + \
            f"Batas ukuran video: {NDRABOT_MAX_ATTACHMENT // 1024000} MB.")
        return False

    send_message(number, "Memulai pengunduhan video, mohon menunggu...")

    # Get and directly send video URL
    url = video.url
    req = send_media_from_url(
        number,
        url,
        caption
    )
    if not req:
        send_message(number, "Gagal mengunduh video! Harap coba lagi.")
    return req
