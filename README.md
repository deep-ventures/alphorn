# Another Lambda Python Horrible Router Naivety

[![Build Status](https://travis-ci.org/grudelsud/alphorn.svg?branch=master)](https://travis-ci.org/grudelsud/alphorn)
[![codecov](https://codecov.io/gh/grudelsud/alphorn/branch/master/graph/badge.svg)](https://codecov.io/gh/grudelsud/alphorn)

Alphorn is a simple Python package to handle Lambda invocations routed by the AWS API Gateway with a `{proxy+}` configuration.

This package takes free inspiration (read: steals code) from [Chalice](https://github.com/aws/chalice) and [Lambdarest](https://github.com/trustpilot/python-lambdarest) but only attempts to implement routing functionalities, hence having a naive approach, remaining very simple, and probably lacking loads of features.

## How to use

define your lambda.py file as below, and configure your AWS lambda handler to be lambda.run

```python
from alphorn import Alphorn

app = Alphorn()

@app.route('/sample/{greeting}')
def sample(greeting):
    return {
        'message': str(greeting),
    }

def run(event, context):
    """lambda handler
    """
    return app.handle(event)
```
