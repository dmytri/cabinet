from pytest import skip
from pytest_bdd import scenarios, scenario, when

scenarios("atdd_apply_container_dependencies.feature")

@scenario("atdd_apply_container_dependencies.feature", "Apply container has dependencies")

@when("python >= 3.12")
def _():
    skip("not implemented")

@when("uv >= 0.6.7")
def _():
    skip("not implemented")

@when("pytest is required")
def _():
    skip("not implemented")

@when("poethepoet is required")
def _():
    skip("not implemented")
