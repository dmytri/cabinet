import sys
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
import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("atdd_apply_container_dependencies.feature")

@given("the system is ready")
def _():
    pass  # Implement the setup for the system readiness

@when("python >= 3.12")
def _():
    assert sys.version_info >= (3, 12)

@when("uv >= 0.6.7")
def _():
    import uv
    assert uv.__version__ >= "0.6.7"

@when("pytest is ")
def _():
    import pytest
    assert pytest.__version__ is not None  # Check if pytest is installed

@when("poethepoet is ")
def _():
    import poethepoet
    assert poethepoet.__version__ is not None  # Check if poethepoet is installed

@then("python is supported version")
def _():
    assert sys.version_info >= (3, 12)

@then("uv is supported version")
def _():
    import uv
    assert uv.__version__ >= "0.6.7"

@then("only packages are present")
def _():
    import pkg_resources
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    required_packages = {"uv", "pytest", "poethepoet"}
    assert installed_packages == required_packages
