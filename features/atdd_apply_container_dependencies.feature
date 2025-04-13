@atdd
Feature: Apply container test dependencies

  Scenario: Apply container has dependencies
    When python >= 3.12 is required
     and uv is required
     and pytest is required
     and poethepoet is optional
    Then python is supported version
     and only required or optional packages are present
