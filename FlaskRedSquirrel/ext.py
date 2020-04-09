from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
bootstrap = Bootstrap()
cache = Cache(
    config = {
        "CACHE_TYPE":"redis"
    }
)

def init_ext(app):
    # 初始化数据库
    db.init_app(app)
    # 初始化迁移
    migrate.init_app(app, db)
    # 初始化Mail
    mail.init_app(app)
    # 初始化缓存cache
    cache.init_app(app)
    # 初始化BootStrap
    bootstrap.init_app(app)

