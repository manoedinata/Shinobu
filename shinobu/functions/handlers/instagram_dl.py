from instaloader import Instaloader
from instaloader import Post
from instaloader.exceptions import ConnectionException
import re

from shinobu.utils.messages import send_message
from shinobu.utils.messages import send_media_from_url

from shinobu.config import INSTALOADER_SESSION_USERNAME
from shinobu.config import INSTALOADER_SESSION_BASE64

loader = Instaloader()
loader.load_session(INSTALOADER_SESSION_USERNAME, INSTALOADER_SESSION_BASE64)

def instagram_dl(link, number, message_id):
    send_message(
        number,
        "Memulai pengunduhan postingan, mohon menunggu...",
        reply=True, message_id=message_id
    )

    # Filter link to shortcode
    shortcode = re.search("^(?:.*\/p\/)([\d\w\-_]+)", link).group(1)

    try:
        post = Post.from_shortcode(loader.context, shortcode)
    except ConnectionException:
        send_message(
            number,
            "Gagal mendapatkan data. Mungkin bot " + \
            "terblokir Instagram. \n" + \
            "Coba nanti, ya.",
            reply=True, message_id=message_id
        )
        return False

    urls = []
    if post.typename == "GraphSidecar":
        for node in post.get_sidecar_nodes():
            urls.append(node.display_url)
    else:
        urls.append(post.url)

    for url in urls:
        req = send_media_from_url(
            number,
            url
        )
        if not req:
            return False

    caption = post.caption
    caption += "\n\n"
    caption += f"🔗 {link}"
    send_message(number, caption)

    return True
