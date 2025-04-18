# BDA Cabinet: Setup and Critical Requirements

## Summary
This document outlines the setup prerequisites and critical requirements for
using the BDA Cabinet framework. It defines the necessary environment setup and
important constraints that must be followed when working with the
Behaviour-Driven Automation system.

## Setup Prerequisites

### Required Components
- **Tilt**: Orchestration tool for managing the development environment
- **Kubernetes Cluster**: Local or remote cluster for running the Apply container
  - Local options: Minikube, Kind, or Docker Desktop with Kubernetes enabled
  - Remote option: Any Kubernetes-compatible cluster
- **Python**: Required for running BDD tests and scenarios
- **uv**: Python package management tool

### Test Environment
All test steps run in the Apply container as a Kubernetes job.

The Apply container is the Tilt-managed environment where all BDD scenarios are
executed, consistent with the BDA Cabinet execution model.

## Critical Requirements

### Must Requirements
- **Host Prerequisites**: Host machine must already have Tilt, Minikube, Python, and uv installed
- **Dependency Management**: All application dependencies must be defined and provisioned by BDA in the target environment
- **Port Configuration**: All exposed ports must be defined in manifest.yml and forwarded in Tiltfile

### Must Not Requirements
- **Package Installation**: Do not install Python packages outside the dependency system
- **Kubernetes Operations**: Do not bypass Tilt for Kubernetes operations

## Relationship to BDA Cabinet

The BDA Cabinet framework relies on this setup to provide the environment where
the four phases (ready, configure, accept, monitor) are executed.

The Apply container referenced in the BDA Cabinet documentation is created and
managed according to the requirements specified in this document.

## Implementation Example

### Tiltfile Example
```python
# Example Tiltfile showing port forwarding configuration
docker_build('apply', '.')
k8s_yaml('manifest.yaml')
k8s_resource('apply', auto_init=False, trigger_mode=TRIGGER_MODE_MANUAL)
```
All setup and configuration must adhere to these requirements to ensure proper
functioning of the BDA Cabinet framework.
