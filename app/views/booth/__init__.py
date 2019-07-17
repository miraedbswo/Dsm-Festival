from flask import Blueprint
from flask_restful import Api

from app.views.booth import history, pay

booth_blueprint = Blueprint('booth', __name__)
booth_api = Api(booth_blueprint)

booth_api.add_resource(history.History, '/history')
booth_api.add_resource(pay.Pay, '/pay')
