from flask import Flask
from flask_migrate import Migrate
from server.config import db, jwt, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, JWT_SECRET_KEY

# Import blueprints
from server.controllers.auth_controller import auth_bp
from server.controllers.guest_controller import guest_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.appearance_controller import appearance_bp

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

    db.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)

    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(guest_bp, url_prefix="/api")
    app.register_blueprint(episode_bp, url_prefix="/api")
    app.register_blueprint(appearance_bp, url_prefix="/api")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
