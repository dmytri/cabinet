load('ext://namespace', 'namespace_create')

if k8s_namespace() != "target":
    fail("Must run in 'target' namespace")

namespace_create('target')

docker_build('target', 'target/')
k8s_yaml('target/manifest.yaml')
k8s_resource('target', port_forwards=['8080'], auto_init=False, trigger_mode=TRIGGER_MODE_MANUAL)

docker_build('build', 'build/')
k8s_yaml('build/manifest.yaml')
k8s_resource('build', auto_init=False, trigger_mode=TRIGGER_MODE_MANUAL)

docker_build('apply', '.')
k8s_yaml('manifest.yaml')
k8s_resource('apply', auto_init=False, trigger_mode=TRIGGER_MODE_MANUAL)

