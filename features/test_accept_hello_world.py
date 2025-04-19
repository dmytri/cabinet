from pytest import skip
from pytest_bdd import scenarios, scenario, given, when, then

scenarios("accept_hello_world.feature")

@given("the target container is running")
def _():
    skip("not implemented")

@when("the user accesses the web server root via HTTP")
def _():
    skip("not implemented")

@then("the response status code should be 200")
def _():
    skip("not implemented")

@then("the response should contain the default Caddy welcome message")
def _():
    skip("not implemented")
