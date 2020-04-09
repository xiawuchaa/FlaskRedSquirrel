from Apps.apis.admin import admin_api
from Apps.apis.goods import goods_api
from Apps.apis.user import user_api


def init_api(app):
    admin_api.init_app(app)
    user_api.init_app(app)
    goods_api.init_app(app)



# # 创建蓝图对象  用于前后端不分离  或者处理家姑娘太文件
# api = Blueprint("api_1_0", __name__)
#
# # 导入蓝图的视图
# from . import demo, verify_code, passport, profile, houses, orders, pay