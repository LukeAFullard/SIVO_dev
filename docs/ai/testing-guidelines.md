---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# A-07: AI Agent Testing Guidelines

This document provides strategies and constraints for AI agents generating tests for the SIVO repository, particularly focusing on Playwright E2E tests and WASM/Pyodide environments.

## 1. End-to-End (E2E) Testing with Playwright

SIVO outputs standalone HTML files that rely heavily on client-side Javascript (Apache ECharts, DOM manipulation). Therefore, unit testing the Python output is insufficient. The actual interactive behavior must be verified using Playwright.

### Core Principles for E2E Test Generation

*   **Location:** All frontend UI verification tests must be placed in the `tests/e2e/` directory (e.g., `test_dashboard_e2e.py`, `test_multi_view.py`).
*   **Framework:** Use `pytest-playwright`.
*   **Test Artifact Cleanup:** Ensure that tests which generate or mutate test artifact files (e.g., `test_autoshrink.html`) revert these side effects before completing, to keep the repository clean.
*   **Asynchronous Handling:** When interacting with elements that trigger animations, network requests, or complex state changes, ensure appropriate `expect(page.locator(...)).to_be_visible()` or similar waits are used instead of hardcoded sleeps.

### Handling Media Playback

When triggering asynchronous media playback (like `audio.play()`) in SIVO's frontend templates, browser strict autoplay policies may reject the promise.
*   **Agent Constraint:** Generated Javascript snippets or test mocks must append a `.catch()` block to gracefully handle promise rejections.

## 2. WASM / Pyodide Constraints (Serverless Execution)

SIVO is designed to be 100% serverless, meaning it can run entirely within the browser using Pyodide/WASM.

### Testing Considerations

*   **No Active Backend:** SIVO does not have a running Python server during execution (unless explicitly using `LiveBinding` with WebSockets). Tests must assume the environment is fully static once compiled to HTML.
*   **File System Access:** When generating tests for Pyodide environments, remember that the "file system" is virtualized in memory. `from_svg` and similar methods must be tested using mocked or virtually injected file structures.
*   **Network Requests:** In Pyodide, standard Python `requests` will not work. SIVO uses `pyodide.http.pyfetch` for network calls when in WASM. AI agents generating mock APIs or testing external integration should account for `fetch()` API behaviors and mock appropriately.

## 3. General Testing Rules

1.  **Run All Checks:** Always attempt to run the full test suite when modifying SIVO code: `PYTHONPATH=src pytest` or `PYTHONPATH=src python run_all_tests.py`.
2.  **Dependencies:** Tests require `pytest`, `pytest-playwright`, `lxml`, and the playwright browser (`playwright install chromium`).
3.  **Logging Verification:** Since `print` statements are forbidden, tests should verify expected behaviors via the `logging` module where applicable, ensuring warnings or errors are logged correctly.
