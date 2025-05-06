import os
from flask import Flask
from .extensions import db
from .routes import main
from config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.register_blueprint(main)

    return app