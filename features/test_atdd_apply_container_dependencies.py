from pytest_bdd import scenarios, when, then, fixture
import subprocess
import json

scenarios("atdd_apply_container_dependencies.feature")

@fixture
def target():
    return {
        "required": set(),
        "optional": set(),
    }

@when("python >= 3.12 is required")
def _(target):
    target["required"].add("python")

@when("uv is required")
def _(target):
    target["required"].add("uv")

@when("pytest is required")
def _(target):
    target["required"].add("pytest")

@when("poethepoet is optional")
def _(target):
    target["optional"].add("poethepoet")

@then("python is supported version")
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

@then("only required or optional packages are present")
def _(target):
    result = subprocess.run(
        ["uv", "pip", "list", "--format", "json"],
        capture_output=True,
        text=True,
        check=True,
    )
    installed = {pkg["name"].lower(): pkg["version"] for pkg in json.loads(result.stdout)}
    allowed = set(target["required"]) | set(target["optional"])
    allowed.discard("python")
    for pkg in installed:
        if pkg not in allowed:
            raise AssertionError(f"Unexpected package installed: {pkg}")
    for req in target["required"]:
        if req == "python":
            continue
        if req not in installed:
            raise AssertionError(f"Required package missing: {req}")
    result = subprocess.run(
        ["uv", "pip", "check"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise AssertionError("uv pip check failed: dependency issues detected")
