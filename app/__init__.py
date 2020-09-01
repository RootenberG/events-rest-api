import os

from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.exceptions import HTTPException

# instantiate extensions
login_manager = LoginManager()
db = SQLAlchemy()


def create_app(environment="development"):

    from config import config
    from .views import Info
    from .views import Tmimeline

    # Instantiate app.
    app = Flask(__name__)
    api = Api(app)
    # Set app config.
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    config[env].configure(app)

    # Set up extensions.
    db.init_app(app)
    login_manager.init_app(app)

    # Register resources
    api.add_resource(Info, "/api/info")
    api.add_resource(Tmimeline, "/api/timeline")

    return app
