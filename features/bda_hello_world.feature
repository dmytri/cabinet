Feature: Hello World Application Deployment

  @bda @dev @ci
  Scenario: Publish application image to GitHub Container Registry
    Given credentials for the GitHub Container Registry are available
    When the application Docker image is built
    And the image is pushed to the GitHub Container Registry
    Then the image is available in the registry
