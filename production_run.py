import os

from app import create_app
from config.app_config import ProductionConfig
from config.db_config import RemoteDBConfig

if "SECRET_KEY" not in os.environ:
    raise Warning("The secret key must bpipe passed by the <SECRET_KEY> envvar.")

application = create_app(ProductionConfig, RemoteDBConfig)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, threaded=True)