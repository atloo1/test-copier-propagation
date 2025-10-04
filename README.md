# test-copier-propagation

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/atloo1/test-copier-propagation/ci.yaml)](https://github.com/atloo1/test-copier-propagation/actions/workflows/ci.yaml?query=branch%3Amain)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Ftest-copier-propagation%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.project.requires-python&label=python)](https://github.com/atloo1/test-copier-propagation/blob/main/pyproject.toml)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Ftest-copier-propagation%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.project.version&label=version)](https://github.com/atloo1/test-copier-propagation/blob/main/pyproject.toml)
[![GitHub License](https://img.shields.io/github/license/atloo1/test-copier-propagation)](https://github.com/atloo1/test-copier-propagation/blob/main/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/atloo1/test-copier-propagation)

[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](https://docs.docker.com/get-started/get-docker/)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

test copier change propagation

## prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## use

```
uv run python -m src.test_copier_propagation.main
```

## development

### 1st time setup

```
uv run pre-commit install
```

### sync with parent template

```
uv run copier update
```

### test locally (preemptively pass the corresponding GitHub action)

```
uv run pytest
```
