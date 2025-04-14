from pytest_bdd import scenarios, when, then
from pytest import fixture
import subprocess
import json

scenarios("atdd_apply_container_dependencies.feature")

@fixture
def target():
    return {
        "required": set(),
        "optional": set(),
        "python_checked": False,
        "uv_checked": False,
    }

@when("python >= 3.12 is required")
def _(target):
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
    target["python_checked"] = True

@when("uv is required")
def _(target):
    result = subprocess.run(
        ["uv", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    version_line = result.stdout.strip() or result.stderr.strip()
    if not version_line:
        raise AssertionError("Could not determine uv version")
    target["uv_checked"] = True

@when("pytest is required")
def _(target):
    target["required"].add("pytest")

@when("poethepoet is optional")
def _(target):
    target["optional"].add("poethepoet")

@then("only required or optional packages are present")
def _(target):
    result = subprocess.run(
        ["uv", "pip", "list", "--format", "json"],
        capture_output=True,
        text=True,
        check=True,
    )
    installed_packages = {pkg["name"].lower() for pkg in json.loads(result.stdout)}
    for req in target["required"]:
        if req not in installed_packages:
            raise AssertionError(f"Required package missing: {req}")
    result = subprocess.run(
        ["uv", "pip", "check"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise AssertionError("uv pip check failed: dependency issues detected")
