from flask_jwt_extended import jwt_required, get_jwt_identity

from app.views.base import BaseResource
from app.models.history import HistoryTable


class History(BaseResource):
    @jwt_required
    def get(self):
        history = HistoryTable.get_history(user_id=get_jwt_identity())

        return {
            'history': history
        }, 200

