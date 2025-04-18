# BDA Cabinet Template

[![Licence: 0BSD](https://img.shields.io/badge/licence-0BSD-blue.svg)](./LICENSE.md)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](.python-version)

> A trick.ca/binet Template for Behaviour-Driven Automation

## What is a BDA Cabinet?

A BDA Cabinet (trick.ca/binet) is an orchestrated automation environment,
managed by Tilt, that runs declarative test and provisioning scenarios using
Behaviour-Driven techniques. It expresses provisioning, validation, and
monitoring as Gherkin-defined behaviours, creating a self-describing and
self-testing system.

### Standard Phases

Phases are ordered explicitly in [`CABINET.yaml`](./CABINET.yaml):

| Phase | Purpose | Nature |
|-------|---------|--------|
| **ready** | Verifies the environment | Verify-only |
| **configure** | Provisions the system using executable scenarios | Declare and Verify |
| **accept** | Validates system features against acceptance criteria | Verify-only |
| **monitor** | Monitors system behaviour continuously | Verify-only |

---

## Benefits

Cabinets package entire applications for use across the development lifecycle:

- **Development Environment**
  ```bash
  tilt up --namespace target
  ```

Cabinets enable fully production-like environments at every stage and integrate seamlessly with GitOps workflows.

## 🧪 Using This Template

### ✅ From GitHub

Click the **"Use this template"** button on GitHub to create a new repository.

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

### Phases and Documentation

- **Distinct Phases**: The system utilizes ordered phases defined in `CABINET.yaml` (see overview above)
- **Detailed Documentation**: For comprehensive definitions and rules, see the [BDA Cabinet Framework documentation](./README_BDA.md)
- **Setup Requirements**: For environment setup and critical requirements, see the [Setup and Critical Requirements documentation](./README_SETUP.md)
- **Agent Guidelines**: For AI agent behavior guidelines, see the [AI Agent Guidelines documentation](./README_CONVENTIONS.md)

### Implementation Approaches

- **Ready Phase**:
  - Verifies that the Tilt apply container has all required dependencies
  - Files: `ready.feature`, `test_ready.py`
  - Read-only checks with no side effects

- **Configure Phase**:
  - Declaratively provisions and configures system infrastructure via BDA
  - Files: `configure_<feature>.feature`, `test_configure_<feature>.py`
  - **Only these steps may modify system state** (mutable)

- **Accept Phase**:
  - Runs acceptance tests to confirm user-visible behaviour
  - Files: `accept_<feature>.feature`, `test_accept_<feature>.py`
  - Must be read-only (immutable)

- **Monitor Phase**:
  - Continuously validates live runtime behaviour with read-only checks
  - Files: `monitor.feature`, `test_monitor.py`
  - Must be read-only (immutable)

### Architecture Principles

- **Apply Container**: The Tilt-managed container environment where all BDD scenarios are executed
- **Target Application**: The software application being deployed, tested, and monitored through the BDA Cabinet framework
- **Declarative Infrastructure**: Supporting infrastructure managed declaratively (Kubernetes manifests, Tilt)
- **Defined Test Order**: Test execution strictly controlled by file sequence in [`CABINET.yaml`](./CABINET.yaml)
- **Tooling**: All tasks run via `uv` and `poe` (e.g., `uv run poe test`)
- **File Organization**: All BDD scenarios (`.feature`) and step definitions (`test_*.py`) in `features/` directory, prefixed by phase

## Prerequisites

Before you begin, ensure you have the following installed:

- [Tilt](https://docs.tilt.dev/) - Orchestration tool
- [Python](https://www.python.org/) - Programming language
- [uv](https://docs.astral.sh/uv/) - Python package manager
- A Kubernetes cluster:
  - Local options:
    - [Minikube](https://minikube.sigs.k8s.io/docs/)
    - [Kind](https://kind.sigs.k8s.io/)
    - [Docker Desktop with Kubernetes enabled](https://docs.docker.com/desktop/kubernetes/)
  - Or a remote cluster

For detailed setup requirements, refer to the [Setup and Critical Requirements documentation](./README_SETUP.md).

## Dependency Management

All Python dependencies are managed with [uv](https://docs.astral.sh/uv/).

| Task | Command |
|------|---------|
| Add package | `uv add <package>` |
| Add dev package | `uv add --dev <package>` |
| Remove package | `uv remove <package>` |
| Sync dependencies | `uv sync` |

**Important**: Do not use `pip` directly.

## Running the Application

- Start the application: `uv run poe start`
- Run tests: `uv run poe test`

## Infrastructure Management

- All Kubernetes/infrastructure operations are managed via Tilt
- Do not use `kubectl` directly
- Ensure Tilt is running in a dedicated terminal

## Testing

- Test execution order is strictly defined by the sequence in `CABINET.yaml`
- To add a new test file or change execution order:
  1. Modify the `tests:` list within `CABINET.yaml`
  2. The `features/conftest.py` file enforces this order during test runs
- Run tests using: `uv run poe test`

## Contributing

- Use [Conventional Commits](https://www.conventionalcommits.org/) for all commit messages
- Do not add features without corresponding acceptance tests
- Follow the fail-fast principle: do not hide errors or use silent fallbacks unless explicitly required

## Coding & Automation Conventions

All spelling in code, comments, documentation, and user-facing text must use Canadian English (e.g., "colour", "behaviour", "favour").

This project uses a unified ruleset for all AI agents and automation logic.

Rules are defined in the [AI Agent Guidelines documentation](./README_CONVENTIONS.md), which should be symlinked for agents like Cursor to interpret and enforce:

```bash
ln -s README_CONVENTIONS.md .cursor-rules
```

## Related Documentation

- [BDA Cabinet Framework](./README_BDA.md) - Detailed explanation of the BDA Cabinet framework, phases, and implementation details
- [Setup and Critical Requirements](./README_SETUP.md) - Setup prerequisites and critical requirements for using the BDA Cabinet
- [AI Agent Guidelines](./README_CONVENTIONS.md) - Guidelines for AI agents working with this project
