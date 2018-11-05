import json

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

