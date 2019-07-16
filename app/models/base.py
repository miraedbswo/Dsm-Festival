from peewee import Model
from peewee import DateTimeField

from app.extension import db
from app.utils import kst_now


class BaseModel(Model):
    class Meta:
        database = db

    created_at = DateTimeField(default=kst_now)
    updated_at = DateTimeField(default=kst_now)

    def save(self, *args, **kwargs):
        self.updated_at = kst_now()
        return super(BaseModel, self).save(*args, **kwargs)

    @classmethod
    def update(cls, __data=None, **update):
        if 'updated_at' not in update:
            update['updated_at'] = cls.updated_at.default()

        return super(BaseModel, cls).update(__data, **update)
