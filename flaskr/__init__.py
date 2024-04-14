from flask import Flask
from config import Config
from datetime import timedelta


def create_app(config_name):
    config = Config()
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=4)
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI']=config.DATA_BASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['PROPAGATE_EXCEPTIONS']=True
    return app

from .app import *