# Contributing to SIVO

First off, thank you for considering contributing to SIVO! It's people like you that make SIVO such a great tool.

## PR Workflow

1.  **Fork the repository** and create your branch from `main`.
2.  If you've added code that should be tested, **add tests**.
3.  Ensure your code passes our linting and type-checking rules.
4.  Update the documentation if necessary.
5.  Issue a pull request with a descriptive title and detailed summary.

## Code Standards

We adhere to standard Python coding conventions:
*   **Linting:** We use `flake8` and `ruff`. Ensure your code passes without warnings.
*   **Type-Checking:** We use `mypy` for static type checking. New code should include type hints.
*   **Formatting:** We use `black`.

To run the checks locally:
```bash
flake8 src/ tests/
mypy src/ tests/
```

## Branch Policies

*   `main`: The primary branch. It should always be stable and deployable.
*   `feature/*`: Use for new features.
*   `bugfix/*`: Use for bug fixes.
*   `docs/*`: Use for documentation updates.

## Testing

We use `pytest` for testing. Ensure you run the tests before submitting a PR.

```bash
pytest
```

For End-to-End (E2E) testing with Playwright, you may need to install the browsers first:

```bash
playwright install chromium
pytest tests/e2e
```

## Licensing
By contributing to SIVO, you agree that your contributions will be licensed under its MIT License.
