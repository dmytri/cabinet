[![Licence: 0BSD](https://img.shields.io/badge/licence-0BSD-blue.svg)](./LICENSE.md)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](.python-version)

> This is a trick.ca/binet Template

**What is a BDA Cabinet?**

A BDA Cabinet (trick.ca/binet) is an orchestrated automation environment, managed by Tilt, that runs declarative test and provisioning scenarios using Behaviour-Driven techniques. It expresses provisioning, validation, and monitoring as Gherkin-defined behaviours, creating a self-describing and self-testing system.

Standard phases, ordered explicitly in `CABINET.yml`, typically include:
- **cabinet:** Verifies the environment (e.g., tools, connectivity). Read-only.
- **bda:** Provisions the system using executable scenarios. **Mutable (causes side effects).**
- **atdd:** Validates system features and behaviour against acceptance criteria. Read-only.
- **bdm:** Monitors system behaviour continuously (synthetic checks). Read-only.

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

This cabinet implements specific phases and patterns:

- **Phases:** The system utilizes distinct, ordered phases defined in `CABINET.yml` (see overview above). This template primarily includes examples for BDA and ATDD phases.
- **Behaviour-Driven Automation (BDA):** Corresponds to the `bda` phase. Automates system configuration and dependencies (`bda_*.feature`, `test_bda_*.py`). These are the only steps intended to modify the target system state (mutable).
- **Acceptance Test-Driven Development (ATDD):** Corresponds to the `atdd` phase. Verifies system behaviour meets expectations (`atdd_*.feature`, `test_atdd_*.py`). These steps must be read-only (immutable).
- **Other Phases:** While not fully exemplified here, the `cabinet` (environment checks) and `bdm` (monitoring) phases follow the same BDD structure but must also be read-only.
- **Declarative Infrastructure:** Supporting infrastructure (like the test execution environment) is managed declaratively (Kubernetes manifests, Tilt). BDA steps handle application-specific provisioning.
- **Defined Test Order:** Test execution order across all phases is strictly controlled by the file sequence in `CABINET.yml` (See Testing section).
- **Tooling:** All tasks run via `uv` and `poe` (e.g., `uv run poe test`).
- **File Locations:** All BDD scenarios (`.feature`) and step definitions (`test_*.py`) are in the `features/` directory, prefixed according to their phase (`bda_`, `atdd_`, etc.).

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

