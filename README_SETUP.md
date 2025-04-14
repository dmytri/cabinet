setup:
  prerequisites:
    - Tilt
    - A Kubernetes cluster (local, e.g., Minikube, Kind, or Docker Desktop with Kubernetes enabled, or remote)
    - Python
    - uv
  test_environment: >
    All test steps run in the Apply container as a Kubernetes job.

critical:
  must:
    - Host must already have Tilt, Minikube, Python, and uv installed
    - All app dependencies must be defined and provisioned by BDA in the target environment
    - All exposed ports must be defined in manifest.yml and forwarded in Tiltfile
  must_not:
    - Install Python packages outside the dependency system
    - Bypass Tilt for Kubernetes operations
