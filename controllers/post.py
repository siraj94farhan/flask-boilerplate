from models.post import Post
from parsers.post import PostParser
import json

class PostController:
    def post(self):
        args = PostParser.parse_args()
        postData = Post(title=args['title'], content=args['content'])
        postData.save()
        return json.loads(postData.to_json())

    def get(self):
        return json.loads(Post.objects().to_json())
