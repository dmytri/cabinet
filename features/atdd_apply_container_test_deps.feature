@atdd
Feature: Apply container test dependencies

  Scenario: Apply container has Python, uv, and pytest installed
    Given the apply container is running
    When I check for Python, uv, and pytest
    Then all are installed and available
