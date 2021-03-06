from flask_restful import Resource, Api
from views import app

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/api/v1/hello')

