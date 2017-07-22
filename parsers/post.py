from flask_restful import reqparse

PostParser = reqparse.RequestParser()

PostParser.add_argument('title', required=True)
PostParser.add_argument('content', required=True)
