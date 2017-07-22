from flask import Flask
from flask_restful import Api

import mongoengine

import config
from resources.index import IndexResource
from resources.post import PostResource

mongoengine.connect(host=config.db['mongo_uri'])

app = Flask(__name__)
api = Api(app)

api.add_resource(IndexResource, '/');
api.add_resource(PostResource, '/post');

if __name__ == '__main__':
    app.run(debug=True)
