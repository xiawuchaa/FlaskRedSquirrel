from werkzeug.security import generate_password_hash, check_password_hash
from Apps.models import BaseModel
from Apps.models.user.user_constant import PERMISSION_NONE
from FlaskRedSquirrel.ext import db


COMMON_USER = 0
BLACK_USER = 1
VIP_USER = 2

class User(BaseModel):

    icon = db.Column(db.String(32))
    username = db.Column(db.String(32), unique=True)
    alipay_id = db.Column(db.String(32), unique=True)
    wechat_id = db.Column(db.String(32), unique=True)
    phone = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))
    invest_id = db.Column(db.String(16))
    is_wechat = db.Column(db.Boolean, default=False)
    is_taobao = db.Column(db.Boolean, default=False)
    permission = db.Column(db.Integer, default=PERMISSION_NONE)
    is_delete = db.Column(db.Boolean, default=False)

    @property
    def password(selfs):
        raise Exception("can't access")

    @password.setter
    def password(self, password_value):
        self._password = generate_password_hash(password_value)

    def check_password(self, password_value):
        return check_password_hash(self._password, password_value)

    def check_permission(self, permission):
        if BLACK_USER & self.permission == BLACK_USER:
            return False
        else:
            return permission & self.permission == permission