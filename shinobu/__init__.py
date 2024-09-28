from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "ohgituokedeh"

    # Routes registration
    ## Web UI
    from .webui import webui_bp
    app.register_blueprint(webui_bp)
    ## Webhook
    from .webhook import webhook_bp
    app.register_blueprint(webhook_bp)

    return app
