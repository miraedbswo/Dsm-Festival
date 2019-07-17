from typing import Any, Dict, List

from peewee import *

from app.models.base import BaseModel, execute_sql
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

        rows = execute_sql(query)

        return rows[0]

    @classmethod
    def get_info_by_rfid(cls, rfid: str) -> Dict[str, Any]:
        query = (
            RFIDTable
            .select(StudentTable.number, StudentTable.name, RFIDTable.point)
            .join(StudentTable)
            .where(RFIDTable.rfid == rfid)
        )
        rows = execute_sql(query)

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
        rows = execute_sql(query)

        return rows


class UnsignedRFIDTable(BaseModel):
    rfid = CharField(unique=True)

    class Meta:
        table_name = 'unsigned_rfid'
