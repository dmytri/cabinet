Feature: Acceptance tests for Hello World site

  @accept @monitor
  Scenario: Hello World home site
    Given the hello world URL
    When the user browses the hello world site
    Then the response status code should be 200
    And the response should contain "hello world"
