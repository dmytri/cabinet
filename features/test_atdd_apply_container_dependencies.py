import sys
import subprocess
from pytest_bdd import scenarios, scenario, when

scenarios("atdd_apply_container_dependencies.feature")

@scenario("atdd_apply_container_dependencies.feature", "Apply container has dependencies")

@when("python >= 3.12")
def _():
    assert sys.version_info >= (3, 12)

@when("uv >= 0.6.7")
def _():
    output = subprocess.check_output(["uv", "run", "uv", "--version"], text=True)
    # uv --version output is like: "uv 0.6.7"
    version_str = output.strip().split()[-1]
    version_tuple = tuple(int(x) for x in version_str.split("."))
    assert version_tuple >= (0, 6, 7)

@when("pytest is required")
def _():
    output = subprocess.check_output(["uv", "pip", "show", "pytest"], text=True)
    assert "Name: pytest" in output

@when("poethepoet is required")
def _():
    output = subprocess.check_output(["uv", "pip", "show", "poethepoet"], text=True)
    assert "Name: poethepoet" in output
