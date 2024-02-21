from secrets import token_urlsafe

from argon2 import PasswordHasher
from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()
password_hasher = PasswordHasher()


def create_app():
    app = Flask(__name__)
    app.secret_key = token_urlsafe(32)  # TODO: extract into config file
    login_manager.init_app(app)

    return app
