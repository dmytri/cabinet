from pytest_bdd import scenario, given, when, then
import pytest

@scenario("atdd_example.feature", "Example acceptance test")
def test_atdd_example():
    pytest.skip("not implemented")

@given("the system is ready")
def system_ready():
    pytest.skip("not implemented")

@when("the user does something")
def user_does_something():
    pytest.skip("not implemented")

@then("the expected result occurs")
def expected_result_occurs():
    pytest.skip("not implemented")
