from pytest import skip
from pytest_bdd import scenarios, scenario, given, when, then

scenarios("bda_hello_world.feature")

@scenario("bda_hello_world.feature", "Publish application image to GitHub Container Registry")
def test_publish_image():
    pass

@given("credentials for the GitHub Container Registry are available")
def _():
    skip("not implemented")

@when("the application Docker image is built")
def _():
    skip("not implemented")

@when("the image is pushed to the GitHub Container Registry")
def _():
    skip("not implemented")

@then("the image is available in the registry")
def _():
    skip("not implemented")
