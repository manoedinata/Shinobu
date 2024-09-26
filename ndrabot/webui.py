# ndraBot Web UI handler

from flask import Blueprint

webui_bp = Blueprint("webui", __name__, url_prefix="/")

@webui_bp.route("/", methods=["GET"])
def root():
    return "Hello, World!"