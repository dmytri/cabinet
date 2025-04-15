[![Licence: 0BSD](https://img.shields.io/badge/licence-0BSD-blue.svg)](./LICENSE.md)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](.python-version)

> This is a trick.ca/binet Template

Cabinets package entire applications for use across the development lifecycle.

- in dev
```bash
tilt up --namespace target
```
- in ci
```bash
tilt up --ci --namespace target
```
They allow use of fully production like environments at every stage, and work well with gitops.


## 🧪 Using This Template

### ✅ From GitHub

Click the **“Use this template”** button on GitHub to create a new repo.

### 🛠️ Via copier

```bash
uvx copier copy https://dmytri/cabinet new-project
cd new-project
git remote add origin git@github.com:your-github/new-project.git
git add .
git commit -m "Initial commit from template"
git push -u origin main
```

## Key Practices

- All code and automation tasks follow Behaviour-Driven Automation (BDA) and Acceptance Test-Driven Development (ATDD) patterns.
- Supporting infrastructure for development and testing (such as the `apply` container, and optionally others) is managed declaratively with Kubernetes manifests and Tilt. Actual application deployment and provisioning is defined by BDA and may use any system.
- Testing and provisioning scenarios live in `features/`, with filenames prefixed by `bda_` or `atdd_`.
- Python test files must be named `test_bda_*.py` for BDA and `test_atdd_*.py` for ATDD.
- Feature files must be named `bda_*.feature` for BDA and `atdd_*.feature` for ATDD.
- All tooling runs via `uv` and `poe`, e.g.:

```bash
uv run poe start      # run app
uv run poe test       # run tests
```

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Tilt](https://docs.tilt.dev/)
- [Python](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/)
- A Kubernetes cluster (local, e.g., [Minikube](https://minikube.sigs.k8s.io/docs/), [Kind](https://kind.sigs.k8s.io/), or [Docker Desktop with Kubernetes enabled](https://docs.docker.com/desktop/kubernetes/)), or a remote cluster

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

- All BDA and ATDD scenarios and their step definitions are in the `features/` directory.
- Test execution order is strictly defined by the sequence of files listed in `CABINET.yml`.
- To add a new test file or change the execution order, modify the `tests:` list within `CABINET.yml`. The `features/conftest.py` file reads this configuration to enforce the specified order during test runs.

## Contributing

- Use [Conventional Commits](https://www.conventionalcommits.org/) for all commit messages.
- Do not add features without corresponding ATDD scenarios and tests.
- Follow the fail-fast principle: do not hide errors or use silent fallbacks unless explicitly required.

# Coding & Automation Conventions

All spelling in code, comments, documentation, and user-facing text must use Canadian English (e.g., "colour", "behaviour", "favour").

This project uses a unified ruleset for all AI agents and automation logic.

Rules are defined in [`CONVENTIONS.md`](./CONVENTIONS.md), which should be symlinked for agents like Cursor to interpret and enforce.

```bash
ln -s CONVENTIONS.md .cursor-rules
```

