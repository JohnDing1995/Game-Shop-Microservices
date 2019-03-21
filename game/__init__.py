
from flask import Flask
from .gameModel import db
from .gameAPI import api

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    api.init_app(app)
    return app
