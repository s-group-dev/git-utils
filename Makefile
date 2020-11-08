.DEFAULT_GOAL := help
.PHONY: ci clean distribute format help init install-local install linc-fix lint lint-fix test

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":[^#]*?## "}; {printf "\033[36m%-50s\033[0m %s\n", $$1, $$2}'


ci: lint test ## Run local ci

clean: ## Remove all Python combile files
	find . -name '*.pyc' -delete
	rm -rf build *.egg-info
	pipenv clean

distribute: ## Create distribution and install it to your machine
	pip3 uninstall -y guts
	python3 setup.py sdist
	pip3 install dist/guts-*.tar.gz

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

test: ## Run tests
	pipenv run pytest

test-cov: ## Run test coverage
	pipenv run pytest --cov --cov-report term --cov-report html:./coverage --cov-fail-under=0

# vim: noexpandtab
