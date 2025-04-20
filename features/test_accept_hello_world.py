import httpx
from pytest_bdd import scenarios, given, when, then

scenarios("accept_hello_world.feature")

@given("the hello world URL")
def _(marked: Callable[[str], bool], target_fixture("target_url")) -> None:

@when("the user browses the hello world site")
def _(context) -> None:
    response = httpx.get("http://example.com/hello-world")
    context["response"] = response

@then("the response status code should be 200")
def _(context) -> None:
    assert context["response"].status_code == 200

@then('the response should contain "hello world"')
def _(context) -> None:
    assert "hello world" in context["response"].text
