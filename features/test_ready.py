import sys
import subprocess
from pytest_bdd import scenarios, scenario, when

scenarios("features/ready.feature")

@scenario("features/ready.feature", "Verify dependencies in apply container")
def test_dependencies_present():
    pass

@when("python >= 3.12")
def _():
    assert sys.version_info >= (3, 12)

@when("uv >= 0.6.7")
def _():
    result = subprocess.run(["uv", "--version"], capture_output=True, text=True, check=True)
    version_str = result.stdout.split()[1]
    version_tuple = tuple(map(int, version_str.split('.')))
    assert version_tuple >= (0, 6, 7)

@when("pytest-bdd is required")
def _():
    result = subprocess.run(["uv", "pip", "show", "pytest-bdd"], capture_output=True, text=True)
    assert "Name: pytest-bdd" in result.stdout, "pytest-bdd is not installed"

@when("poethepoet is required")
def _():
    result = subprocess.run(["uv", "pip", "show", "poethepoet"], capture_output=True, text=True)
    assert "Name: poethepoet" in result.stdout, "poethepoet is not installed"

@when("httpx is required")
def _():
    result = subprocess.run(["uv", "pip", "show", "httpx"], capture_output=True, text=True)
    assert "Name: httpx" in result.stdout, "httpx is not installed"

@when("kubernetes is required")
def _():
    result = subprocess.run(["uv", "pip", "show", "kubernetes"], capture_output=True, text=True)
    assert "Name: kubernetes" in result.stdout, "kubernetes is not installed"
