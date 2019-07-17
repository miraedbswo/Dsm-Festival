from enum import Enum
from typing import Any, Dict, List

from peewee import *

from app.extension import db
from app.exception import ForbiddenException, WrongAuthException, UsedBoothException
from app.models.base import BaseModel, execute_sql
from app.models.student import StudentTable


class PayStatus(Enum):
    HAS_MONEY = 0
    STAFF = 1


class RFIDTable(BaseModel):
    rfid = CharField(primary_key=True, max_length=16)
    student_id = ForeignKeyField(StudentTable, db_column='id', to_field='id')
    point = IntegerField(default=15)
    level = IntegerField()

    class Meta:
        table_name = 'rfid'

    @classmethod
    def is_payable(cls, point: int, level: int) -> PayStatus:
        if point < 0:
            raise ForbiddenException()

        if level > 0:
            return PayStatus.STAFF

        return PayStatus.HAS_MONEY

    @classmethod
    def pay(cls, rfid: str, booth_id: int, point: int):
        from app.models.history import HistoryTable
        user = RFIDTable.get_info_by_rfid(rfid)
        if HistoryTable.is_used(rfid, booth_id):
            raise UsedBoothException()

        remain_point = user.get('point') + point
        level = user.get('level')

        pay_level = RFIDTable.is_payable(remain_point, level)

        if (level == pay_level) == 0:
            query = RFIDTable.update(point=remain_point).where(RFIDTable.rfid == rfid)
            db.execute_sql(str(query))

        HistoryTable.set_history(rfid, booth_id, point)

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
            .select(StudentTable.number, StudentTable.name, RFIDTable.point, RFIDTable.level)
            .join(StudentTable)
            .where(RFIDTable.rfid == rfid)
        )
        rows = execute_sql(query)

        if not rows:
            raise WrongAuthException()

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
