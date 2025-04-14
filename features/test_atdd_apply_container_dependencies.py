
from pytest import skip
from pytest_bdd import scenario, given, when, then

@scenario("atdd_apply_container_dependencies.feature", "Apply container has dependencies")
def _():
    skip("not implemented")

@when("python >= 3.12")
def _():
    pass

@when("uv >= 0.6.7")
def _():
    pass

@when("pytest is required")
def _():
    pass

@when("poethepoet is required")
def _():
    pass
