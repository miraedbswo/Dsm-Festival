from peewee import *

from app.models.base import BaseModel


class StudentTable(BaseModel):
    id = CharField(primary_key=True)
    pw = CharField()
    name = CharField(max_length=10)
    number = IntegerField()
    email = CharField()

    class Meta:
        table_name = 'student'
