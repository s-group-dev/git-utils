.DEFAULT_GOAL := help
.PHONY: ci clean build build-local format help init install install-local release-test test test-cov

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":[^#]*?## "}; {printf "\033[36m%-50s\033[0m %s\n", $$1, $$2}'


ci: lint test ## Run local ci

clean: ## Remove all Python combile files
	find . -name '*.pyc' -delete
	rm -rf build *.egg-info
	pipenv clean

build: ## Build distribution
	python3 -m build

build-local: ## Create local distribution 
	python3 setup.py sdist

format: ## Format code using isort and black
	pipenv run black src/ tests/
	pipenv run isort src/ test/

init: ## Initialize project
	pipenv run pre-commit install -t pre-commit
	pipenv run pre-commit install -t pre-push

install: ## Install dependencies
	pipenv install --dev .

install-local: ## Install a local setup.py into your virtual environment
	pipenv install -e .

lint: ## Lint all Python files
	pipenv run rstcheck **/*.rst
	pipenv run flake8 src/ tests/
	pipenv run mypy src/ tests/

release-test: ## Release to testpypi
	python3 -m twine upload dist/*

release-test: ## Release to testpypi
	python3 -m twine upload --repository testpypi dist/*

test: ## Run tests
	pipenv run pytest

test-cov: ## Run test coverage
	pipenv run pytest --cov --cov-report term --cov-report html:./coverage --cov-fail-under=0

# vim: noexpandtab