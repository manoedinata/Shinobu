# Shinobu Web UI handler

from flask import Blueprint
from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for

import requests
from .config import WWEB_API_URL
from .config import WWEB_API_SESSION_NAME

webui_bp = Blueprint("webui", __name__, url_prefix="/")

@webui_bp.route("/", methods=["GET"])
def root():
    connected = []
    qr = ""
    sessionInfo = ""

    status = requests.get(WWEB_API_URL + f"/session/status/{WWEB_API_SESSION_NAME}").json()
    if status["success"]:
        connected = [True, ""]
        sessionInfo = requests.get(WWEB_API_URL + f"/client/getClassInfo/{WWEB_API_SESSION_NAME}").json()["sessionInfo"]
    else:
        if "message" in status.keys():
            connected = [False, status["message"]]
        else:
            connected = [False, status["error"]]

        # Get QR
        qr = requests.get(WWEB_API_URL + f"/session/qr/{WWEB_API_SESSION_NAME}").json()
        if qr["success"]: qr = qr["qr"] # Show QR only when ready, else keep `qr` empty

    return render_template("home.html", connected=connected, qr=qr, sessionInfo=sessionInfo)

@webui_bp.route("/start", methods=["POST"])
def start():
    stop = requests.get(WWEB_API_URL + f"/session/start/{WWEB_API_SESSION_NAME}")
    if stop.json()["success"]:
        flash("Sukses memulai sesi", "success")
    else:
        flash(f"Gagal memulai sesi. Alasan: {stop['json']['error']}", "danger")

    return redirect(url_for("webui.root"))

@webui_bp.route("/stop", methods=["POST"])
def stop():
    stop = requests.get(WWEB_API_URL + f"/session/terminate/{WWEB_API_SESSION_NAME}")
    if stop.ok:
        flash("Sukses logout", "success")
    else:
        flash(f"Gagal logout. Alasan: {stop['json']['error']}", "danger")

    return redirect(url_for("webui.root"))
