from functools import wraps

from flask import request

from app.context import context_property
from app.exception import BadRequestException


def json_type_validate(json_schema: dict):
    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            json: dict = request.json
            if not json:
                raise BadRequestException()

            for key, type_ in json_schema.items():
                value = json.get(key)
                if type(value) is not type_:
                    break
            else:
                context_property.request_payload = json
                return fn(*args, **kwargs)
            raise BadRequestException()

        return wrapper

    return decorator


RFID_POST_JSON = dict(rfid=str)
LOGIN_POST_JSON = dict(id=str, pw=str)
PAY_POST_JSON = dict(rfid=str, boothId=int, point=int)
