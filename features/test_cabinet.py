import sys
import subprocess
from pytest import skip
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
    result = subprocess.run(["uv", "--version"], capture_output=True, text=True, check=True)
    version_str = result.stdout.split()[1]
    version_tuple = tuple(map(int, version_str.split('.')))
    assert version_tuple >= (0, 6, 7)

@when("pytest is required")
def _():
    try:
        import pytest
    except ImportError:
        assert False, "pytest is not installed"

@when("poethepoet is required")
def _():
    try:
        import poethepoet
    except ImportError:
        assert False, "poethepoet is not installed"

@when("httpx is required")
def _():
    try:
        import httpx
    except ImportError:
        assert False, "httpx is not installed"

@when("kubernetes is required")
def _():
    try:
        import kubernetes
    except ImportError:
        assert False, "kubernetes is not installed"

