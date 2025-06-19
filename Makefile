SHELL := bash
.ONESHELL:


.PHONY: lint
lint:
	@echo "Running Ruff linter..."
	uv run ruff check --fix

.PHONY: format
format:
	@echo "Running Ruff formatter..."
	uv run ruff format
