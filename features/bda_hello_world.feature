Feature: BDA | Hello World Application Deployment

  Scenario: Publish Image to GitHub Container Registry
    Given Credentials for the GitHub Container Registry are available
     When Application Docker image is built
      And Image is pushed to the GitHub Container Registry
     Then Image is available in the registry

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

