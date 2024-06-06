from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    # Routes registration
    from .webhook import webhook_bp
    app.register_blueprint(webhook_bp)

    return app
