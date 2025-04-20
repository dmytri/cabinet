Feature: Acceptance tests for Hello World site

  @accept
  Scenario: Hello World home site
    When the user accesses browser the hello world site
    Then the response status code should be 200
    And the response should contain "hello world"
