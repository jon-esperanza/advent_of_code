.PHONY: fmt
fmt:
	pipenv run black .
	pipenv run isort .

.PHONY: lint
lint:
	pipenv run flake8 .

.PHONY: test
test:
	pipenv run pytest

.PHONY: clean
clean:
	rm -rf .pytest_cache
	pipenv --rm

.PHONY: deps
deps:
	pipenv install --dev
