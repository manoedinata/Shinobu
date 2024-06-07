from instaloader import Instaloader
from instaloader import Post
from instaloader.exceptions import ConnectionException
import re

from ndrabot.utils.messages import send_message
from ndrabot.utils.messages import send_media_from_url

from ndrabot.config import INSTALOADER_SESSION_USERNAME
from ndrabot.config import INSTALOADER_SESSION_BASE64

loader = Instaloader()
loader.load_session(INSTALOADER_SESSION_USERNAME, INSTALOADER_SESSION_BASE64)

def instagram_dl(link, number):
    send_message(number, "Memulai pengunduhan postingan, mohon menunggu...")

    # Filter link to shortcode
    shortcode = re.search("^(?:.*\/p\/)([\d\w\-_]+)", link).group(1)

    try:
        post = Post.from_shortcode(loader.context, shortcode)
    except ConnectionException:
        send_message(
            number,
            "Gagal mendapatkan data. Mungkin bot " + \
            "terblokir Instagram. \n" + \
            "Coba nanti, ya."
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
    return True
