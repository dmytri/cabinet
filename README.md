## Key Practices

- All code and automation tasks follow [Behavior-Driven Automation (BDA)] and [Acceptance Test-Driven Development (ATDD)] patterns.
- Infra is managed declaratively with Kubernetes manifests applied via Tilt.
- Testing and provisioning scenarios live in `tests/`, with filenames prefixed by `bda_` or `atdd_`.
- All tooling runs via `uv` and `poe`, e.g.:

```bash
uv run poe start      # run app
uv run poe test       # run tests
```

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Tilt](https://docs.tilt.dev/)
- [Minikube](https://minikube.sigs.k8s.io/docs/)
- [Python](https://www.python.org/) (see `.python-version` for the required version)
- [uv](https://docs.astral.sh/uv/)

## Dependency Management

All Python dependencies are managed with [uv](https://docs.astral.sh/uv/).  
Do not use `pip` directly.

Example commands:
- `uv add <package>`
- `uv add --dev <package>`
- `uv remove <package>`
- `uv sync`

## Running the Application

- Start the application: `uv run poe start`
- Run tests: `uv run poe test`

## Infrastructure

- All Kubernetes/infrastructure operations are managed via Tilt.
- Do not use `kubectl` directly.
- Ensure Tilt is running in a dedicated terminal.

## Testing

- All BDA and ATDD scenarios and their step definitions are in the `tests/` directory.
- New test files must be added to the `TESTS` list in `tests/conftest.py`.
- BDA test files (starting with `bda_`) must be listed before ATDD test files (starting with `atdd_`).

## Contributing

- Use [Conventional Commits](https://www.conventionalcommits.org/) for all commit messages.
- Do not add features without corresponding ATDD scenarios and tests.
- Follow the fail-fast principle: do not hide errors or use silent fallbacks unless explicitly required.

# Coding & Automation Conventions

This project uses a unified ruleset for all AI agents and automation logic.

Rules are defined in [`CONVENTIONS.md`](./CONVENTIONS.md), which should be symlinked for agents like Cursor to interpret and enforce:

```bash
ln -s CONVENTIONS.md .cursor-rules
```



