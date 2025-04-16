from pytest import skip
from pytest_bdd import scenarios, scenario, given, when, then

scenarios("bda_hello_world.feature")

# Scenario: Publish Image to GitHub Container Registry
@scenario("bda_hello_world.feature", "Publish Image to GitHub Container Registry")
def test_publish_image():
    pass

@given("Credentials for the GitHub Container Registry are available")
def _():
    skip("not implemented")

@when("Application Docker image is built")
def _():
    skip("not implemented")

@when("Image is pushed to the GitHub Container Registry")
def _():
    skip("not implemented")

@then("Image is available in the registry")
def _():
    skip("not implemented")


# Scenario: Proxy /hello requests to a dedicated Bunny pull zone
@scenario("bda_hello_world.feature", "Proxy /hello requests to a dedicated Bunny pull zone")
def test_proxy_hello_requests():
    pass

@given("Bunny API key is available")
def _():
    skip("not implemented")

@given('"asym.me" domain is served by a Bunny pull zone')
def _():
    skip("not implemented")

@when("A Bunny Magic Container running Hello World image")
def _():
    skip("not implemented")

@when('DNS CNAME record added from "hello.cdn.asym.me" to the Bunny Magic Container')
def _():
    skip("not implemented")

@when('Bunny pull zone "hello" created with origin "hello.cdn.asym.me"')
def _():
    skip("not implemented")

@when('Custom hostname "hello.cdn.asym.me" to the pull zone')
def _():
    skip("not implemented")

@when('TLS for the custom hostname "hello.cdn.asym.me"')
def _():
    skip("not implemented")

@when('Edge Rule added on the "asym.me" pull zone to forward "/hello" to "https://hello.cdn.asym.me"')
def _():
    skip("not implemented")

@then('Requests to "asym.me/hello" are served via the "hello" pull zone origin')
def _():
    skip("not implemented")
