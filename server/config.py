from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

import os

db = SQLAlchemy()
jwt = JWTManager()

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "postgresql://george-benedict:12345@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or "super-secret"
