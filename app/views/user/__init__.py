from flask import Blueprint
from flask_restful import Api

from app.views.user import create_rfid, login

user_blueprint = Blueprint('user', __name__)
user_api = Api(user_blueprint)

user_api.add_resource(create_rfid.CreateRFID, '/rfid')
