from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.views.base import BaseResource
from app.models import RFIDTable


class Rank(BaseResource):
    def get(self):
        top_10_rank = RFIDTable.get_top_10_rank()

        return {
            'top_10_rank': top_10_rank
        }, 201
