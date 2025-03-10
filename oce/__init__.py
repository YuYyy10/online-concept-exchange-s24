from secrets import token_urlsafe

from argon2 import PasswordHasher
from flask import Flask
from flask_dance.contrib.github import make_github_blueprint, github
from flask_login import LoginManager


login_manager = LoginManager()
password_hasher = PasswordHasher()


def create_app():
    app = Flask(__name__)
    app.config['DB_NAME'] = 'oce.db'  # TODO: extract into config file
    app.secret_key = token_urlsafe(32)  # TODO: extract into config file
    login_manager.init_app(app)

    #Github OAuth config
    github_blueprint = make_github_blueprint(
        client_id="Ov23liIJBChlsCtbBCeT",
        client_secret="39ab2349a7ca34127ada968fb6ad89ff679e8c2c"
        # redirect_to = 'github_login'
    )
    app.register_blueprint(github_blueprint, url_prefix="/github_login")

    from oce.accounts.routes import accounts
    from oce.content.routes import content
    from oce.errors.handlers import errors
    from oce.forum.routes import forum

    app.register_blueprint(accounts)
    app.register_blueprint(content)
    app.register_blueprint(errors)
    app.register_blueprint(forum)

    return app
