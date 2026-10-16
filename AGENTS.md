# Agent Instructions

Guidance for AI coding agents working in this repository.

## Package manager

Use [uv](https://docs.astral.sh/uv/). Commit `uv.lock` and run commands with `uv run --locked`.

## Commands

- `uv run --locked tox -e style` runs the linters, formatters and type checkers.
- `uv run --locked tox -e 3.14,cov` runs the tests with coverage.
- `uv run --locked prek run --all-files` runs the pre-commit hooks.

## Layout

- `src/app/main.py` mounts every example under `src/app/applications/<framework>/`.
- Each framework example lives in its own package with an `app.py`.
- Tests live in `tests/`.

## Conventions

- Ruff runs with `select = ["ALL"]`. Fix the code instead of adding ignores, except in `per-file-ignores` for framework signatures.
- Pin GitHub Actions by commit SHA with a version comment. Renovate keeps them current.
- Follow [Conventional Commits](https://www.conventionalcommits.org/) for commits and PR titles, and [Conventional Branch](https://conventional-branch.github.io/) for branch names.
