from pytest_bdd import scenario, given, when, then
import pytest

@scenario("bda_stub.feature", "Stub BDA test to ensure CI passes")
def test_bda_stub():
    pytest.skip("not implemented")

@given("the system is initialized")
def system_initialized():
    pytest.skip("not implemented")

@when("no action is taken")
def no_action():
    pytest.skip("not implemented")

@then("the test passes")
def test_passes():
    pytest.skip("not implemented")
