import os


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    JSON_AS_ASCII = False

    # Api class in flask_restful will replace the origin Flask App exception handler.
    # But if PROPAGATE_EXCEPTIONS is true, custom exception handler will works.
    # https://github.com/flask-restful/flask-restful/blob/master/flask_restful/__init__.py#L281
    PROPAGATE_EXCEPTIONS = True


class LocalConfig(BaseConfig):
    ENV = "development"
    DEBUG = True


class ProductionConfig(BaseConfig):
    ENV = "production"
    DEBUG = False


class TestConfig(BaseConfig):
    ENV = "test"
    TESTING = True
