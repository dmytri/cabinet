import httpx
from typing import Callable
from pytest_bdd import scenarios, given, when, then

scenarios("accept_hello_world.feature")

@given("the hello world URL", target_fixture="service")
def _(marked: Callable[[str], bool]) -> str:
    if marked('dev'):
        return "http://localhost:8080/"
    elif marked('ci'):
        return "http://target.hello-world.svc.cluster.local"
    else:
        return "https://asym.me/tric;to=hello-world"

@when("the user browses the hello world site")
def _(service: str, context) -> None:
    response = httpx.get(service)
    context["response"] = response

@then("the response status code should be 200")
def _(context) -> None:
    assert context["response"].status_code == 200

@then('the response should contain "hello world"')
def _(context) -> None:
    assert "hello world" in context["response"].text
