test:
	pipenv run pytest -n 4 --cov-config .coveragerc --cov=alphorn --cov-report=xml:coverage.xml --cov-report=html:test-reports --junitxml=test-reports/results.xml tests/

codecov:
	pipenv run codecov
