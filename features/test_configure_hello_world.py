import os
from pytest import skip, fixture
from pytest_bdd import scenarios, given, when, then
from kubernetes import client, config, utils
from kubernetes.client import CoreV1Api
from typing import cast

## FIXTURES
#

@fixture
def markers(pytestconfig) -> str:
    markers = cast(str, pytestconfig.getoption("-m"))
    assert markers, "pytest must be called with markers eg -m dev"
    joined = ' '.join(markers.split())
    normalized = f" {joined} "
    return normalized

@fixture
def marked(mark: str, markers: str) -> bool:
    has_dev: bool = f" {mark} " in markers
    not_negated: bool = f" not {mark} " not in markers

    return has_dev and not_negated


## SCENARIOS
#

scenarios("configure_hello_world.feature")

# --- Steps for Scenario: Build Hello World Container ---

@given("Kubernetes API Connection is available", target_fixture="k8s_client")
def _(marked) -> CoreV1Api:

    if marked('dev'):
        config.load_kube_config()
    elif marked('ci'):
        config.load_incluster_config()
    else:
        raise RuntimeError("Kubernetes API Connection is not available")

    return client.CoreV1Api()

@then("The Hello World Service is available")
def _(k8s_client: CoreV1Api) -> None:
    assert k8s_client.read_namespaced_service("hello-world", "target")

# --- Steps for Scenario: Publish Image to GitHub Container Registry ---

@given("Credentials for the GitHub Container Registry are available")
def _() -> None:
    username = os.getenv("GITHUB_USERNAME")
    token = os.getenv("GITHUB_TOKEN")
    assert username and token, "GITHUB_USERNAME and GITHUB_TOKEN must be set in the .env.creds file"

@given("Kaniko build image is present")
def _() -> None:
    skip("not implemented")

@when("Application Docker image is built")
def _() -> None:
    config.load_kube_config()
    k8s_client = client.ApiClient()
    yaml_file = 'build/manifest_build.yaml'
    utils.create_from_yaml(k8s_client,yaml_file,verbose=True)

@when("Image is pushed to the GitHub Container Registry")
def _() -> None:
    skip("not implemented")

@then("Image is available in the registry")
def _() -> None:
    skip("not implemented")

# --- Steps for Scenario: Proxy /hello requests to a dedicated Bunny pull zone ---

@given("Bunny API key is available")
def _() -> None:
    skip("not implemented")

@given('"asym.me" domain is served by a Bunny pull zone')
def _() -> None:
    skip("not implemented")

@when("A Bunny Magic Container running Hello World image")
def _() -> None:
    skip("not implemented")

@when('DNS CNAME record added from "hello.cdn.asym.me" to the Bunny Magic Container')
def _() -> None:
    skip("not implemented")

@when('Bunny pull zone "hello" created with origin "hello.cdn.asym.me"')
def _() -> None:
    skip("not implemented")

@when('Custom hostname "hello.cdn.asym.me" to the pull zone')
def _() -> None:
    skip("not implemented")

@when('TLS for the custom hostname "hello.cdn.asym.me"')
def _() -> None:
    skip("not implemented")

@when('Edge Rule added on the "asym.me" pull zone to forward "/hello" to "https://hello.cdn.asym.me"')
def _() -> None:
    skip("not implemented")

@then('Requests to "asym.me/hello" are served via the "hello" pull zone origin')
def _() -> None:
    skip("not implemented")

