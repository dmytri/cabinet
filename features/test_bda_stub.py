from pytest_bdd import scenario, given, when, then
import pytest

@scenario("bda_stub.feature", "Stub BDA test to ensure CI passes")
def test_bda_stub():
    pytest.skip("not implemented")

@given("the system is initialized")
def _():
    pytest.skip("not implemented")

@when("no action is taken")
def _():
    pytest.skip("not implemented")

@then("the test passes")
def _():
    pytest.skip("not implemented")
