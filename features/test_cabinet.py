import sys
import subprocess
from packaging.version import parse as parse_version
from pytest_bdd import scenarios, scenario, when

scenarios("cabinet.feature")

@scenario("cabinet.feature", "Apply container has dependencies")
def _():
    pass

@when("python >= 3.12")
def _():
    assert sys.version_info >= (3, 12)

@when("uv >= 0.6.7")
def _():
    output = subprocess.check_output(["uv", "run", "uv", "--version"], text=True)
    # uv --version output is like: "uv 0.6.7"
    version_str = output.strip().split()[-1]
    installed_version = parse_version(version_str)
    required_version = parse_version("0.6.7")
    assert installed_version >= required_version

@when("pytest is required")
def _():
    output = subprocess.check_output(["uv", "pip", "show", "pytest"], text=True)
    assert "Name: pytest" in output

@when("poethepoet is required")
def _():
    output = subprocess.check_output(["uv", "pip", "show", "poethepoet"], text=True)
    assert "Name: poethepoet" in output

@when("pyinfra is required")
def _():
    output = subprocess.check_output(["uv", "pip", "show", "pyinfra"], text=True)
    assert "Name: pyinfra" in output
