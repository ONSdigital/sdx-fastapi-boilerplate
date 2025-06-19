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

.PHONY: test
test:
	@echo "Running UV sync..."
	uv sync
	@echo "Running Unit Tests..."
	uv run pytest -v --disable-warnings tests/

.PHONY: test-parallel
test-parallel:
	@echo "Running Unit Tests in parallel..."
	@echo "Running UV sync..."
	uv sync
	@echo "Running Unit Tests..."
	uv run pytest -n auto -v --disable-warnings tests/  --- Uncomment this line to run tests in parallel

start-dev:
	@echo "Starting development server..."
	uv run uvicorn app.main:app
