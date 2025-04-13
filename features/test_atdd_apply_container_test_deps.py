from pytest_bdd import scenario, given, when, then
import pytest

@scenario("atdd_apply_container_test_deps.feature", "Apply container has Python, uv, and pytest installed")
def test_atdd_apply_container_test_deps():
    pytest.skip("not implemented")

@given("the apply container is running")
def apply_container_running():
    pytest.skip("not implemented")

@when("I check for Python, uv, and pytest")
def check_for_deps():
    pytest.skip("not implemented")

@then("all are installed and available")
def all_installed():
    pytest.skip("not implemented")
