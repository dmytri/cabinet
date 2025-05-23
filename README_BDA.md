# BDA Cabinet: Behaviour-Driven Automation Framework

## Flow: ready → configure → accept → monitor

## Summary
A **BDA Cabinet** orchestrates the deployment, testing, and monitoring of
your target application via Behavior‑Driven Automation

## Glossary
- **BDA**: Behaviour Driven Automation. Self-describing and self-testing automation using Gherkin Scenarios
- **Target Application**: The software deployed, tested, and monitored via the BDA Cabinet
- **Apply Container**: Tilt-managed container executing all BDD scenarios
- **Ready Phase**: Ensure the apply container has necessary dependencies
- **Configure Phase**: Provision and configure target application infrastructure declaratively
- **Accept Phase**: Conduct acceptance tests for user-visible behaviour
- **Monitor Phase**: Validate live runtime behaviour with read-only checks

## Execution Model
- **Runtime Environment**: All scenarios run within the Tilt apply container
- **Execution Engine**: pytest automatically executes all phases in sequence
- **Execution Order**: Phases are executed in the order defined in CABINET.yaml
- **Output Handling**: Standard pytest output is generated and logs are captured by Tilt
- **Error Handling**: Standard pytest error reporting is used

## Tilt Integration
Tilt is responsible for:
- Building the apply container with all dependencies
- Applying the Kubernetes job manifest for the apply container
- Capturing and storing logs from test execution in apply container

## Phases

### 1. ready
- **Purpose**: Verify that the Tilt apply container has all required dependencies
- **Files**:
  - Feature file: `ready.feature` under `features/`
  - Test file: `test_ready.py` under `features/`
- **Tags**: [@accept]
- **Rules**:
  - There must be exactly one `ready.feature` and one `test_ready.py` under `features/`
  - Scenarios MUST only perform checks—no provisioning or side-effects

### 2. configure
- **Purpose**: Declaratively provision and configure system infrastructure via BDA
- These tests are declations, the implement and verify the requirements
- These tests have side effects, but must be stateless and idempotent
- **Files**:
  - Feature files: `configure_<feature>.feature` under `features/`
  - Test files: `test_configure_<feature>.py` under `features/`
- **Tags**: [@dev, @ci, @stage, @prod] (at least one required)
- **Rules**:
  - Use BDD conventions:
      Given [precondition]
      When [declaration of desired state]
      Then [verification]
  - Scenarios must include **one or more** of `@dev`, `@ci`, `@stage`, `@prod`
  - DO NOT include `@accept` here

### 3. accept
- **Purpose**: Run acceptance tests to confirm user-visible behaviour
- **Environment**: Tests must be environment-agnostic and run unmodified across all environments
- **Files**:
  - Feature files: `accept_<feature>.feature` under `features/`
  - Test files: `test_accept_<feature>.py` under `features/`
- **Tags**: [@accept]
- **Rules**:
  - Scenarios must include `@accept`. They may *optionally* also include `@monitor` if they perform read-only checks suitable for continuous monitoring.
  - DO NOT include any of `@dev`, `@ci`, `@stage`, `@prod` tags here

### 4. monitor
- **Purpose**: Continuously validate live runtime behaviour with read-only checks.
  This phase is optional. Monitoring checks can alternatively be included in the `accept` phase by adding the `@monitor` tag to relevant `@accept` scenarios.
- **Files**:
  - Feature file: `monitor.feature` under `features/`
  - Test file: `test_monitor.py` under `features/`
- **Tags**: [@monitor]
- **Rules**:
  - If this phase is used, scenarios must *only* use the `@monitor` tag.
  - There must be exactly one `monitor.feature` and one `test_monitor.py` under `features/` *if this phase is implemented*.
  - Scenarios are checks against live systems
  - No side-effects permitted

## Implementation Details

### BDD Stubs
- **Directory**: features/
- **Rules**:
  - Every test file must include `scenarios("...")` to load tests from the corresponding feature file
  - All step definition functions (`@given`, `@when`, `@then`) must use the name `_`
  - Stubs should call `skip("not implemented")`
- **Example**:
  ```python
  from pytest import skip
  from pytest_bdd import scenarios, given, when

  # Path is RELATIVE to the features/ directory, so just the filename.
  # This call generates the tests based on the feature file scenarios.
  scenarios("ready.feature")

  # No separate @scenario decorator or placeholder function needed here.

  # Step definitions implement the steps from the feature file.
  # ALL step functions must be named _
  @given("Some precondition")
  def _(): # Implemented step
      # ... implementation code ...
      pass

  @when("Some action occurs")
  def _(): # Step definition stub
      skip("not implemented")
  ```

### CABINET.yaml Example
```yaml
cabinet: >
  example bda cabinet

tests:
  - path: test_ready.py
    phase: ready
    feature: features/ready.feature
    description: "Verify dependencies in apply container"

  - path: test_configure_webapp.py
    phase: configure
    feature: features/configure_webapp.feature
    description: "Deploy and configure web application"

  - path: test_accept_webapp.py
    phase: accept
    feature: features/accept_webapp.feature
    description: "Validate web application functionality"

  - path: test_monitor.py
    phase: monitor
    feature: features/monitor.feature
    description: "Monitor web application health"
```

pytest automatically executes all phases in the exact order specified in this file.

## Maintenance and Alignment

### ALIGN prompt
When I ask to "Align" the features, ensure:

Details:
1.  **`CABINET.yaml`:** Entries complete (`path`, `phase`, `feature`, `description`)
2.  **Tags**:
    - `ready`: Only `@accept`
    - `configure`: 1+ of `@dev`/`@ci`/`@stage`/`@prod` (single tag OK)
    - `accept`: Must include `@accept`; may optionally include `@monitor`. No other tags allowed.
    - `monitor`: Optional phase. If present, must *only* use `@monitor`.
3.  **Test Files**:
    - Correct `scenarios()` usage
    - No extra decorators
    - All steps implemented or skipped
4.  **Output:** Summarise only required changes

**Strictly enforce**:
   - Tags per phase (single @ci is valid for configure)
   - features match CABINET.yaml
**Never**:
   - Add/remove steps or files unless missing
   - Modify formatting, imports, or comments
   - Change implemented logic
**Only edit if**:
   - A rule is *directly* violated
   - The fix is *unambiguous*

