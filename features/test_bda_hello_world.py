from pytest import skip
from pytest_bdd import scenarios, scenario, given, when, then

scenarios("bda_hello_world.feature")

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

