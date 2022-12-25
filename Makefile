test:
	poetry run pytest

lint:
	poetry run flake8 algorithms tests
