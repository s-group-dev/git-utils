.DEFAULT_GOAL := help
.PHONY: ci clean distribute format help init install-local install linc-fix lint lint-fix test

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":[^#]*?## "}; {printf "\033[36m%-50s\033[0m %s\n", $$1, $$2}'


ci: linc test ## Run local ci

clean: ## Remove all Python combile files
	find . -name '*.pyc' -delete
	rm -rf build *.egg-info
	pipenv clean

distribute: ## Create distribution and install it to your machine
	pip3 uninstall -y guts
	python3 setup.py sdist
	pip3 install dist/guts-*.tar.gz

format: ## Format code using isort and black
	pipenv run black src/
	pipenv run isort src/

init: ## Initialize project
	@echo "Installing Git pre-commit hook"
	ln -sf ../../bin/git-pre-commit-hook.sh .git/hooks/pre-commit

install: ## Install dependencies
	pipenv install --dev .

install-local: ## Install a local setup.py into your virtual environment
	pipenv install -e .

linc: ## Lint changed Python files
	bin/run-lint.sh --changed

linc-fix: ## Fix linter errors for changes Python files
	bin/run-lint.sh --changed --fix

lint: ## Lint all Python files
	bin/run-lint.sh

lint-fix: ## Fix linter for Python files
	bin/run-lint.sh --fix

test: ## Run tests
	@PYTHONPATH=. pytest

# vim: noexpandtab
