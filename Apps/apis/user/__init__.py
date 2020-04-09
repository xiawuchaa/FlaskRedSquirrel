from flask_restful import Api

from Apps.apis.user.user_api import UserResource

user_api = Api(prefix='/api/user')


user_api.add_resource(UserResource, '/user/')