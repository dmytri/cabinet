from pytest import skip
from pytest_bdd import scenarios, scenario, given, when, then

@scenarios("atdd_hello_world_site.feature")

@scenario("atdd_hello_world_site.feature", "Accessing the default Caddy site")

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

