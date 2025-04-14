# === <code> ===
code:
  style:
    - Fail fast: do not hide errors
    - No try blocks, guards, or silent fallbacks unless asked
    - No external dependencies unless instructed
    - Use standard library and simple constructs
    - No inline comments — code must be self-explanatory
    - Only perform the exact task stated — no unsolicited edits, enhancements, fixes, refactors, comments, or formatting changes.
    - Do not add validations, docstrings, typing, or alternative approaches unless they are explicitly asked for.
    - Do not modify unrelated code, even if it appears broken or suboptimal.
    - If the request is ambiguous, ask for clarification — do not assume or guess.
    - Do not suggest or make any code changes in response to test output unless the user explicitly requests a fix or modification.
# === </code> ===

# === <setup> ===
setup:
  prerequisites:
    - Tilt
    - A Kubernetes cluster (local, e.g., Minikube, Kind, or Docker Desktop with Kubernetes enabled, or remote)
    - Python
    - uv
  test_environment: >
    All test steps run in the Apply container as a Kubernetes job.
# === </setup> ===

# === <local_setup> ===
critical:
  must:
    - Host must already have Tilt, Minikube, Python, and uv installed
    - All app dependencies must be defined and provisioned by BDA in the target environment
    - All exposed ports must be defined in manifest.yml and forwarded in Tiltfile
  must_not:
    - Install Python packages outside the dependency system
    - Bypass Tilt for Kubernetes operations
# === </local_setup> ===

# === <language> ===
language:
  spelling: >
    Always use Canadian English spelling in all code, comments, documentation, and user-facing text.
    Examples: "colour" not "color", "favour" not "favor", "organize" not "organise", "behaviour" not "behavior".
# === </language> ===
