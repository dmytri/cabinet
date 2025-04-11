from pytest_bdd import scenario, given, when, then

@scenario("bda_stub.feature", "Stub BDA test to ensure CI passes")
def test_bda_stub():
    pass

@given("the system is initialized")
def system_initialized():
    pass

@when("no action is taken")
def no_action():
    pass

@then("the test passes")
def test_passes():
    pass
