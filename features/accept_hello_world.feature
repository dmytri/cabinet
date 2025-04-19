Feature: Acceptance tests for Hello World site

  @accept
  Scenario: Accessing the default Caddy site
    Given the target container is running
    When the user accesses the web server root via HTTP
    Then the response status code should be 200
    And the response should contain the default Caddy welcome message
