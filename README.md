[![Licence: 0BSD](https://img.shields.io/badge/licence-0BSD-blue.svg)](./LICENSE.md)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](.python-version)

> This is a trick.ca/binet Template

**What is a BDA Cabinet?**

A BDA Cabinet (trick.ca/binet) is an orchestrated automation environment, managed by Tilt. It uses Behaviour-Driven techniques to express provisioning, validation, and potentially monitoring as Gherkin-defined behaviours. This creates a self-describing and self-testing system built with executable scenarios.

Phases (like provisioning, testing, monitoring) are ordered explicitly in `CABINET.yml`.

---

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

## Core Concepts & Practices

This cabinet follows specific patterns for automation and testing:

- **Behaviour-Driven Automation (BDA):** Automates system configuration and dependencies using self-describing, scenario-based tests (`bda_*.feature`, `test_bda_*.py`). BDA scenarios describe *how* the system should be provisioned or changed and are the only tests intended to have side effects (mutable).
- **Acceptance Test-Driven Development (ATDD):** Verifies that system behaviour meets expectations *after* provisioning or changes (`atdd_*.feature`, `test_atdd_*.py`). ATDD scenarios describe *what* the expected behaviour is and must be read-only (immutable).
- **Declarative Infrastructure:** Supporting infrastructure for development and testing (e.g., the `apply` container) is managed declaratively with Kubernetes manifests and Tilt. BDA steps handle the actual application provisioning.
- **Defined Test Order:** Test execution order across phases is strictly controlled by `CABINET.yml` (See Testing section).
- **Tooling:** All tasks are run via `uv` and `poe` (e.g., `uv run poe test`).
- **File Locations:** All BDD scenarios (`.feature` files) and their corresponding Python step definitions (`test_*.py` files) reside in the `features/` directory.

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

- Test execution order is strictly defined by the sequence of files listed in `CABINET.yml`.
- To add a new test file or change the execution order, modify the `tests:` list within `CABINET.yml`. The `features/conftest.py` file reads this configuration to enforce the specified order during test runs.
- Run tests using: `uv run poe test`

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

