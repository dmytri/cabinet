from pytest_bdd import scenario, given, when, then
import pytest

@scenario("atdd_apply_container_dependencies.feature", "Apply container has dependencies")
def _():
    pytest.skip("not implemented")

@when("python >= 3.12 is required")
def _():
    pytest.skip("not implemented")

@when("uv is required")
def _():
    pytest.skip("not implemented")

@when("pytest is required")
def _():
    pytest.skip("not implemented")

@when("poethepoet is optional")
def _():
    pytest.skip("not implemented")

@then("python is supported version")
def _():
    pytest.skip("not implemented")

@then("only required or optional packages are present")
def _():
    pytest.skip("not implemented")
