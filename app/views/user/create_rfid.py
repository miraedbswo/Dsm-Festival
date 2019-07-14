from pydantic import BaseModel

from app.decorators.json_schema import json_type_validate, RFID_POST_JSON
from app.views.base import BaseResource
from app.models import UnsignedRFIDTable
from app.context import context_property


class RFIDModel(BaseModel):
    rfid: str


class CreateRFID(BaseResource):
    @json_type_validate(RFID_POST_JSON)
    def post(self):
        payload = context_property.request_payload

        rfid = payload.get('rfid')

        UnsignedRFIDTable.insert(rfid=rfid).execute()

        return '', 201
