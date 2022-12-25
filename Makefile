test:
	poetry run pytest -vv

lint:
	poetry run flake8 algorithms tests

test-cov:
	poetry run pytest --cov=algorithms --cov-report xml
