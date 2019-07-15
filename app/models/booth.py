from peewee import *

from app.extension import db
from app.models.base import BaseModel


class BoothTable(BaseModel):
    booth_id = IntegerField(primary_key=True)
    booth_name = CharField(primary_key=True)
    booth_rating = IntegerField(default=100)

    class Meta:
        database = db
        table_name = 'booth'
