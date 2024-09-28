# This file is only used when the app is deployed
# via WSGI. For local development, use:
#  $ flask run

from shinobu import create_app
from werkzeug.middleware.proxy_fix import ProxyFix

# Initialize app for Gunicorn
app = create_app()

# Middleware to correct some headers when proxy is used
# Ref: https://flask.palletsprojects.com/en/3.0.x/deploying/proxy_fix/
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)
