from shinobu.functions.handlers import defaults
from shinobu.functions.handlers import quotes
from shinobu.functions.handlers import dadjoke
from shinobu.functions.handlers import youtube_dl
from shinobu.functions.handlers import instagram_dl

from shinobu.utils.detect_website import detect_website

def handle(data: dict):
    # Check if it's just additional data after image
    # Check if it has `hasMedia` field
    if data.get("hasMedia"):
        return True

    # Parse retrieved data
    messageId = data["id"]["id"]
    sender = data["from"]
    message = data["body"].split()

    # Skip empty webhook data
    if len(message) < 1:
        return True

    # Handle video downloader
    website = detect_website(message[0])
    if website:
        # YouTube
        if website == "youtube":
            youtube_dl.youtube_dl(link=message[0], number=sender)
        elif website == "instagram":
            instagram_dl.instagram_dl(link=message[0], number=sender)
        else:
            return False

        return True

    # List of available commands
    if message[0].startswith("/"):
        if not any([
            # Quote
            quotes.get_quote(body=message, number=sender, message_id=messageId),
            # Dad joke
            dadjoke.dad_joke(body=message, number=sender, message_id=messageId)
        ]):
            # Command not found
            return defaults.unknown_command(number=sender, message_id=messageId)

        # Everything seems to be successfully handled
        return True

    # Make `send_hi()` function as the last resort.
    # In case the sent command from user isn't recognized: Say hi.
    defaults.send_hi(body="".join(message).strip(), number=sender)
