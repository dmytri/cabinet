
import yaml

# Load test files from the YAML configuration
with open("CABINET.yaml", "r") as file:
    TESTS = [test["path"] for test in yaml.safe_load(file)["tests"]]
    print(f"Loaded test files: {TESTS}")

def pytest_ignore_collect(path):
    ignored = path.basename not in TESTS
    print(f"Ignoring {path.basename}: {ignored}")
    return ignored

def pytest_collection_modifyitems(items):
    def sort_key(item):
        print(f"item: {item}")
        return (TESTS.index(item.fspath.basename), item.nodeid)

    items.sort(key=sort_key)

def pytest_bdd_before_scenario(scenario):
    print(f"\n\033[34mScenario: {scenario.name}\033[0m")

def pytest_bdd_after_step(step):
    print(f"\033[32m ✅ Step passed: {step.name}\033[0m")

def pytest_bdd_step_error(step):
    print(f"\033[31m 💥 Step failed: {step.name}\033[0m")
