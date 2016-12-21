import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from braindump.models.user import AnonymousUser
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.anonymous_user = AnonymousUser
    login_manager.init_app(app)

    # Register Blueprints
    from braindump.controllers.dashboard import dashboard
    app.register_blueprint(dashboard)

    from braindump.controllers.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from braindump.controllers.notes import notes
    app.register_blueprint(notes, url_prefix='/notes')

    return app
