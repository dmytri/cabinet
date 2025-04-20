import os
from typing import cast
from pytest import skip, fixture, FixtureRequest
from pytest_bdd import scenarios, given, when, then
from kubernetes import client, config, utils
from kubernetes.client import CoreV1Api


## FIXTURES
#

# conftest.py

@fixture
def is_dev(request) -> bool:
    from _pytest.mark.evaluate import cached_eval
    expr: str = request.config.getoption("markexpr") or ""
    if not expr:
        return False
    namespace = {"dev": True}
    return bool(cached_eval(request.config, expr, namespace))

# @fixture
# def is_dev(pytestconfig) -> bool:
#     marker = pytestconfig.getoption("-m")
#     if not marker:
#         return False

#     joined = ' '.join(marker.split())
#     normalized = f" {joined} "
#     has_dev = " dev " in normalized
#     not_negated = " not dev " not in normalized

#     return has_dev and not_negated


## SCENARIOS
#

scenarios("configure_hello_world.feature")

# --- Steps for Scenario: Build Hello World Container ---

@given("Kubernetes API Connection", target_fixture="k8s_client")
def _(is_dev: bool) -> CoreV1Api:

    if is_dev:
        config.load_kube_config()
    else:
        config.load_incluster_config()

    return client.CoreV1Api()

@then("The Hello World Container is running")
def _(k8s_client: CoreV1Api) -> None:
    assert k8s_client.read_namespaced_service("hello-world", "target")

# --- Steps for Scenario: Publish Image to GitHub Container Registry ---

@given("Credentials for the GitHub Container Registry are available")
def _():
    username = os.getenv("GITHUB_USERNAME")
    token = os.getenv("GITHUB_TOKEN")
    assert username and token, "GITHUB_USERNAME and GITHUB_TOKEN must be set in the .env.creds file"

@given("Kaniko build image is present")
def _():
    skip("not implemented")

@when("Application Docker image is built")
def _():
    config.load_kube_config()
    k8s_client = client.ApiClient()
    yaml_file = 'build/manifest_build.yaml'
    utils.create_from_yaml(k8s_client,yaml_file,verbose=True)

@when("Image is pushed to the GitHub Container Registry")
def _():
    skip("not implemented")

@then("Image is available in the registry")
def _():
    skip("not implemented")

# --- Steps for Scenario: Proxy /hello requests to a dedicated Bunny pull zone ---

@given("Bunny API key is available")
def _():
    skip("not implemented")

@given('"asym.me" domain is served by a Bunny pull zone')
def _():
    skip("not implemented")

@when("A Bunny Magic Container running Hello World image")
def _():
    skip("not implemented")

@when('DNS CNAME record added from "hello.cdn.asym.me" to the Bunny Magic Container')
def _():
    skip("not implemented")

@when('Bunny pull zone "hello" created with origin "hello.cdn.asym.me"')
def _():
    skip("not implemented")

@when('Custom hostname "hello.cdn.asym.me" to the pull zone')
def _():
    skip("not implemented")

@when('TLS for the custom hostname "hello.cdn.asym.me"')
def _():
    skip("not implemented")

@when('Edge Rule added on the "asym.me" pull zone to forward "/hello" to "https://hello.cdn.asym.me"')
def _():
    skip("not implemented")

@then('Requests to "asym.me/hello" are served via the "hello" pull zone origin')
def _():
    skip("not implemented")

