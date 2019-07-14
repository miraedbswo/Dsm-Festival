from datetime import datetime
from pytz import timezone, utc

from flask_restful import Resource

KST = timezone('Asia/Seoul')


class BaseResource(Resource):
    @staticmethod
    def kst_now() -> datetime:
        now = datetime.utcnow()
        kst_now = utc.localize(now).astimezone(KST)
        return kst_now
