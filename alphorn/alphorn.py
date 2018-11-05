from .response import Response

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
