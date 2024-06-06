from pytube import YouTube
from io import BytesIO
from base64 import b64encode

from ndrabot.utils.messages import send_video

def youtube_dl(link, number):
    yt = YouTube(link)
    title = yt.title
    caption = f"{title} | {link}"
    b64data = "" # This will contain large Base64 data depending on the video

    video = yt.streams.filter(progressive=True).get_highest_resolution()
    if not video:
        return False

    # Temporary buffer to store video data
    # NOTE: If the video size is huge, we'll be damned.
    with BytesIO() as file:
        # Save video
        video.stream_to_buffer(file)
        file.seek(0)
        b64data = b64encode(file.getvalue()).decode()

    req = send_video(number, video.mime_type, b64data, video.default_filename, caption)
    return req
