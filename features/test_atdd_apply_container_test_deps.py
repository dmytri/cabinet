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
def check_for_deps(request):
    result = subprocess.run(
        ["uv", "pip", "list", "--format", "json"],
        capture_output=True,
        text=True,
        check=True
    )
    installed = {pkg["name"].lower() for pkg in json.loads(result.stdout)}
    required = {"python", "uv", "pytest"}
    # Store in request for access in the next step
    request.config.cache.set("atdd_apply_container_test_deps/installed", installed)
    request.config.cache.set("atdd_apply_container_test_deps/required", required)

@then("all are installed and available")
def all_installed(request):
    installed = request.config.cache.get("atdd_apply_container_test_deps/installed", set())
    required = request.config.cache.get("atdd_apply_container_test_deps/required", set())
    missing = required - installed
    assert not missing, f"Missing required packages: {missing}"
