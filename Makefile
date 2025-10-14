SHELL := bash
.ONESHELL:


.PHONY: lint
lint:
	@echo "Running Ruff linter..."
	uv run --only-group lint ruff check --fix


.PHONY: format
format:
	@echo "Running Ruff formatter..."
	uv run --only-group lint ruff format


.PHONY: test
test:
	@echo "Running UV sync..."
	uv sync
	@echo "Running Unit Tests..."
	uv run --group test pytest -v --disable-warnings tests/

.PHONY: test-parallel
test-parallel:
	@echo "Running Unit Tests in parallel..."
	@echo "Running UV sync..."
	uv sync
	@echo "Running Unit Tests..."
	uv run --group test pytest -n auto -v --disable-warnings tests/

.PHONY: dev
dev:
	@echo "Starting development server..."
	uv run uvicorn app.main:app


.PHONY: increment
increment:
	@echo "🔼 Bumping project version..."
	uv run --only-group version-check python .github/scripts/increment_version.py
	@echo "🔄 Generating new lock file..."
	uv lock
