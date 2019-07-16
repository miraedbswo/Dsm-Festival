from datetime import datetime
from peewee import Model
from peewee import DateTimeField

from app.extension import db


def cursor_to_dict(cursor):
    columns = [col[0] for col in cursor.description]
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return rows


class BaseModel(Model):
    class Meta:
        database = db

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(BaseModel, self).save(*args, **kwargs)

    @classmethod
    def update(cls, __data=None, **update):
        if 'updated_at' not in update:
            update['updated_at'] = cls.updated_at.default()

        return super(BaseModel, cls).update(__data, **update)
