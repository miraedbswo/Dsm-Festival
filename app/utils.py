from datetime import datetime
from pytz import timezone, utc

KST = timezone('Asia/Seoul')


def kst_now() -> datetime:
    utc_now = datetime.utcnow()
    now = utc.localize(utc_now).astimezone(KST)
    return now
