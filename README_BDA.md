bda:
  definition: >
    Behaviour-Driven Automation (BDA) is a self-describing and self-testing approach to automating system configuration and dependencies.
  structure: |
    Scenario: [infra behaviour]
      Given [precondition]
      When [requirement]
      Then [verification]
  rules:
    - Use BDD conventions; steps must be declarative.
    - Include tags such as @dev, @ci, @stage, @prod as required.
    - Ensure all configuration and dependencies are covered by BDA.
    - Store all BDA feature files in the `features/` directory without subdirectories.
    - Name all Python test files for BDA with the prefix `test_bda_` (e.g., `test_bda_stub.py`) and place them in the `features/` directory without subdirectories to comply with pytest conventions.
    - Start BDA feature filenames with `bda_` and ensure they clearly describe the covered behaviour.
    - Do not include the @atdd tag in BDA scenarios.

atdd
  definition: >
    Acceptance Test-Driven Development uses natural language scenarios to define and validate system behaviour before implementation.
  structure: |
    Scenario: [behaviour]
      Given [preconditions]
       When [action]
       Then [outcome]
  rules:
    - All features must be covered by ATDD scenarios.
    - Never add a feature not covered by ATDD and backed by pytest tests.
    - All ATDD feature files must be in features/ with no subdirectories.
    - ATDD feature filenames must start with atdd_ and clearly describe the feature.
    - All Python test files for ATDD must be in features/ with no subdirectories and must start with test_atdd_ (e.g., test_atdd_login.py) to comply with pytest conventions.
    - Must not include BDA tags (@dev, @ci, @prod).

prompts:
  - input: Generate a BDA scenario for adding a Redis service
    context: Use a file named bda_add_redis.feature in the tests/ directory
  - input: Add an ATDD scenario for user registration
    context: Use a file named atdd_user_registration.feature with Given/When/Then steps

bdd_stubs:
  rules:
    - **MANDATORY:** Every pytest-bdd test file must include BOTH an `@scenarios("feature_file.feature")` decorator at the top AND an individual `@scenario("feature_file.feature", "Scenario name")` decorator for each scenario. This applies even if there is only one scenario in the feature file.
    - Each pytest-bdd test file must start with an @scenarios decorator referencing its feature file.
    - Each pytest-bdd test file must also include an @scenario decorator for each scenario in the feature file, but neither @scenarios nor @scenario should be followed by a function definition.
    - Each Given/When/Then step in the feature file must have a matching Python function decorated with @given, @when, or @then from pytest-bdd, named _ (underscore).
    - All Python functions decorated with @given, @when, or @then for BDA or ATDD scenarios must call skip("not implemented") in their body (import skip from pytest at the top).
    - This ensures that all scenarios are discoverable and runnable by pytest-bdd, and that unimplemented steps are clearly indicated.
  rationale: |
    Including BOTH `@scenarios` and individual `@scenario` decorators ensures:
      - All scenarios are auto-discovered and listed by pytest-bdd.
      - Consistency and future-proofing as more scenarios are added.
      - No scenario is missed due to omission or copy-paste errors.
  checklist: |
    - [ ] File includes `@scenarios("feature_file.feature")`
    - [ ] File includes `@scenario(...)` for each scenario
    - [ ] No function body after `@scenarios` or `@scenario`
    - [ ] All step functions call `skip("not implemented")`
  warning: |
    **Warning:** Omitting `@scenarios` will result in incomplete test discovery and is a violation of project conventions.
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
    - Any new pytest test file must be added to the TESTS list in tests/conftest.py for it to be collected and run.
    - All ATDD tests (files starting with atdd_) must always be listed after all BDA tests (files starting with bda_) in the TESTS list, so that BDA tests run first.
