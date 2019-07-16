from peewee import *
from flask_jwt_extended import get_jwt_identity

from app.extension import db
from app.models.base import BaseModel, cursor_to_dict
from app.models.student import StudentTable


class RFIDTable(BaseModel):
    rfid = CharField(primary_key=True, max_length=16)
    student_id = ForeignKeyField(StudentTable, db_column='id', to_field='id')
    point = IntegerField(default=15)
    level = IntegerField()

    class Meta:
        table_name = 'rfid'

    @classmethod
    def get_my_info(cls):
        query = (
            RFIDTable
            .select(StudentTable.number, StudentTable.name, RFIDTable.point)
            .join(StudentTable)
            .where(StudentTable.id == get_jwt_identity())
        )
        cursor = db.execute_sql(str(query))
        rows = cursor_to_dict(cursor)

        return rows[0]

    @classmethod
    def get_my_rank(cls, user_id: str):
        query = (
            RFIDTable
            .select(RFIDTable, StudentTable)
            .join(StudentTable)
            .where(StudentTable.id == user_id)
            .get()
        )

        my_rank = db.execute(query)

        return my_rank

    @classmethod
    def get_top_10_rank(cls):
        query = (
            RFIDTable
            .select(RFIDTable, StudentTable)
            .join(StudentTable)
            .order_by(RFIDTable.point.desc())
            .limit(10)
        )

        top_10_rank = db.execute(query)

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
    rfid = CharField(unique=True)

    class Meta:
        table_name = 'unsigned_rfid'
