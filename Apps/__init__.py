from flask import Flask
from Apps.apis import init_api
from FlaskRedSquirrel.ext import init_ext
from FlaskRedSquirrel.middleware import load_middleware
from FlaskRedSquirrel.settings import envs


def create_app(env):
    # 创建app
    app = Flask(__name__)
    # 注册settings配置，环境配置
    app.config.from_object(envs.get(env))
    # 注册第三方包
    init_ext(app)
    # 注册api
    init_api(app)
    # 注册蓝图
    from Apps import blueprint
    app.register_blueprint(blueprint.api)
    # 注册中间件
    load_middleware(app)
    # 返回app
    return app