from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:chickboyz@localhost:5432/ball_api'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    return app