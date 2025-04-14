from pytest_bdd import scenarios, when
import sys

scenarios("atdd_apply_container_dependencies.feature")

@when("python >= 3.12")
def _():
    assert sys.version_info >= (3, 12), "Python version must be 3.12 or higher"
