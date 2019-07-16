from flask import Blueprint
from flask_restful import Api

from app.views.booth import history

booth_blueprint = Blueprint('booth', __name__)
booth_api = Api(booth_blueprint)

booth_api.add_resource(history.History, '/history')
