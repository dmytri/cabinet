from pytest_bdd import scenario, given, when, then
import pytest
import subprocess
import json

_installed_packages = set()
_required_packages = set()

@scenario("atdd_apply_container_test_deps.feature", "Apply container has Python, uv, and pytest installed")
def _():
    pass

@given("the apply container is running")
def _():
    pass

@when("I check for Python, uv, and pytest")
def _():
    result = subprocess.run(
        ["uv", "pip", "list", "--format", "json"],
        capture_output=True,
        text=True,
        check=True
    )
    installed = {pkg["name"].lower() for pkg in json.loads(result.stdout)}
    required = {"python", "uv", "pytest"}
    _installed_packages.clear()
    _installed_packages.update(installed)
    _required_packages.clear()
    _required_packages.update(required)

@then("all are installed and available")
def _():
    missing = _required_packages - _installed_packages
    assert not missing, f"Missing required packages: {missing}"
