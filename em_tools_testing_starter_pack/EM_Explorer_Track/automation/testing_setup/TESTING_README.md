# EM Tools Testing Protocol

This folder contains setup files for automated and local testing using `pytest`.

## Structure

- `.github/workflows/run_pytest.yml`: GitHub Actions workflow for CI
- `requirements.txt`: Dependencies for test environment
- `tests/test_placeholder.py`: Example test case
- `automation/testing_setup/`: Backup of these setup files

## Running Tests Locally

```bash
pip install -r requirements.txt
pytest
```

## Running Tests in CI

On every push to `main` or `dev`, GitHub Actions will:
- Install dependencies
- Run `pytest`
- Upload logs as an artifact
