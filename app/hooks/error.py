from werkzeug.exceptions import HTTPException


def http_exception_handler(e: HTTPException):
    return e.description, e.code
