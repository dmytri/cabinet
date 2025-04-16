FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /code

COPY CABINET.yaml .
COPY pyproject.toml .
COPY features features

CMD uv run poe ci
