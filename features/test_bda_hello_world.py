from pytest_bdd import scenarios, scenario, given, when, then
from pytest import skip

scenarios("bda_hello_world.feature")

@scenario("bda_hello_world.feature", "Stub BDA test to ensure CI passes")

@given("the system is initialized")
def _():
    skip("not implemented")

@when("no action is taken")
def _():
    skip("not implemented")

@then("the test passes")
def _():
    skip("not implemented")
