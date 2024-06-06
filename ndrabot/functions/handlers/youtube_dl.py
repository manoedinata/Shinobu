import requests
from pytube import YouTube
from io import BytesIO
from base64 import b64encode

from ndrabot.config import WWEB_API_SENDMESSAGE_ENDPOINT

def youtube_dl(link, number):
    yt = YouTube(link)
    title = yt.title
    b64data = "" # This will contain large Base64 data depending on the video

    video = yt.streams.filter(progressive=True).get_highest_resolution()
    if not video:
        print("No video stream found")
        return False

    # Temporary buffer to store video data
    # NOTE: If the video size is huge, we'll be damned.
    with BytesIO() as file:
        # Save video
        video.stream_to_buffer(file)
        file.seek(0)
        b64data = b64encode(file.getvalue()).decode()

    req = requests.post(WWEB_API_SENDMESSAGE_ENDPOINT, json={
        "chatId": number,
        "contentType": "MessageMedia",
        "content": {
            "mimetype": video.mime_type,
            "data": b64data,
            "filename": video.default_filename
        },
        "options": {
            "caption": f"{title} | {link}"
        }
    })
    if not req.ok:
        return False

    return True
