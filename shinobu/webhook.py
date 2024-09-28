# Shinobu Webhook handler

from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for

from .functions import message
from .functions import media

webhook_bp = Blueprint("webhook", __name__, url_prefix="/webhook")

@webhook_bp.route("/", methods=["GET", "POST"])
def handler():
    if request.method == "GET":
        return redirect(url_for("webui.root"))

    data = request.json

    # Ignore empty data
    if not "message" in data["data"].keys():
        return "Skipping empty data."

    # Check if message is from me
    # If yes: Skip ahead
    if data["data"]["message"]["fromMe"]:
        return "Skipping unneeded data from bot."

    # Check if sent from group
    # Just check if the data has "author" field in it
    if "author" in data["data"].keys() and data["data"]["message"].get("author"):
        # TODO: We're not supporting group command for now
        return "Skipping commands from group."

    # Type: Message
    if data["dataType"] == "message":
        if not any([
            message.handle(data=data["data"]["message"])
        ]):
            return "Unhandled response; returning OK..."
        return "OK. Handled."
    
    # Type: Media
    elif data["dataType"] == "media":
        if not any([
            media.handle(media=data["data"]["messageMedia"], data=data["data"]["message"])
        ]):
            return "Unhandled response; returning OK..."
        return "OK. Handled."

    return "Unknown data type; returning OK..."
