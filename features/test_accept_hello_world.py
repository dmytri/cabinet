import httpx
from typing import Callable
from pytest_bdd import scenarios, given, when, then
from pytest import fixture

scenarios("accept_hello_world.feature")

@fixture(scope="function")
def context():
    return {}

@given("the hello world URL", target_fixture="hello_world_url")
def _(marked: Callable[[str], bool]) -> str:
    if marked('dev'):
        return "http://localhost:8080/"
    elif marked('ci'):
        return "http://hello-world.target.svc.cluster.local"
    else marked("monitor"):
        return "https://asym.me/tric;to=hello-world"

@when("the user browses the hello world site")
def _(hello_world_url: str, context) -> None:
    response = httpx.get(hello_world_url)
    context["response"] = response

@then("the response status code should be 200")
def _(context) -> None:
    assert context["response"].status_code == 200

@then('the response should contain "hello world"')
def _(context) -> None:
    assert "hello world" in context["response"].text
