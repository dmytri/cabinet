summary: >
  Defines Behaviour-Driven Automation phases for trick.ca/binet.
  Only BDA steps perform side effects. All others validate behaviour.

phases:

  cabinet:
    mutable: false
    definition: >
      Cabinet tests verify that the test infrastructure (e.g., Python, uv, Tilt) is ready before running BDA.
    file_prefix: cabinet_
    directory: features/
    rules:
      - Python test files must start with `test_cabinet_` and be in `features/`.
      - Cabinet scenarios must not perform provisioning or monitoring.

  bda:
    mutable: true
    definition: >
      Behaviour-Driven Automation (BDA) automates system configuration and dependencies using self-describing, scenario-based tests.
    structure: |
      Scenario: [infra behaviour]
        Given [precondition]
        When [requirement]
        Then [verification]
    file_prefix: bda_
    directory: features/
    rules:
      - Steps must be declarative and follow BDD conventions.
      - Tag scenarios with @dev, @ci, @stage, or @prod as needed.
      - Python test files must start with `test_bda_`.
      - Do not include @atdd in BDA scenarios.

  atdd:
    mutable: false
    definition: >
      Acceptance Test-Driven Development (ATDD) verifies that system behaviour meets expectations before or after implementation.
    structure: |
      Scenario: [expected behaviour]
        Given [precondition]
        When [action]
        Then [outcome]
    file_prefix: atdd_
    directory: features/
    rules:
      - All features must have ATDD scenarios and tests.
      - Python test files must start with `test_atdd_`.
      - Do not include @dev, @ci, or @prod tags in ATDD scenarios.

  bdm:
    mutable: false
    definition: >
      Behaviour-Driven Monitoring (BDM) continuously validates that system behaviour holds using declarative, synthetic checks.
    structure: |
      Scenario: [runtime behaviour]
        Given [expected state]
        When [condition]
        Then [assertion]
    file_prefix: bdm_
    directory: features/
    rules:
      - Python test files must start with `test_bdm_`.
      - BDM scenarios must be read-only and executable in live environments.

bdd_stubs:
  rules:
    - Every test file must include both `scenarios(...)` and individual `@scenario(...)` decorators.
    - Use `_` as the function name for all step definitions.
    - All step functions must call `skip("not implemented")`.

  example: |
    from pytest import skip
    from pytest_bdd import scenarios, scenario, given

    scenarios("feature_file.feature")
    scenario("feature_file.feature", "Scenario name")

    @given("step")
    def _():
        skip("not implemented")

test_ordering:
  rules:
    - Tests must be declared in CABINET.yml in desired execution order.
