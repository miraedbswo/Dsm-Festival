from typing import Any, Dict, List

from peewee import *

from app.models.base import BaseModel, execute_sql
from app.models import BoothTable, StudentTable, RFIDTable


class HistoryTable(BaseModel):
    rfid = ForeignKeyField(RFIDTable, db_column='rfid', to_field='rfid')
    used_booth = ForeignKeyField(BoothTable, db_column='used_booth', to_field='booth_id')
    point = IntegerField()

    class Meta:
        table_name = 'history'

    @classmethod
    def is_used(cls, rfid: str, booth_id: int) -> bool:
        query = (
            HistoryTable
            .select(HistoryTable.used_booth)
            .where(
                (HistoryTable.rfid == rfid) &
                (HistoryTable.used_booth == booth_id)
            )
        )

        row = execute_sql(query)

        if row is None:
            return False

        return True

    @classmethod
    def get_history(cls, user_id: str) -> List[Dict[str, Any]]:
        query = (
            BoothTable
            .select(BoothTable.booth_name, HistoryTable.point)
            .join(StudentTable)
            .join(HistoryTable)
            .where(StudentTable.id == user_id)
        )

        rows = execute_sql(query)

        return rows
