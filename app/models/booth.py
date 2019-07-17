from peewee import *

from app.extension import db
from app.models.base import BaseModel


class BoothTable(BaseModel):
    booth_id = IntegerField(primary_key=True)
    booth_name = CharField()

    class Meta:
        database = db
        table_name = 'booth'
