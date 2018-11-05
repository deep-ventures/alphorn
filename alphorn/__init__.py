import json
import functools


class Response:
    _default_headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True,
    }

    def __init__(self, headers=None):
        self._headers = headers

    @property
    def headers(self):
        if self._headers is not None:
            self._default_headers.update(self._headers)
        return self._default_headers

    def __call__(self, body={}, status_code=200):
        return {
            "isBase64Encoded": False,
            "statusCode": status_code,
            "headers": self.headers,
            "body": json.dumps(body)
        }


class Alphorn:
    _routes = {}

    def __init__(self, headers=None):
        self._headers = headers

    def route(self, path):
        def _register_view(view_func):
            if path in self._routes.keys():
                raise ValueError(f'handler for {path} is already defined')
            self._routes[path] = view_func
            return view_func
        return _register_view

    def handle(self, event):
        """

        :param event: the event parameter received by a lambda handler
        :type event: dict
        """
        # TODO: marshall path fragments with parameters then invoke function
        # passing the correct path parameters
        response = Response(self._headers)
        func = self._routes.get(event.get('path'))
        try:
            body = func()
            return response(body)
        except Exception as e:
            return response(status_code=404)
