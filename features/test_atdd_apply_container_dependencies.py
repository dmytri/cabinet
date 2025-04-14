from pytest_bdd import scenarios, when
import sys

scenarios("atdd_apply_container_dependencies.feature")

from pytest import skip

@given("pytest is required")
def _():
    skip("not implemented")

@given("poethepoet is required")
def _():
    skip("not implemented")
