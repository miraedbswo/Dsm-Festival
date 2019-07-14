import os

from flask_cors import CORS
from flask_jwt_extended import JWTManager
from peewee import MySQLDatabase

db: MySQLDatabase = MySQLDatabase(**{
        'database': os.getenv('DB_DATABASE'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST', 'dsm-festival.c8yvg2qxmek7.ap-northeast-2.rds.amazonaws.com'),
        'port': os.getenv('PORT', 3306),
    })

jwt = JWTManager()
cors = CORS()
