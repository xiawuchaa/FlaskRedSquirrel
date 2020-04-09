from flask_restful import Resource, reqparse, fields, abort, marshal
from Apps.apis.api_constant import USER_ACTION_REGISTER, HTTP_CREATE_OK, USER_ACTION_LOGIN, HTTP_OK
from Apps.apis.user.utils import get_user, generate_user_token
from Apps.models.user.user_model import User
from FlaskRedSquirrel.ext import cache


parse_base = reqparse.RequestParser()
parse_base.add_argument("password", type=str, required=True, help="请输入密码")
parse_base.add_argument("action", type=str, required=True, help="请确认请求参数")

parse_register = parse_base.copy()
parse_register.add_argument("username", type=str, required=True, help="请输入用户名")
parse_register.add_argument("phone", type=str, required=True, help="请输入手机号")

parse_login = parse_base.copy()
parse_login.add_argument("username", type=str, help="请输入用户名")
parse_login.add_argument("phone", type=str, help="请输入手机号")

movie_user_fields = {
    "username":fields.String,
    "password":fields.String(attribute="_password"),
    "phone":fields.String,
}

single_movie_user_fields = {
    "status":fields.Integer,
    "msg":fields.String,
    "data":fields.Nested(movie_user_fields)
}


class UserResource(Resource):

    def get(self):
        user = User()
        return {'msg':'ok'}
    def post(self):
        args = parse_base.parse_args()
        password = args.get("password")
        action = args.get("action").lower()

        if action == USER_ACTION_REGISTER:
            args_register = parse_register.parse_args()
            username = args_register.get("username")
            phone = args_register.get("phone")

            user = User()
            user.username = username
            user.password = password
            user.phone = phone
            print(username)
            print(password)
            print(phone)

            if not user.save():
                abort(400, msg="create fail")
            data = {
                "status":HTTP_CREATE_OK,
                "msg":"用户创建成功",
                "data":user
            }
            return marshal(data, single_movie_user_fields)
        elif action == USER_ACTION_LOGIN:
            args_login = parse_login.parse_args()

            username = args_login.get("username")
            phone = args_login.get("phone")

            user = get_user(username) or get_user(phone)

            if not user:
                abort(400, msg="用户不存在")
            if not user.check_password(password):
                abort(401, msg="密码错误")

            if user.is_delete:
                abort(401, msg="用户不存在")
            token = generate_user_token()
            cache.set(token, user.id, timeout=60*60*24*7)
            data = {
                "msg":"login success",
                "status":HTTP_OK,
                "token":token
            }
            return data

        else:
            abort(400, msg="请提供正确的参数")