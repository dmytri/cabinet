from pytest_bdd import scenarios, scenario, given, when, then
from pytest import skip

scenarios("atdd_example.feature")

@scenario("atdd_example.feature", "Example acceptance test")
def _():
    skip("not implemented")

@given("the system is ready")
def _():
    skip("not implemented")

@when("the user does something")
def _():
    skip("not implemented")

@then("the expected result occurs")
def _():
    skip("not implemented")
