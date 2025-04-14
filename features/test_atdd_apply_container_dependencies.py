from pytest import skip
from pytest_bdd import scenario, when, then

@scenario("atdd_apply_container_dependencies.feature", "Apply container has dependencies")

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
