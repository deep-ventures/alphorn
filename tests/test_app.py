import pytest
import json

from .fixtures import sample_app_200, sample_app_404, sample_event
from alphorn import Alphorn, Response, version


def test_version():
    assert version.__version__ == '0.1'


def test_event(sample_event):
    assert sample_event['resource'] == '/{proxy+}'


def test_basic_headers():
    r = Response()
    assert r()['headers'] == Response._default_headers


def test_extra_headers():
    extra_headers = {
        'Authorization': 'blah',
    }
    r = Response(headers=extra_headers)
    extra_headers.update(Response._default_headers)
    assert r()['headers'] == extra_headers


def test_handler_404(sample_app_404, sample_event):
    out = sample_app_404.handle(sample_event)
    assert out['statusCode'] == 404


def test_handler_200(sample_app_200, sample_event):
    out = sample_app_200.handle(sample_event)
    assert out['statusCode'] == 200
    assert out['body'] == json.dumps({'message': 'sample'})


def test_routes_raises():
    app = Alphorn()
    @app.route('/path')
    def path_1():
        return {}

    with pytest.raises(ValueError):
        @app.route('/path')
        def path_2():
            return {}
