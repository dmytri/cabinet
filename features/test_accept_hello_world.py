from pytest import skip
from pytest_bdd import scenarios, given, when, then

scenarios("accept_hello_world.feature")

@given("the target container is running")
def _() -> None:
    skip("not implemented")

@when("the user accesses browser the hello world site")
def _() -> None:
    skip("not implemented")

@then("the response status code should be 200")
def _() -> None:
    skip("not implemented")

@then("the response should contain the default Caddy welcome message")
def _() -> None:
    skip("not implemented")
