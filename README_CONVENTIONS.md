agent:
  - TESTS:
      - Do not suggest or make any code changes in response to test output
      - After test runs wait for user input
  - Do not modify unrelated code, even if it appears broken or suboptimal.
  - Always use Canadian English spelling.
  - HELLO:
      - When I say hello, follow this sequence:
        - Summerize what you understand as key conventions.
        - State what you don't understand from the conventions or can't do.
        - Suggest how we can improve or clarify conventions.
        - STOP and don't do anything else.
        - Be very concice, stick to what's important, give me the tldr version.
        - WAIT.

code:
  - Fail early: do not hide errors, allow scripts to fail naturally.
    - No try blocks, guards, or silent fallbacks unless asked.
    - Do not add validations, docstrings, typing, or alternative approaches unless they are explicitly asked for.
  - No external dependencies unless instructed.
    - Use standard library and simple constructs.
  - No inline comments — code must be self-explanatory.

python:
  - dependency_management: uv
  - enforce_pyproject: true
  - run_start: "uv run poe start"
  - run_dev: "uv run poe dev"
  - example_commands:
    - uv add httpx
    - uv remove httpx
    - uv sync

commit:
  - format: Conventional Commits

