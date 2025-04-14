import sys
import subprocess
from packaging.version import parse as parse_version
from pytest_bdd import scenarios, scenario, when

scenarios("atdd_apply_container_dependencies.feature")

@scenario("atdd_apply_container_dependencies.feature", "Apply container has dependencies")
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

@when("dockerfile >= 3.4.0")
def _():
    output = subprocess.check_output(["uv", "pip", "show", "dockerfile"], text=True)
    version_line = next(line for line in output.splitlines() if line.startswith("Version:"))
    # Version line is like: "Version: 3.4.0"
    version_str = version_line.split(":", 1)[1].strip()
    installed_version = parse_version(version_str)
    required_version = parse_version("3.4.0")
    assert installed_version >= required_version
