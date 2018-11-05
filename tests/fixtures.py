import pytest

from alphorn import Alphorn

@pytest.fixture
def sample_app_200():
    app = Alphorn()
    @app.route('/config/123')
    def sample():
        return {
            'message': 'sample',
        }
    return app

@pytest.fixture
def sample_app_404():
    app = Alphorn()
    @app.route('/sample')
    def sample():
        return {
            'message': 'sample',
        }
    return app

@pytest.fixture
def sample_event():
    return {
        "resource": "/{proxy+}",
        "path": "/config/123",
        "httpMethod": "GET",
        "headers": None,
        "multiValueHeaders": None,
        "queryStringParameters": {
            "type": "ev",
            "brand": "porsche"
        },
        "multiValueQueryStringParameters": {
            "type": [
                "ev"
            ],
            "brand": [
                "porsche"
            ]
        },
        "pathParameters": {
            "proxy": "config/123"
        },
        "stageVariables": None,
        "requestContext": {
            "path": "/{proxy+}",
            "accountId": "648039538347",
            "resourceId": "9bg3n3",
            "stage": "test-invoke-stage",
            "domainPrefix": "testPrefix",
            "requestId": "4317cb31-df5f-11e8-a0aa-d9c9e01beb05",
            "identity": {
                "cognitoIdentityPoolId": None,
                "cognitoIdentityId": None,
                "apiKey": "test-invoke-api-key",
                "cognitoAuthenticationType": None,
                "userArn": "arn:aws:iam::648039538347:user/tom@londondroids.com",
                "apiKeyId": "test-invoke-api-key-id",
                "userAgent": "aws-internal/3 aws-sdk-java/1.11.432 Linux/4.9.124-0.1.ac.198.71.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.181-b13 java/1.8.0_181",
                "accountId": "648039538347",
                "caller": "AAAUSERID",
                "sourceIp": "test-invoke-source-ip",
                "accessKey": "AAAACCESSKEY",
                "cognitoAuthenticationProvider": None,
                "user": "AAAUSERID"
            },
            "domainName": "testPrefix.testDomainName",
            "resourcePath": "/{proxy+}",
            "httpMethod": "GET",
            "extendedRequestId": "PyLlLFtmjoEFSDQ=",
            "apiId": "pdbi2eofs7"
        },
        "body": None,
        "isBase64Encoded": False
    }
