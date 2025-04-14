from pytest_bdd import scenarios, scenario, when, then
import subprocess
import json

scenarios("atdd_apply_container_dependencies.feature")

@scenario("atdd_apply_container_dependencies.feature", "Apply container has dependencies")
def _():
    pass

REQUIRED_PACKAGES = {
    "python": ">=3.12",
    "uv": None,
    "pytest": None,
}
OPTIONAL_PACKAGES = {
    "poethepoet": None,
}

def _get_python_version_from_uv():
    result = subprocess.run(
        ["uv", "pip", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    # Accept both "using Python" and "Python" in output for robustness
    for line in result.stdout.splitlines():
        if "using Python" in line:
            return line.split("using Python")[-1].strip(" )\n")
        if "Python" in line:
            # fallback: extract after "Python"
            return line.split("Python")[-1].strip(" )\n")
    return ""

def _get_installed_packages():
    result = subprocess.run(
        ["uv", "pip", "list", "--format", "json"],
        capture_output=True,
        text=True,
        check=True,
    )
    return {pkg["name"].lower(): pkg["version"] for pkg in json.loads(result.stdout)}

def _has_package(name):
    packages = _get_installed_packages()
    return name.lower() in packages

def _get_package_version(name):
    packages = _get_installed_packages()
    return packages.get(name.lower())

def _uv_pip_check():
    result = subprocess.run(
        ["uv", "pip", "check"],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0

@when("python >= 3.12 is required")
def _():
    version = _get_python_version_from_uv()
    if not version:
        raise AssertionError("Could not determine Python version from uv")
    major, minor, *_ = (int(x) for x in version.split("."))
    if (major, minor) < (3, 12):
        raise AssertionError(f"Python version {version} is less than 3.12")

@when("uv is required")
def _():
    if not _has_package("uv"):
        raise AssertionError("uv is not installed")

@when("pytest is required")
def _():
    if not _has_package("pytest"):
        raise AssertionError("pytest is not installed")

@when("poethepoet is optional")
def _():
    # Optional: do nothing, just check presence in @then step
    pass

@then("python is supported version")
def _():
    version = _get_python_version_from_uv()
    if not version:
        raise AssertionError("Could not determine Python version from uv")
    major, minor, *_ = (int(x) for x in version.split("."))
    if (major, minor) < (3, 12):
        raise AssertionError(f"Python version {version} is less than 3.12")

@then("only required or optional packages are present")
def _():
    installed = _get_installed_packages()
    allowed = set(REQUIRED_PACKAGES.keys()) | set(OPTIONAL_PACKAGES.keys())
    # python is not listed in uv pip list, so ignore it
    allowed.discard("python")
    for pkg in installed:
        if pkg not in allowed:
            raise AssertionError(f"Unexpected package installed: {pkg}")
    # Check for dependency issues
    if not _uv_pip_check():
        raise AssertionError("uv pip check failed: dependency issues detected")
