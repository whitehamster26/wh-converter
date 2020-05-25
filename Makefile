lint:
	poetry run flake8 wh-conv
test:
	poetry run pytest --cov=wh-conv --cov-report xml tests/