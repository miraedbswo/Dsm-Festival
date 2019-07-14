from flask import Response, abort
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.decorators.validate import PayloadLocation, validate_with_pydantic
from app.views.base import BaseResource
from app.models.student import StudentTable
from app.context import context_property


class Login(BaseResource):
    # @validate_with_pydantic(PayloadLocation.JSON, )
    def post(self):
        payload = context_property.request_payload

        id = payload.id
        pw = payload.pw

        user = StudentTable.get_or_none(id=id)
        if user is None or check_password_hash(user.pw, pw):
            abort(401)

        return Response({
            "accessToken": create_access_token(user.id)
        }, 200)
