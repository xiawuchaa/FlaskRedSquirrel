import os
import pymysql

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or "3306"
    database = dbinfo.get("DATABASE") or ""
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, database)

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRECT_KEY = "fjdsaufrioewv540-945-023"
    dbinfo = {
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"root",
        "HOST":"localhost",
        "PORT":3306,
        "DATABASE":"FlaskRedSquirrel"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

class DevelopConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True

class StagingConfig(Config):
    pass

class ProductConfig(Config):
    pass

envs = {
    "development":DevelopConfig,
    "testing":TestConfig,
    "staging":StagingConfig,
    "product":ProductConfig,
    "default":DevelopConfig
}

ADMINS = ('Rock', 'Tom')

FILE_PATH_PREFIX = "/static/uploads/icons"

STATIC_FOLD='static'
STATIC_URL_PATH='/static'

TEMPLATE_FOLD='templates'

UPLOADS_DIR = os.path.join(BASE_DIR, 'static/uploads/icons')

if __name__ == '__main__':
    print(BASE_DIR)  # /home/atea/PycharmProjects/FlaskRedSquirrel
    print(FILE_PATH_PREFIX)
    print(UPLOADS_DIR)  # /home/atea/PycharmProjects/FlaskRedSquirrel/statics/uploads/icons