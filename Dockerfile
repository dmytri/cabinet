FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /code

COPY pyproject.toml .
COPY tests tests

CMD uv run poe ci
