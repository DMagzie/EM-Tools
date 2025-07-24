## ✅ GitHub Actions

- Automatic testing and linting on push
- Coverage reporting with `pytest --cov`

## 🧹 Pre-Commit Hooks

This project uses [pre-commit](https://pre-commit.com) to automatically enforce linting rules and code quality before every commit.

### Setup

1. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Install the Git hook:
   ```bash
   pre-commit install
   ```

3. To manually run all pre-commit checks on the entire repo:
   ```bash
   pre-commit run --all-files
   ```

The hook includes:
- `ruff` for linting (Python syntax, style, and import order)
- Automatic trailing whitespace and end-of-file fixes
- YAML syntax checks
