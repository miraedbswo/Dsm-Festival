from peewee import *

from app.models.base import BaseModel
from app.models.student import StudentTable


class RFIDTable(BaseModel):
    rfid = CharField(primary_key=True, max_length=16)
    student_id = ForeignKeyField(StudentTable, db_column='id', to_field='id')
    point = IntegerField(default=15)
    level = IntegerField()

    class Meta:
        table_name = 'rfid'

    @classmethod
    def get_my_rank(cls, user_id: str):
        my_rank = (
            RFIDTable
            .select()
            .join(StudentTable)
            .where(StudentTable.id == user_id)
            .get()
        )

        return my_rank

    @classmethod
    def get_top_10_rank(cls):
        top_10_rank = (
            RFIDTable
            .select()
            .join(StudentTable)
            .order_by(RFIDTable.point.desc())
            .limit(10)
            .get()
        )

        return top_10_rank

    @classmethod
    def get_by_rfid(cls, rfid: str):
        user = (
            RFIDTable
            .select()
            .join(StudentTable)
            .where(RFIDTable.rfid == rfid)
            .get()
        )

        return user


class UnsignedRFIDTable(BaseModel):
    id = IntegerField(primary_key=True)
    rfid = CharField(unique=True)

    class Meta:
        table_name = 'unsigned_rfid'
