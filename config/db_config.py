import os


class LocalDBConfig:
    DB_SETTING = {
        'database': 'test',
        'user': 'test',
        'password': 'test',
        'host': '127.0.0.1',
        'port': 3306,
    }


class RemoteDBConfig:
    DB_SETTING = {
        'database': os.getenv('DB_DATABASE'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST', 'dsm-festival.c8yvg2qxmek7.ap-northeast-2.rds.amazonaws.com'),
        'port': os.getenv('PORT'),
    }
