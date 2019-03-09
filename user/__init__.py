import os

from flask import Flask

from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)
    app.app_context().push()
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from user.auth import auth_blueprint
    from user.users import users_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(auth_blueprint)
    db.create_all()



    return app

