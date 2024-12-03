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

.PHONY: day
day:
	./advent_of_code/2024/scripts/new_day.sh "$(DAY)"
	make fmt
