from flask import Response
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.decorators.json_schema import json_type_validate, LOGIN_POST_JSON
from app.exception import WrongAuthException
from app.views.base import BaseResource
from app.models.student import StudentTable
from app.context import context_property


class Login(BaseResource):
    @json_type_validate(LOGIN_POST_JSON)
    def post(self):
        payload = context_property.request_payload

        id = payload.get('id')
        pw = payload.get('pw')

        user = StudentTable.get_or_none(id=id)
        if user is None or check_password_hash(user.pw, pw):
            raise WrongAuthException()

        return Response({
            "accessToken": create_access_token(user.id)
        }, 200)
