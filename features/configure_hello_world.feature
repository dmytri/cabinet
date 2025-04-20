Feature: Deploy and configure Hello World application

  @dev @ci
  Scenario: Hello World Container is Built and Deployed by Tilt
    Given Kubernetes API Connection
    Then The Hello World Container is running

  @stage @prod
  Scenario: Publish Image to GitHub Container Registry
    Given Credentials for the GitHub Container Registry are available
      And Kaniko build image is present
     When Application Docker image is built
      And Image is pushed to the GitHub Container Registry
     Then Image is available in the registry

  @stage @prod
  Scenario: Proxy /hello requests to a dedicated Bunny pull zone
    Given Bunny API key is available
      And "asym.me" domain is served by a Bunny pull zone
     When A Bunny Magic Container running Hello World image
      And DNS CNAME record added from "hello.cdn.asym.me" to the Bunny Magic Container
      And Bunny pull zone "hello" created with origin "hello.cdn.asym.me"
      And Custom hostname "hello.cdn.asym.me" to the pull zone
      And TLS for the custom hostname "hello.cdn.asym.me"
      And Edge Rule added on the "asym.me" pull zone to forward "/hello" to "https://hello.cdn.asym.me"
     Then Requests to "asym.me/hello" are served via the "hello" pull zone origin
