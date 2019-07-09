import os

from app import create_app
from config.app_config import LocalConfig
from config.db_config import LocalDBConfig

if "SECRET_KEY" not in os.environ:
    raise Warning("The secret key must bpipe passed by the <SECRET_KEY> envvar.")

app = create_app(LocalConfig, LocalDBConfig)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, threaded=True)
