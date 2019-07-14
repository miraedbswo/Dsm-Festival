from peewee import *

from app.models.base import BaseModel
from app.models import BoothTable, RFIDTable


class HistoryTable(BaseModel):
    rfid = ForeignKeyField(RFIDTable, db_column='rfid', to_field='rfid')
    used_booth = ForeignKeyField(BoothTable, db_column='used_booth', to_field='booth_name')
    point = IntegerField()

    class Meta:
        table_name = 'history'
