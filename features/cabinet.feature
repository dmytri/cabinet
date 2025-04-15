Feature: Apply container test dependencies

  @atdd
  Scenario: Apply container has dependencies
    When python >= 3.12
     And uv >= 0.6.7
     And pytest is required
     And poethepoet is required
     And httpx is required
