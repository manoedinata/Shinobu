from ndrabot.functions.handlers import defaults
from ndrabot.functions.handlers import quotes
from ndrabot.functions.handlers import dadjoke
from ndrabot.functions.handlers import youtube_dl

from ndrabot.utils.detect_website import detect_website

def handle(data: dict):
    # Check if message is from me
    # If yes: Skip ahead
    if data.get("fromMe"):
        return True

    # Check if sent from group
    # Just check if the data has "author" field in it
    if data.get("author"):
        # TODO: We're not supporting group command for now
        return True

    # Parse retrieved data
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
        else:
            return False

        return True

    # List of available commands
    if message[0].startswith("/"):
        if not any([
            # Quote
            quotes.get_quote(body=message, number=sender),
            # Dad joke
            dadjoke.dad_joke(body=message, number=sender)
        ]):
            # Command not found
            return defaults.unknown_command(number=sender)

        # Everything seems to be successfully handled
        return True

    # Make `send_hi()` function as the last resort.
    # In case the sent command from user isn't recognized: Say hi.
    defaults.send_hi(number=sender)
