from flask import Flask
from app.config import Config
from app.extensions import db, cors
from app.api.routes import health_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    cors.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(health_bp, url_prefix="/api/v1")

    return app
