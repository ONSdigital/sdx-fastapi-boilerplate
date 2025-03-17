# sdx-fastapi-boilerplate
A boilerplate for creating fastapi services

## Prerequisites

- Python 3.13
- Poetry

### Installing Python 3.13:

If you don't have Python 3.13 installed, you can install it using pyenv. Follow the instructions below to install pyenv and Python 3.13:

```bash
brew install pyenv
pyenv install 3.13.0
```

### Install Poetry:
   - This project uses Poetry for dependency management. Ensure Poetry is installed on your system.
   - If Poetry is not installed, you can install it using:
```bash
brew install pipx
pipx install poetry
```
- Use the official Poetry installation guide for other installation methods: https://python-poetry.org/docs/#installation
- Verify the installation by using the following command:
```bash
poetry --version
```

## Generate `.env`

To use environment variables, you need to create a `.env` file in the root directory of the project. You can copy the `.env.example` file and rename it to `.env`:

```bash
cp .env.example .env
```

## Running the service

```bash
poetry run dev
```

## Linting

```bash
ruff lint
```
