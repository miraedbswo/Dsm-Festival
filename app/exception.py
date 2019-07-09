from werkzeug.exceptions import HTTPException


class BadRequestException(HTTPException):
    code = 400
    description = 'Bad Parameter Request'


class WrongAuthException(HTTPException):
    code = 401
    description = 'Wrong Auth'
