from pytest import skip
from pytest_bdd import scenarios, given, when, then

scenarios("monitor.feature")

@given("the Hello World application is deployed")
def _() -> None:
    skip("not implemented")

@when("health check endpoint is accessed")
def _() -> None:
    skip("not implemented")

@then("the response status code should be 200")
def _() -> None:
    skip("not implemented")

@then("the application reports as healthy")
def _() -> None:
    skip("not implemented")
