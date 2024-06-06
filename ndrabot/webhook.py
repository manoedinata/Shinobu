# ndraBot Webhook handler

from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for

import json

from .functions import message

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.get("/")
def root():
    return "Halo, dunia!"

@webhook_bp.route("/webhook", methods=["GET", "POST"])
def handler():
    if request.method == "GET":
        return redirect(url_for("webhook.root"))

    data = request.json
    # print(json.dumps(data, indent=4))

    # Type: Message
    if data["dataType"] == "message":
        if not any([
            message.handle(data=data["data"]["message"])
        ]):
            return "Unhandled response; returning OK..."
    
    return "Unknown data type; returning OK..."
