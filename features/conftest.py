import yaml
from pytest import fixture
from typing import cast, Callable

## FIXTURES
#

@fixture
def marked(pytestconfig) -> Callable[[str], bool]:
    markers = cast(str, pytestconfig.getoption("-m"))
    assert markers, "this cabinet requires pytest to be called with markers eg -m dev"
    joined = ' '.join(markers.split())
    normalized = f" {joined} "

    def _checker(mark: str) -> bool:
        has_mark: bool = f" {mark} " in normalized
        not_negated: bool = f" not {mark} " not in normalized
        return has_mark and not_negated

    return _checker

## ENFORCE EXITFIRST

def pytest_configure(config):
    if not config.option.maxfail == 1:
        raise RuntimeError("this cabinet requires -x/--exitfirst to be used.")

## ORDERING

with open("CABINET.yaml", "r") as file:
    TESTS = [test["path"] for test in yaml.safe_load(file)["tests"]]

def pytest_ignore_collect(path):
    return path.basename not in TESTS

def pytest_collection_modifyitems(items):
    def sort_key(item):
        return (TESTS.index(item.fspath.basename), item.nodeid)

    items.sort(key=sort_key)

# TEST OUTPUT

def pytest_bdd_before_scenario(scenario):
    print(f"\n\033[34mScenario: {scenario.name}\033[0m")

def pytest_bdd_after_step(step):
    print(f"\033[32m ✅ Step passed: {step.name}\033[0m")

def pytest_bdd_step_error(step):
    print(f"\033[31m 💥 Step failed: {step.name}\033[0m")
