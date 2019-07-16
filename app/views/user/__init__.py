from flask import Blueprint
from flask_restful import Api

from app.views.user import info, rfid, login, rank

user_blueprint = Blueprint(
    name='user',
    import_name=__name__,
    url_prefix='/account',
)
user_api = Api(user_blueprint)

user_api.add_resource(rfid.CreateRFID, '/rfid')
user_api.add_resource(info.GetInfoByToken, '/info')
user_api.add_resource(info.GetInfoByRFID, '/info/<rfid>')
user_api.add_resource(login.Login, '/login')
user_api.add_resource(rank.Rank, '/rank')
