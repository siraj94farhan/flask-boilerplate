from flask_restful import Resource
from controllers.post import PostController

class PostResource(Resource):
    def post(self):
        return PostController.post(self)

    def get(self):
        return PostController.get(self);
