from pytest_bdd import scenarios, when, then
from pytest import fixture
import subprocess
import json

scenarios("atdd_apply_container_dependencies.feature")

@fixture
def required():
    return []

@when("python >= 3.12")
def _(required):
    result = subprocess.run(
        ["uv", "run", "python", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    version_line = result.stdout.strip() or result.stderr.strip()
    assert (
        version_line.lower().startswith("python ") and
        tuple(map(int, version_line.split(" ")[1].split(".")[:2])) >= (3, 12)
    ), "Python version is less than 3.12 or could not be determined"
    required.append("python")

@when("uv is >= 0.6.7")
def _(required):
    result = subprocess.run(
        ["uv", "run", "uv", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    version_line = result.stdout.strip() or result.stderr.strip()
    parts = version_line.split()
    if len(parts) < 2:
        raise AssertionError(f"Unexpected uv version output: {version_line}")
    version = parts[1]
    major, minor, patch = (int(x) for x in version.split("."))
    if (major, minor, patch) < (0, 6, 7):
        raise AssertionError(f"uv version {version} is less than 0.6.7")
    required.append("uv")

@when("pytest is required")
def _(required):
    result = subprocess.run(
        ["uv", "run", "pytest", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    if result.returncode != 0:
        raise AssertionError("pytest is not available in the container")
    required.append("pytest")

@when("poethepoet is required")
def _(required):
    result = subprocess.run(
        ["uv", "run", "poe", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    if result.returncode != 0:
        raise AssertionError("poethepoet is not available in the container")
    required.append("poethepoet")

@then("python is supported version")
def _(required):
    result = subprocess.run(
        ["uv", "run", "python", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    version_line = result.stdout.strip() or result.stderr.strip()
    if not version_line.lower().startswith("python "):
        raise AssertionError("Could not determine Python version from uv")
    version = version_line.split(" ")[1]
    major, minor, *_ = (int(x) for x in version.split("."))
    if (major, minor) < (3, 12):
        raise AssertionError(f"Python version {version} is less than 3.12")

@then("uv is supported version")
def _(required):
    result = subprocess.run(
        ["uv", "run", "uv", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    version_line = result.stdout.strip() or result.stderr.strip()
    parts = version_line.split()
    if len(parts) < 2:
        raise AssertionError(f"Unexpected uv version output: {version_line}")
    version = parts[1]
    major, minor, patch = (int(x) for x in version.split("."))
    if (major, minor, patch) < (0, 6, 7):
        raise AssertionError(f"uv version {version} is less than 0.6.7")

@then("only required packages are present")
def _(required):
    result = subprocess.run(
        ["uv", "pip", "list", "--format", "json"],
        capture_output=True,
        text=True,
        check=True,
    )
    installed_packages = {pkg["name"].lower() for pkg in json.loads(result.stdout)}
    for req in required:
        if req == "python" or req == "uv":
            continue
        if req not in installed_packages:
            raise AssertionError(f"Required package missing: {req}")
    result = subprocess.run(
        ["uv", "pip", "check"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise AssertionError("uv pip check failed: dependency issues detected")
