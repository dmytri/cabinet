from pytest import skip
from pytest_bdd import scenarios, scenario, given, when, then

# Corrected path: removed "features/" prefix
scenarios("monitor.feature")

# Corrected path: removed "features/" prefix
@scenario("monitor.feature", "Verify Hello World application is healthy")

@given("the Hello World application is deployed")
def _():
    skip("not implemented")

@when("health check endpoint is accessed")
def _():
    skip("not implemented")

@then("the response status code should be 200")
def _():
    skip("not implemented")

@then("the application reports as healthy")
def _():
    skip("not implemented")
