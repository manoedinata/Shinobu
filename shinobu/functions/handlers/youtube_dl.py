from pytube import YouTube
from datetime import timedelta

from shinobu.config import MAX_ATTACHMENT

from shinobu.utils.messages import send_message
from shinobu.utils.messages import send_media_from_url

def youtube_dl(link, number):
    send_message(number, "Memulai pengunduhan video, mohon menunggu...")

    yt = YouTube(link)
    try:
        video = yt.streams.filter(progressive=True).get_highest_resolution()
        if not video:
            send_message(number, "Video tidak ditemukan! Cek kembali URL Anda.")
            return False
    except Exception as e:
        send_message(
            number,
            "Gagal mendapatkan informasi video! \n" + \
            f"*Alasan*: _{str(e)}_"
        )
        return False

    # Build caption
    caption = \
        f"*{yt.title}* \n" + \
        "\n" + \
        f"👥 Uploader: {yt.author} \n" + \
        f"🕛 Durasi: {timedelta(seconds=yt.length)} \n" + \
        f"🔗 Link: {yt.watch_url}"

    # Limit file size
    if video.filesize_approx > MAX_ATTACHMENT:
        send_message(
            number,
            "Maaf, video terlalu besar untuk diunduh. Coba video lain. \n" + \
            f"Batas ukuran video: {MAX_ATTACHMENT // 1024000} MB.")
        return False

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
