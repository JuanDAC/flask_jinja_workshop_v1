
from flask import Flask

from app.views import app_views

from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(app_views)
    return app
