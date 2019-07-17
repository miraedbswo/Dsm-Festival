import json

from flask import Response
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.views.base import BaseResource
from app.models import RFIDTable


class GetInfoByToken(BaseResource):
    @jwt_required
    def get(self):
        me = RFIDTable.get_info_by_token(user_id=get_jwt_identity())

        return {
            "number": me['number'],
            "name": me['name'],
            "point": me['point'],
        }, 200


class GetInfoByRFID(BaseResource):
    def get(self, rfid: str):
        me = RFIDTable.get_info_by_rfid(rfid)

        number = me.get('number')
        name = me.get('name')
        point = me.get('point')

        return Response(f'{number},{name},{point}', 200)
