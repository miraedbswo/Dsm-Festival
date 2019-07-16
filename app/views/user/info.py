from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.extension import db
from app.views.base import BaseResource
from app.models import RFIDTable, StudentTable


class GetInfoByToken(BaseResource):
    @jwt_required
    def get(self):
        me = RFIDTable.get_my_info()

        return {
            "number": me['number'],
            "name": me['name'],
            "point": me['point'],
        }, 200


class GetInfoByRFID(BaseResource):
    def get(self, rfid: str):
        me = RFIDTable.get_user_by_rfid(rfid)

        return jsonify({
            "number": me.number,
            "name": me.name,
            "point": me.point,
        }), 200
