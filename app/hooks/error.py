from flask import jsonify
from werkzeug.exceptions import HTTPException


def http_exception_handler(e: HTTPException):
    return jsonify({'message': e.description}), e.code
