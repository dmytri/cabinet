import pytest
import sys
import subprocess
from pytest import skip
from pytest_bdd import scenarios, given, when, then

@scenarios("atdd_apply_container_dependencies.feature")
def _():
    pass

@when("python >= 3.12")
def _():
    assert sys.version_info >= (3, 12), "Python version must be 3.12 or greater"

@when("uv >= 0.6.7")
def _():
    try:
        result = subprocess.run(["uv", "--version"], capture_output=True, text=True, check=True)
        uv_version = result.stdout.strip()
        uv_version = tuple(map(int, uv_version.split(".")))
        assert uv_version >= (0, 6, 7), f"uv version must be >= 0.6.7, but is {uv_version}"
    except FileNotFoundError:
        pytest.fail("uv is not installed")
    except Exception as e:
        pytest.fail(f"Failed to check uv version: {e}")

@when("pytest is required")
def _():
    skip("not implemented")

@when("poethepoet is required")
def _():
    skip("not implemented")
