from pytest_bdd import scenarios, scenario, given, when, then
from pytest import skip

scenarios("atdd_apply_container_dependencies.feature")

@scenario("atdd_apply_container_dependencies.feature", "Apply container has dependencies")
def _():
    skip("not implemented")

@given("the apply container is running")
def _():
    skip("not implemented")

@when("python >= 3.12 is required")
def _():
    skip("not implemented")

@when("uv is required")
def _():
    skip("not implemented")

@when("is required")
def _():
    skip("not implemented")

@when("poethepoet is optional")
def _():
    skip("not implemented")

@then("python is supported version")
def _():
    skip("not implemented")

@then("only required or optional packages are present")
def _():
    skip("not implemented")
