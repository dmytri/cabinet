# === <prompt> ===
prompt: >
  You are a coding assistant. Follow all rules below when generating or editing code.
  Follow these conventions for code development, testing, and infrastructure.
# === </prompt> ===

# === <commit> ===
commit:
  format: Conventional Commits
  reference: https://www.conventionalcommits.org/
# === </commit> ===

# === <python> ===
python:
  dependency_management: uv
  enforce_pyproject: true
  pip_disallowed: true
  scripts_must_use_poe: true
  run_script: "uv run poe <task>"
  run_start: "uv run poe start"
  run_dev: "uv run poe dev"
  example_commands:
    - uv add httpx
    - uv add --dev pytest
    - uv add --group test pytest-cov
    - uv remove httpx
    - uv pip sync
  reference: https://docs.astral.sh/uv/concepts/projects/dependencies/
# === </python> ===

# === <infra> ===
infra:
  tilt_only: true
  kubectl_disallowed: true
  assumption: "Tilt is running in a dedicated terminal, never use Tilt cli"
# === </infra> ===

# === <bda> ===
bda:
  definition: >
    Behavior-Driven Automation is a self-describing and self-testing approach to automating system configuration and dependencies.
  structure: |
    Scenario: [infra behaviour]
      Given [precondition]
       When [requirement]
       Then [verification]
  rules:
    - Use BDD conventions; steps are declarative.
    - Tags: eg @dev, @ci, @stage, @prod required.
    - All configuration and dependencies must be covered by BDA.
    - All BDA steps must be in tests/ with no subdirectories.
    - Filenames must start with bda_ and clearly describe the covered behavior.
# === </bda> ===

# === <atdd> ===
atdd:
  definition: >
    Acceptance Test-Driven Development uses natural language scenarios to define and validate system behavior before implementation.
  structure: |
    Scenario: [behaviour]
      Given [preconditions]
       When [action]
       Then [outcome]
  rules:
    - All features must be covered by ATDD scenarios.
    - Never add a feature not covered by ATDD and backed by pytest tests.
    - All ATDD steps must be in tests/ with no subdirectories.
    - Filenames must start with atdd_ and clearly describe the feature.
    - Must not include BDA tags (@dev, @ci, @prod).
# === </atdd> ===

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
# === </code> ===

# === <setup> ===
setup:
  prerequisites:
    - Tilt
    - Minikube
    - Python
    - uv
  test_environment: >
    All test steps run in the Apply container as a Kubernetes job.
# === </setup> ===

# === <critical> ===
critical:
  must:
    - Host must already have Tilt, Minikube, Python, and uv installed
    - All test dependencies must be in Apply container
    - All app dependencies must be defined and provisioned by BDA in the target environment
    - All exposed ports must be defined in manifest.yml and forwarded in Tiltfile
  must_not:
    - Modify host beyond permitted dependencies
    - Install Python packages outside the dependency system
    - Bypass Tilt for Kubernetes operations
# === </critical> ===

# === <prompt_examples> ===
prompts:
  - input: Generate a BDA scenario for adding a Redis service
    context: Use a file named bda_add_redis.feature in the tests/ directory
  - input: Add an ATDD scenario for user registration
    context: Use a file named atdd_user_registration.feature with Given/When/Then steps
# === </prompt_examples> ===

# === <bdd_stubs> ===
bdd_stubs:
  rule: >
    Whenever a new BDA or ATDD scenario is added in a .feature file,
    corresponding Python step definitions must be created in the tests/ directory.
    Each Given/When/Then step in the feature file must have a matching Python function
    decorated with @given, @when, or @then from pytest-bdd, even if the function body is a stub.
    The test function decorated with @scenario should also be marked as skipped with pytest.skip("not implemented").
    This ensures that all scenarios are discoverable and runnable by pytest-bdd, and that unimplemented steps are clearly indicated.

  example: |
    from pytest_bdd import scenario, given, when, then
    import pytest

    @scenario("bda_example.feature", "Example scenario")
    def test_bda_example():
        pytest.skip("not implemented")

    @given("some precondition")
    def some_precondition():
        pytest.skip("not implemented")

    @when("an action occurs")
    def an_action_occurs():
        pytest.skip("not implemented")

    @then("an outcome is verified")
    def an_outcome_is_verified():
        pytest.skip("not implemented")
# === </bdd_stubs> ===

# === <test_ordering> ===
test_ordering:
  rules:
    - Any new pytest test file must be added to the TESTS list in tests/conftest.py for it to be collected and run.
    - All ATDD tests (files starting with atdd_) must always be listed after all BDA tests (files starting with bda_) in the TESTS list, so that BDA tests run first.
# === </test_ordering> ===

