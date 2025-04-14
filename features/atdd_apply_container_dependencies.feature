Feature: Apply container test dependencies

  @atdd
  Scenario: Apply container has dependencies
    When python >= 3.12 is required
     And uv is required
     And pytest is required
     And poethepoet is optional
    Then python is supported version
     And only required or optional packages are present
