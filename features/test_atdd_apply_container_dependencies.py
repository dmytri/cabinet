from pytest import skip
from pytest_bdd import scenarios, when, then

scenarios("atdd_apply_container_dependencies.feature")

@when("python >= 3.12")
def _():
    skip("not implemented")

@when("uv >= 0.6.7")
def _():
    skip("not implemented")

@when("pytest is ")
def _():
    skip("not implemented")

@when("poethepoet is ")
def _():
    skip("not implemented")

@then("python is supported version")
def _():
    skip("not implemented")

@then("uv is supported version")
def _():
    skip("not implemented")

@then("only  packages are present")
def _():
    skip("not implemented")
