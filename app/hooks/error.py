from werkzeug.exceptions import HTTPException


def http_exception_handler(e: HTTPException):
    return {'message': e.description}, e.code
