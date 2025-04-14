agent:
  - Do not suggest or make any code changes in response to test output unless the user explicitly requests a fix or modification.
  - Do not modify unrelated code, even if it appears broken or suboptimal.
  - Always use Canadian English spelling
  - hello:
    - When I say hello, follow this sequence
      - confirm what you understand from these conventions
      - say what you don't undertand or can't do
      - stop and don't do anything else

code:
  - Fail early: do not hide errors, allow scrits to fail naturally
    - No try blocks, guards, or silent fallbacks unless asked
    - Do not add validations, docstrings, typing, or alternative approaches unless they are explicitly asked for.
  - No external dependencies unless instructed
    - Use standard library and simple constructs
  - No inline comments — code must be self-explanatory

python:
  dependency_management: uv
  enforce_pyproject: true
  pip_disallowed: true
  run_start: "uv run poe start"
  run_dev: "uv run poe dev"
  example_commands:
    - uv add httpx
    - uv remove httpx
    - uv sync

commit:
  format: Conventional Commits

