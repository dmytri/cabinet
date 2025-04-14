# === <python> ===
python:
  dependency_management: uv
  enforce_pyproject: true
  pip_disallowed: true
  run_script: "uv run poe <task>"
  run_start: "uv run poe start"
  run_dev: "uv run poe dev"
  example_commands:
    - uv add httpx
    - uv add --dev pytest
    - uv add --group test pytest-cov
    - uv remove httpx
    - uv sync
  reference: https://docs.astral.sh/uv/concepts/projects/dependencies/
# === </python> ===
