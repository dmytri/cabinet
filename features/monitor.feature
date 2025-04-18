Feature: Monitor | Hello World Application Health

  @monitor
  Scenario: Verify Hello World application is healthy
    Given the Hello World application is deployed
    When health check endpoint is accessed
    Then the response status code should be 200
    And the application reports as healthy
