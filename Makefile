test:
	pipenv run pytest -n 4 --cov-config .coveragerc --cov=alphorn --cov-report html:test-reports --junitxml=test-reports/results.xml tests/
