---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# A-01: AI Agent Manifest

A comprehensive map for AI agents to understand the repository structure, entry points, and coding guidelines when working with the SIVO codebase.

## 1. Repository Overview for Agents

The SIVO repository is structured to separate concerns between the declarative Python API used by users, the internal SVG parsing and manipulation logic, and the Jinja2-based HTML/JS runtime that renders the interactive visualizations. SIVO does not use an active backend server during runtime; it compiles user configurations into standalone HTML bundles.

## 2. Directory Structure & Roles

### `src/sivo/core/`
This directory contains the primary Python API and Pydantic models.
*   **`sivo.py`**: Contains the core `Sivo` class, which handles importing SVGs, mapping data, and bundling output.
*   **`config.py`**: Defines the rigorous Pydantic configuration models (e.g., `SivoConfig`, `ViewConfig`, `ElementConfig`). These govern data validation.
*   **`actions.py`**: Defines the interactive action models (e.g., `TooltipAction`, `ClickAction`, `DrillDownAction`).
*   **`infographic.py`**: Implements the `Infographic` class for generating static and thematic visual elements (e.g., bar charts, choropleths).
*   **`dashboard.py`** & **`project.py`**: Handle multi-view, grid-based layout implementations (`SivoDashboard` and `SivoProject`).

### `src/sivo/svg/`
This directory handles raw SVG processing and manipulation.
*   **`parser.py`**: Parses raw SVGs using `lxml` with strict security settings (e.g., `resolve_entities=False` to prevent XXE).
*   **`manipulator.py`**: Logic for modifying paths, transforming coordinates, generating dynamic elements (like auto-scaled text and Native SVG KPI cards), and injecting CSS.

### `src/sivo/runtime/`
This directory contains the bundling logic and the frontend JS/HTML templates.
*   **`bundle_generator.py`**: The bridge that converts the validated Pydantic Python configurations into a serialized JSON payload and injects it into Jinja2 templates.
*   **`templates/echarts.html`**: The default Javascript runtime engine. It initializes Apache ECharts to render the SVG, loads `window.SivoData`, and attaches frontend event listeners for user interactions.
*   **`templates/dashboard_blocks.html`**: A secondary runtime engine specifically for rendering CSS-grid based `SivoDashboard` configurations.

### `src/sivo/cli/`
Contains the SIVO Command Line Interface logic for initializing configurations from SVGs, validating JSON configs, and running the local annotation server.

### `tests/`
*   **`tests/`**: Contains pytest test files. Note that frontend UI verifications use Playwright in `tests/e2e/`.

## 3. Key Architectural Constraints

When writing or modifying code for SIVO, AI agents must adhere to the following constraints:

1.  **100% Serverless Execution**: SIVO outputs standalone HTML files. The JS bundle must function purely on the client side without relying on an active Python server for its core functionality (except when explicitly using LiveBinding, which uses WebSockets, or the Streamlit component).
2.  **Strict Pydantic Models**: All configuration inputs are validated against strict Pydantic models with `model_config = ConfigDict(extra="forbid")`. Agents must not generate or hallucinate unknown kwargs, as this will trigger explicit validation errors during mapping.
3.  **Jinja2 Data Injection**: Python dictionaries are serialized and injected into the HTML templates (e.g., `echarts.html`) via Jinja2 (e.g., `var SivoData = {{ sivo_data | tojson | safe }};`).
4.  **Logging Standard**: Standard `print` statements are strictly forbidden in core files. The standard Python `logging` module must be used (`logger.info`, `logger.warning`, etc.).
5.  **Security**:
    *   **CSP & DOMPurify**: Frontend HTML injections (via `.innerHTML`) must always be wrapped in `window.DOMPurify.sanitize()` to prevent XSS. A strict Content-Security-Policy (CSP) is implemented in templates.
    *   **Path Traversal**: File opening operations must securely resolve and validate paths using `os.path.abspath` or `os.path.realpath`, preventing traversal attacks (`..`).
    *   **SSRF**: URL fetching (e.g., in `fetch_image_base64`) must explicitly validate standard `http`/`https` schemes and reject localhost or internal IP ranges.

## 4. Important Entry Points for Agents

When attempting to solve a bug or implement a feature, start your investigation here:
*   **User API Changes**: `src/sivo/core/sivo.py`
*   **Configuration Validation Errors**: `src/sivo/core/config.py` and `src/sivo/core/actions.py`
*   **SVG Structure or Element Creation**: `src/sivo/svg/manipulator.py`
*   **Frontend Javascript Logic**: `src/sivo/runtime/templates/echarts.html`
*   **Python to JS Bridging**: `src/sivo/runtime/bundle_generator.py`

## 5. Cross-References

For more specific details, refer to the following documentation:
*   [Pydantic Schema Reference](schema-reference.md)
*   [Technical API Reference](../api/core_models.md) (When implemented)
*   [Troubleshooting Guide](../reference/troubleshooting.md)

## Getting Started

If you are a human reading this or generating code, ensure you check out the [Getting Started Tutorial](../tutorials/getting-started.md) and [Core Concepts](../guides/core-concepts.md) for a human-centric introduction.
