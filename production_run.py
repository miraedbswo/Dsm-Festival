import os

from app import create_app
from config.app_config import ProductionConfig
from config.db_config import RemoteDBConfig

if "SECRET_KEY" not in os.environ:
    raise Warning("The secret key must bpipe passed by the <SECRET_KEY> envvar.")

application = create_app(ProductionConfig, RemoteDBConfig)
