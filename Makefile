test:
	poetry run pytest

lint:
	poetry run flake8 algorithms tests

test-cov:
	poetry run pytest --cov=algorithms --cov-report xml
