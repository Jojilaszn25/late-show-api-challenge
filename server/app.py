from flask import Flask
from server.config import db, jwt, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, JWT_SECRET_KEY
from flask_migrate import Migrate
from server.models import *

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

    db.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)

    from server.controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    return app

app = create_app()
