from flask import Response

from app.decorators.json_schema import json_type_validate, PAY_POST_JSON
from app.views.base import BaseResource
from app.models.rfid import RFIDTable
from app.context import context_property


class Pay(BaseResource):
    @json_type_validate(PAY_POST_JSON)
    def post(self):
        """
        이상한 rfid 값이면 401
        json으로 받은 point 값을 적용했을 때 0 이하인 경우 403
        history에 이미 같은 부스 id로 찍혀있는 경우 409

        rfid level이 1이면 돈 무제한
        """
        payload = context_property.request_payload

        rfid = payload.get('rfid')
        booth_id = payload.get('boothId')
        point = payload.get('point')

        RFIDTable.pay(rfid, booth_id, point)

        return Response('', 201)

