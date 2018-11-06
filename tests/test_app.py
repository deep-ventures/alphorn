import pytest
import json

from .fixtures import sample_app_200, sample_app_404, sample_event
from alphorn import Alphorn, Response, version


def test_version():
    assert version.__version__ == '0.2'


def test_event(sample_event):
    assert sample_event['resource'] == '/{proxy+}'


def test_basic_headers():
    r = Response()
    assert r()['headers'] == Response._cors_headers


def test_extra_headers():
    extra_headers = {
        'Authorization': 'blah',
    }
    r = Response(headers=extra_headers)
    extra_headers.update(Response._cors_headers)
    assert r()['headers'] == extra_headers


def test_handler_404(sample_app_404, sample_event):
    out = sample_app_404.handle(sample_event)
    assert out['statusCode'] == 404


def test_handler_200(sample_app_200, sample_event):
    out = sample_app_200.handle(sample_event)
    assert out['statusCode'] == 200
    assert out['body'] == json.dumps({'message': '123'})


def test_routes_raises_path():
    app = Alphorn()
    @app.route('/path')
    def path_1():
        return {}

    with pytest.raises(ValueError):
        @app.route('/path')
        def path_2():
            return {}


def test_routes_raises_args():
    app = Alphorn()
    with pytest.raises(TypeError):
        @app.route('/path', weird_arg='something')
        def path():
            return {}


def test_routes_doesnt_find_entry(sample_event):
    app = Alphorn()
    @app.route('/config/123', methods=['POST'])
    def path():
        return {}

    out = app.handle(sample_event)
    assert out['statusCode'] == 404
