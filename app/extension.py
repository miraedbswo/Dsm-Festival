from flask_cors import CORS
from flask_jwt_extended import JWTManager
from peewee import MySQLDatabase

db: MySQLDatabase
jwt = JWTManager()
cors = CORS()
