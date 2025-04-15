
import yaml

# Load test files from the YAML configuration
with open("CABINET.yml", "r") as file:
    TESTS = [test["path"] for test in yaml.safe_load(file)["tests"]]

def pytest_ignore_collect(path):
    return path.basename not in TESTS

def pytest_collection_modifyitems(items):
    def sort_key(item):
        return (TESTS.index(item.fspath.basename), item.nodeid)

    items.sort(key=sort_key)

def pytest_bdd_before_scenario(scenario):
    print(f"\n\033[34mScenario: {scenario.name}\033[0m")

def pytest_bdd_after_step(step):
    print(f"\033[32m ✅ Step passed: {step.name}\033[0m")

def pytest_bdd_step_error(step):
    print(f"\033[31m 💥 Step failed: {step.name}\033[0m")
