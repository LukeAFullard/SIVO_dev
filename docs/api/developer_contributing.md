---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Developer & Contributing Guidelines

Thank you for your interest in contributing to SIVO! These guidelines will help you set up your local development environment, run tests, and understand the expected PR workflow.

## Setting Up Your Environment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/sivo.git
   cd sivo
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   Install both standard and development requirements.
   ```bash
   pip install -r requirements.txt
   pip install pytest pytest-cov pytest-playwright flake8 ruff mypy
   ```

4. **Install Playwright Browsers:**
   Playwright requires specific browser binaries for End-to-End (E2E) testing.
   ```bash
   playwright install chromium
   ```

## Coding Standards & Linting

SIVO strictly adheres to standard Python coding conventions to ensure readability and maintainability.

- **Linting:** We use `flake8` and `ruff`. Ensure your code passes all linting rules without warnings.
- **Type-Checking:** We use `mypy` for static type checking. All new code must include comprehensive type hints.
- **Formatting:** Ensure your code is properly formatted (e.g., using `black`).
- **Logging:** Use the standard Python `logging` module. **Do not use `print()` statements** in core library code.

Run checks locally:
```bash
flake8 src/ tests/
ruff check src/ tests/
mypy src/ tests/
```

## Running Tests

Testing is critical. Before submitting a PR, ensure all tests pass.

### Unit Tests
Run the standard unit test suite:
```bash
PYTHONPATH=src pytest
```

*(Note: We set `PYTHONPATH=src` so the test runner correctly resolves internal module imports).*

### End-to-End (E2E) Tests
Run the E2E suite to verify frontend rendering and interactions:
```bash
PYTHONPATH=src pytest tests/e2e
```

**Important Notes for E2E Testing:**
- E2E tests may generate local test artifacts (e.g., `test_autoshrink.html`). Do not commit these files. Ensure they are ignored via `.gitignore` or clean them up before committing.

## CI/CD Pipeline

We enforce quality via GitHub Actions. Our pipeline (`.github/workflows/ci.yml`) automatically runs:
- Python linting (`flake8`, `ruff`)
- Type-checking (`mypy`)
- Tests (`pytest` and `pytest-playwright` with coverage)
- Vulnerability scanning (`npm audit`, `pip-audit`)

Your PR must pass all CI checks before it can be merged.

## PR Workflow

1. Create a branch from `main` (e.g., `feature/your-feature-name` or `bugfix/issue-number`).
2. Write tests for your new code or fix.
3. Verify your changes locally (run linters, unit tests, and E2E tests).
4. Update relevant documentation.
5. Create a Pull Request with a clear title and detailed summary of changes.

By contributing to SIVO, you agree that your contributions will be licensed under its MIT License.
