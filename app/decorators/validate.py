from enum import Enum
from functools import wraps
from typing import Type

from flask import request
from pydantic.main import MetaModel

from app.context import context_property


class PayloadLocation(Enum):
    ARGS = "args"
    JSON = "json"


def validate_with_pydantic(payload_location: PayloadLocation, model: Type[MetaModel]):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            payload = getattr(request, payload_location.value)
            if payload_location is not PayloadLocation.JSON:
                payload = getattr(request, payload.to_dict())

            schema = model(**payload)

            context_property.request_payload = schema

            return fn(*args, **kwargs)

        return wrapper

    return decorator


