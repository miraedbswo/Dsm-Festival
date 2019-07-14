from peewee import *

from app.models.base import BaseModel
from app.models.student import StudentTable


class RFIDTable(BaseModel):
    rfid = CharField(primary_key=True, max_length=16)
    student_id = ForeignKeyField(StudentTable, db_column='id', to_field='id')
    point = IntegerField(default=15)

    class Meta:
        table_name = 'rfid'


class UnsignedRFIDTable(BaseModel):
    rfid = CharField(primary_key=True)

    class Meta:
        table_name = 'unsigned_rfid'