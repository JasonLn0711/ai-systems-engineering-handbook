# Failure Modes

- Container works locally but fails with missing env, volume, or network config.
- Kubernetes deployment loops because readiness or startup assumptions are wrong.
- GPU workload fails because runtime and scheduling requirements are not declared.
