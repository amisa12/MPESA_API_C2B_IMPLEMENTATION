from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import config

db = SQLAlchemy()


def init_app(config_name):
    application = Flask(__name__)
    application.config.from_object(config[config_name])

    db.init_app(application)
    db.app = application

    return application