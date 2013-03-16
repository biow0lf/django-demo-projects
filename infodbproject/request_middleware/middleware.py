from request_middleware.models import RequestModel
import json

"""
Middleware for storing all http requests in the DB
"""


class StoreEveryHttpRequestInDb(object):
    def process_request(self, request):
        secure = request.is_secure()
        path = request.path
        get = json.dumps(request.GET)
        post = json.dumps(request.POST)
        cookies = json.dumps(request.COOKIES)

        r = RequestModel(secure=secure,
                         path=path,
                         get=get,
                         post=post,
                         cookies=cookies)
        r.save()
        return None
