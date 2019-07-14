from enum import Enum
from functools import wraps
from typing import Type

from flask import request
from pydantic.main import BaseModel

from app.context import context_property


class PayloadLocation(Enum):
    ARGS = "args"
    JSON = "json"


def validate_with_pydantic(location: PayloadLocation, model: Type[BaseModel]):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            payload = getattr(request, location.value)
            if location is not PayloadLocation.JSON:
                payload = getattr(request, payload.to_dict())

            schema = model(**payload)

            context_property.request_payload = schema

            return fn(*args, **kwargs)

        return wrapper

    return decorator


