from pytest import skip
from pytest_bdd import scenarios, scenario, when

scenarios("atdd_apply_container_dependencies.feature")

@scenario("atdd_apply_container_dependencies.feature", "Apply container has dependencies")

@when("python >= 3.12")
def _():
    import sys
    assert sys.version_info >= (3, 12)

@when("uv >= 0.6.7")
def _():
    import subprocess
    output = subprocess.check_output(["uv", "--version"], text=True)
    version_str = output.strip().split()[0]
    version_tuple = tuple(int(x) for x in version_str.split("."))
    assert version_tuple >= (0, 6, 7)

@when("pytest is required")
def _():
    skip("not implemented")

@when("poethepoet is required")
def _():
    skip("not implemented")
