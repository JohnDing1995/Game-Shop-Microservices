import os

from flask import Flask

from flask_cors import CORS

from .models import db, bcrypt
from .config import Config




def create_app():

    # instantiate the app
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.DATABASE_URI
    # enable CORS
    CORS(app)
    app.app_context().push()
    db.init_app(app)
    bcrypt.init_app(app)

    from user.auth import auth_blueprint
    from user.users import users_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(auth_blueprint)
    db.create_all()



    return app

