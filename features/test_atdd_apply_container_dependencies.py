from pytest_bdd import scenarios, when
import sys

scenarios("atdd_apply_container_dependencies.feature")

import subprocess

@when("uv >= 0.6.7")
def _():
    result = subprocess.run(['uv', '--version'], capture_output=True, text=True)
    version = result.stdout.strip()
    assert version >= "0.6.7"
