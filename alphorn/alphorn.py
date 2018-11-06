from collections import defaultdict

from .route import RouteEntry
from .response import Response


class Alphorn:
    _routes = defaultdict(dict)

    def route(self, path, **kwargs):
        def _register_view(view_func):
            # if path in self._routes.keys():
            #     raise ValueError(f'handler for {path} is already defined')
            # self._routes[path] = view_func
            self._add_route(path, view_func, **kwargs)
            return view_func
        return _register_view

    def _add_route(self, path, view_func, **kwargs):
        name = kwargs.pop('name', view_func.__name__)
        methods = kwargs.pop('methods', ['GET'])
        cors = kwargs.pop('cors', True)

        if kwargs:
            unexpected = ', '.join(list(kwargs))
            raise TypeError(f'route() got unexpected arguments: {unexpected}')

        for method in methods:
            if method in self._routes[path]:
                raise ValueError(f'{method} handler for {name} is already defined')

            entry = RouteEntry(view_func, name, path, method, cors)
            self._routes[path][method] = entry

    def _find_route_entry(self, event):
        path = event.get('path')
        method = event.get('requestContext', {}).get('httpMethod')

        for route in sorted(self._routes.keys(), reverse=True):
            try:
                route_entry = self._routes[route][method]
                m = route_entry.match(path)
                if m is not None:
                    return route_entry, m
            except Exception:
                pass
        return None, None

    def handle(self, event):
        """

        :param event: the event parameter received by a lambda handler
        :type event: dict
        """
        route_entry, match = self._find_route_entry(event)
        try:
            body = route_entry.view_func(**match.groupdict())
            response = Response(route_entry.cors)
            return response(body)
        except Exception:
            return Response()(status_code=404)
