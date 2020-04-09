from flask_restful import Api
from Apps.apis.goods.index import IndexResource

goods_api = Api(prefix='/goods')
goods_api.add_resource(IndexResource, '/index/')