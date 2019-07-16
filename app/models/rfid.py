from typing import Any, Dict, List

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
    def get_info_by_token(cls, user_id: str) -> Dict[str, Any]:
        query = (
            RFIDTable
            .select(StudentTable.number, StudentTable.name, RFIDTable.point)
            .join(StudentTable)
            .where(StudentTable.id == user_id)
        )
        cursor = db.execute_sql(str(query))
        rows = cursor_to_dict(cursor)

        return rows[0]

    @classmethod
    def get_info_by_rfid(cls, rfid: str) -> Dict[str, Any]:
        query = (
            RFIDTable
            .select(StudentTable.number, StudentTable.name, RFIDTable.point)
            .join(StudentTable)
            .where(RFIDTable.rfid == rfid)
        )
        cursor = db.execute_sql(str(query))
        rows = cursor_to_dict(cursor)

        return rows[0]

    @classmethod
    def get_top_10_rank(cls) -> List[Dict[str, Any]]:
        query = (
            RFIDTable
            .select(RFIDTable.point, StudentTable.name)
            .join(StudentTable)
            .order_by(RFIDTable.point.desc())
            .limit(10)
        )
        cursor = db.execute_sql(str(query))
        rows = cursor_to_dict(cursor)

        return rows


class UnsignedRFIDTable(BaseModel):
    rfid = CharField(unique=True)

    class Meta:
        table_name = 'unsigned_rfid'
