from werkzeug.exceptions import HTTPException

from flask import Flask, jsonify
from jwt.exceptions import PyJWTError
from flask_jwt_extended.exceptions import JWTExtendedException
from peewee import MySQLDatabase


def register_extension(flask_app: Flask):
    from app import extension
    extension.db = MySQLDatabase(**flask_app.config['DB_SETTING'])
    extension.jwt.init_app(flask_app)
    extension.jwt.invalid_token_loader(wrong_token_handler)
    extension.jwt.expired_token_loader(wrong_token_handler)
    extension.cors.init_app(flask_app)


def register_hooks(flask_app: Flask):
    from app import exception
    from app.hooks.error import http_exception_handler

    flask_app.register_error_handler(HTTPException, http_exception_handler)
    flask_app.register_error_handler(JWTExtendedException, jwt_handle)
    flask_app.register_error_handler(PyJWTError, jwt_handle)


def register_views(flask_app: Flask):
    # from app.views.account import account_blueprint
    # flask_app.register_blueprint(account_blueprint)
    pass


def create_app(*config_cls) -> Flask:
    flask_app = Flask(__name__)
    for config in config_cls:
        flask_app.config.from_object(config)

    register_extension(flask_app)
    register_hooks(flask_app)
    register_views(flask_app)

    return flask_app


def wrong_token_handler(wrong_token: str):
    return jsonify({
        'status': 403,
        'sub_status': 42,
        'msg': 'Wrong Token'
    }), 403


def jwt_handle(e: Exception):
    return str(e), 403
