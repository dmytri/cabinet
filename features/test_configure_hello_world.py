import os
from pytest import skip
from pytest_bdd import scenarios, given, when, then
from kubernetes import client, config, utils

scenarios("configure_hello_world.feature")

# --- Steps for Scenario: Build Hello World Container ---

@then("The Hello World Container is running")
def _():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    namespace = "target"
    label_selector = "app=target"
    pod_list = v1.list_namespaced_pod(namespace=namespace, label_selector=label_selector)
    assert len(pod_list.items) > 0, f"FAIL: No pods found with label '{label_selector}' in namespace '{namespace}'"
    running_pods = [pod for pod in pod_list.items if pod.status.phase == "Running"]
    assert len(running_pods) > 0, f"FAIL: No pods with label '{label_selector}' are in the 'Running' phase in namespace '{namespace}'"
    print(f"PASS: Found {len(running_pods)} running pod(s) with label '{label_selector}' in namespace '{namespace}'")

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

