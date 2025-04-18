# AI Agent Guidelines

## Core Principles

This document defines operational guidelines for AI agents working in this
development environment. Follow these instructions precisely to ensure
consistent and expected behavior.

## Agent Behavior

### Test Handling
- **Do not** suggest or make any code changes in response to test output
- After test runs, **wait for user input** before taking any action
- When asked about test rules, reiterate: do nothing after test runs

### Code Modification
- **Do not** modify unrelated code, even if it appears broken or suboptimal
- Make changes only to code explicitly identified by the user

### Language
- Always use **Canadian English** spelling (e.g., "colour" not "color")

### Prompt Responses

#### HELLO Prompt
When the user says "hello", follow this exact sequence:
1. Summarize what you understand as key conventions
2. Be very concise, focusing only on what's important
3. Provide a TLDR version
4. Stop and wait for further instructions

#### TEST_RULES Prompt
When asked about test rules:
1. Reiterate the rule: do nothing after test runs
2. Wait for user direction

## Code Guidelines

### Error Handling Philosophy
- **Fail early**: Do not hide errors, allow scripts to fail naturally
- Do not add:
  - Try/except blocks
  - Guards
  - Silent fallbacks
- Exception: Only add error handling when explicitly requested

### Code Simplicity
- **No external dependencies** unless specifically instructed
- Use standard library and simple constructs
- **No inline comments** — code must be self-explanatory
- Do not add the following unless explicitly requested:
  - Validations
  - Docstrings
  - Type hints
  - Alternative approaches

## Python Environment

### Dependency Management
- Tool: **uv** (Python package manager)
- Enforce pyproject.toml for all dependencies
- Run commands:
  - Production: `uv run poe start`
  - Development: `uv run poe dev`

### Example Commands
```bash
# Add a package
uv add httpx

# Remove a package
uv remove httpx

# Synchronize dependencies
uv sync
```

## Commit Standards
- Format: **Conventional Commits**
- Example: `feat: add user authentication`

---

*These guidelines ensure consistent AI agent behavior aligned with project requirements and development standards.*

