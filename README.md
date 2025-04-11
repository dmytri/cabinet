## Key Practices

- All code and automation tasks follow [Behavior-Driven Automation (BDA)] and [Acceptance Test-Driven Development (ATDD)] patterns.
- Infra is managed declaratively with Kubernetes manifests applied via Tilt.
- Testing and provisioning scenarios live in `tests/`, with filenames prefixed by `bda_` or `atdd_`.
- All tooling runs via `uv` and `poe`, e.g.:

```bash
uv run poe start      # run app
uv run poe dev        # run tests
```

# Coding & Automation Conventions

This project uses a unified ruleset for all AI agents and automation logic.

Rules are defined in [`CONVENTIONS.md`](./CONVENTIONS.md), which should be symlinked for agents like Cursor to interpret and enforce:

```bash
ln -s CONVENTIONS.md .cursor-rules
```



