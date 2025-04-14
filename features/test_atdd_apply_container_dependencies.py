from pytest_bdd import scenarios, when, then
import subprocess
import json

scenarios("atdd_apply_container_dependencies.feature")

REQUIRED_PACKAGES = {
    "python": ">=3.12",
    "uv": None,
    "pytest": None,
}
OPTIONAL_PACKAGES = {
    "poethepoet": None,
}

@when("python >= 3.12 is required")
def _():
    result = subprocess.run(
        ["uv", "pip", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    version = ""
    for line in result.stdout.splitlines():
        if "using Python" in line:
            version = line.split("using Python")[-1].strip(" )\n")
            break
        if "Python" in line:
            version = line.split("Python")[-1].strip(" )\n")
            break
    if not version:
        raise AssertionError("Could not determine Python version from uv")
    major, minor, *_ = (int(x) for x in version.split("."))
    if (major, minor) < (3, 12):
        raise AssertionError(f"Python version {version} is less than 3.12")

@when("uv is required")
def _():
    result = subprocess.run(
        ["uv", "pip", "list", "--format", "json"],
        capture_output=True,
        text=True,
        check=True,
    )
    packages = {pkg["name"].lower(): pkg["version"] for pkg in json.loads(result.stdout)}
    if "uv" not in packages:
        raise AssertionError("uv is not installed")

@when("pytest is required")
def _():
    result = subprocess.run(
        ["uv", "pip", "list", "--format", "json"],
        capture_output=True,
        text=True,
        check=True,
    )
    packages = {pkg["name"].lower(): pkg["version"] for pkg in json.loads(result.stdout)}
    if "pytest" not in packages:
        raise AssertionError("pytest is not installed")

@when("poethepoet is optional")
def _():
    pass

@then("python is supported version")
def _():
    result = subprocess.run(
        ["uv", "pip", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    version = ""
    for line in result.stdout.splitlines():
        if "using Python" in line:
            version = line.split("using Python")[-1].strip(" )\n")
            break
        if "Python" in line:
            version = line.split("Python")[-1].strip(" )\n")
            break
    if not version:
        raise AssertionError("Could not determine Python version from uv")
    major, minor, *_ = (int(x) for x in version.split("."))
    if (major, minor) < (3, 12):
        raise AssertionError(f"Python version {version} is less than 3.12")

@then("only required or optional packages are present")
def _():
    result = subprocess.run(
        ["uv", "pip", "list", "--format", "json"],
        capture_output=True,
        text=True,
        check=True,
    )
    installed = {pkg["name"].lower(): pkg["version"] for pkg in json.loads(result.stdout)}
    allowed = set(REQUIRED_PACKAGES.keys()) | set(OPTIONAL_PACKAGES.keys())
    allowed.discard("python")
    for pkg in installed:
        if pkg not in allowed:
            raise AssertionError(f"Unexpected package installed: {pkg}")
    result = subprocess.run(
        ["uv", "pip", "check"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise AssertionError("uv pip check failed: dependency issues detected")
