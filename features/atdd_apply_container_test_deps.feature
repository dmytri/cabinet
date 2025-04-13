@atdd
Feature: Apply container test dependencies

  Scenario: Apply container has Python, uv, and pytest installed
    When python >= 3.12 is installed
    and uv is installed
    and pytest is installed
    and poethepoet is optional
    Then no other packages are installed
    Then all are installed and available
