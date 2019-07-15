from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.views.base import BaseResource
from app.models import RFIDTable


class Rank(BaseResource):
    @jwt_required
    def get(self):
        top_10_rank = RFIDTable.get_top_10_rank()
        my_rank = RFIDTable.get_my_rank(get_jwt_identity())

        result = {
            'top_10_rank': [
                {
                    "name": user.name,
                    "point": user.point,
                } for user in top_10_rank
            ],

            'my_rank': {
                "name": my_rank.name,
                "point": my_rank.point,
            },
        }

        return jsonify(result), 201
