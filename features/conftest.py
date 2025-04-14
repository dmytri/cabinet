# Define the list of test filenames to include and the order to run them
TESTS = [
    "test_bda_stub.py",
    "test_atdd_apply_container_dependencies.py",
    "test_atdd_example.py"
]

def pytest_ignore_collect(path):
    """
    Skip collecting any file not explicitly listed in TESTS.
    """
    return path.basename not in TESTS

def pytest_collection_modifyitems(items):
    """
    Sort collected items to match the order of TESTS.
    """
    def sort_key(item):
        return (TESTS.index(item.fspath.basename), item.nodeid)

    items.sort(key=sort_key)

def pytest_bdd_before_scenario(scenario):
    print(f"\n\033[34mScenario: {scenario.name}\033[0m")

def pytest_bdd_after_step(step):
    print(f"\033[32m ✅ Step passed: {step.name}\033[0m")

def pytest_bdd_step_error(step):
    print(f"\033[31m 💥 Step failed: {step.name}\033[0m")
