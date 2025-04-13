# Define the list of test filenames to include and the order to run them
TESTS = [
    "test_bda_stub.py"
]

def pytest_ignore_collect(path, config):
    """
    Skip collecting any file not explicitly listed in TESTS.
    """
    return path.basename not in TESTS

def pytest_collection_modifyitems(config, items):
    """
    Sort collected items to match the order of TESTS.
    """
    def sort_key(item):
        return (TESTS.index(item.fspath.basename), item.nodeid)

    items.sort(key=sort_key)

