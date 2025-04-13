from pytest_bdd import scenario, given, when, then
import pytest
import subprocess
import json

@scenario("atdd_apply_container_test_deps.feature", "Apply container has Python, uv, and pytest installed")
def test_atdd_apply_container_test_deps():
    pass

@given("the apply container is running")
def apply_container_running():
    pass

@when("I check for Python, uv, and pytest")
def check_for_deps():
    result = subprocess.run(
        ["uv", "pip", "list", "--format", "json"],
        capture_output=True,
        text=True,
        check=True
    )
    installed = {pkg["name"].lower() for pkg in json.loads(result.stdout)}

    result_groups = subprocess.run(
        ["uv", "pip", "list", "--groups", "--format", "json"],
        capture_output=True,
        text=True,
        check=True
    )
    groups = json.loads(result_groups.stdout)
    declared = set()
    for group in groups.values():
        for pkg in group:
            declared.add(pkg["name"].lower())

    return {"installed": installed, "declared": declared}

@then("all are installed and available")
def all_installed(check_for_deps):
    installed = check_for_deps["installed"]
    declared = check_for_deps["declared"]
    missing = installed - declared
    assert not missing, f"Undeclared installed packages: {missing}"
