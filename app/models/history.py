from typing import Any, Dict, List

from peewee import *

from app.extension import db
from app.models.base import BaseModel, cursor_to_dict
from app.models import BoothTable, StudentTable, RFIDTable


class HistoryTable(BaseModel):
    rfid = ForeignKeyField(RFIDTable, db_column='rfid', to_field='rfid')
    used_booth = ForeignKeyField(BoothTable, db_column='used_booth', to_field='booth_id')
    point = IntegerField()

    class Meta:
        table_name = 'history'

    @classmethod
    def get_history(cls, user_id: str) -> List[Dict[str, Any]]:
        query = (
            BoothTable
            .select(BoothTable.booth_name, HistoryTable.point)
            .join(StudentTable)
            .join(HistoryTable)
            .where(StudentTable.id == user_id)
        )

        cursor = db.execute_sql(str(query))
        rows = cursor_to_dict(cursor)

        return rows
