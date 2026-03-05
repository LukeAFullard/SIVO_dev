# SIVO Examples Plan

This document outlines a structured plan for creating example scripts and applications that demonstrate how to use SIVO (SVG Interactive Vector Objects). These examples will serve as practical tutorials for users, ranging from basic setup to advanced Streamlit integrations.

> **Note:** Each example should be contained within its own dedicated subfolder inside the `examples/` directory (e.g., `examples/01_hello_world/`) to keep scripts, SVGs, and generated HTML files cleanly isolated.

## Phase 1: Basic Usage (Standalone HTML Export)

**Objective:** Demonstrate the simplest way to use SIVO's Python API to transform an SVG into an interactive HTML file.

### Example 1.1: Hello World (Tooltips and Colors)
*   **Location:** `examples/01_hello_world/`
*   **Description:** Load a basic SVG (e.g., a simple geometric shape or a map outline). Map tooltips with simple HTML content and assign custom base/hover colors. Export to a standalone HTML file.
*   **Key Concepts:** `Sivo.from_svg()`, `map()` with `tooltip`, `html`, `color`, `hover_color`, `to_html()`.

### Example 1.2: URL Navigation
*   **Location:** `examples/02_url_navigation/`
*   **Description:** Map SVG elements to external URLs. Clicking a specific path opens a new tab.
*   **Key Concepts:** `map()` with `url`.

### Example 1.3: Declarative Configuration (JSON)
*   **Location:** `examples/03_json_config/`
*   **Description:** Show how to initialize a SIVO project entirely from a `config.json` file instead of writing Python mapping code.
*   **Key Concepts:** `Sivo.from_config()`, `ProjectConfig`.

---

## Phase 2: Advanced Standalone Features

**Objective:** Showcase complex interactivity within the exported HTML, requiring no backend server.

### Example 2.1: SVG Drill-Downs (Hierarchical Navigation)
*   **Location:** `examples/04_drilldowns/`
*   **Description:** Create a multi-level experience (e.g., World Map -> Country Map -> State Map). Clicking a region loads a secondary SVG file dynamically in the browser.
*   **Key Concepts:** `map()` with `drill_to`, ECharts dynamic map registration.

### Example 2.2: Custom Asset Injection
*   **Location:** `examples/05_custom_assets/`
*   **Description:** Inject custom CSS and JavaScript into the generated HTML to overlay custom floating UI elements or change the default tooltip styling beyond the standard API.
*   **Key Concepts:** `to_html(custom_css=..., custom_js=...)`.

---

## Phase 3: Streamlit Integration

**Objective:** Demonstrate bidirectional communication between interactive SVGs and a live Python backend using Streamlit.

### Example 3.1: Basic Callbacks (Click Events)
*   **Location:** `examples/06_streamlit_callbacks/`
*   **Description:** A simple dashboard where clicking an SVG element updates a Streamlit text metric or chart.
*   **Key Concepts:** `sivo_component()`, `map()` with `callback_event` and `callback_payload`, reading the return value in Streamlit.

### Example 3.2: Hover Events & Real-time State
*   **Location:** `examples/07_streamlit_hover/`
*   **Description:** A dashboard that reacts instantly as the user hovers over different SVG regions, updating side panels without requiring a click.
*   **Key Concepts:** `map()` with `hover_callback_event`, performance considerations with frequent state updates.

### Example 3.3: Programmatic Zooming & Panning
*   **Location:** `examples/08_streamlit_zoom/`
*   **Description:** A Streamlit app with a dropdown menu or buttons. Selecting an item in the Streamlit UI programmatically centers and zooms the SVG map to that specific element.
*   **Key Concepts:** `sivo_component(zoom_to="element_id")`.

### Example 3.4: Comprehensive Dashboard
*   **Location:** `examples/09_comprehensive_dashboard/`
*   **Description:** A culmination of all features: A "Smart Factory" or "Campus Management" dashboard featuring tooltips, click/hover callbacks to update live data graphs, drill-downs into specific buildings, and programmatic zooming based on external sensor data simulated in Streamlit.

---

## Process for Creating Examples

1.  **Create Directory:** Create a new subfolder for the example (e.g., `examples/01_hello_world/`). Place any required `.svg` files inside this directory to ensure path isolation.
2.  **Write Code:** Implement the example script clearly, with extensive inline comments explaining the *why* behind each SIVO API call.
3.  **Update README:** Link the new examples in the main project `README.md` under a "Tutorials / Examples" section.
4.  **Test:** Ensure Streamlit examples run cleanly via `streamlit run <script.py>` and standalone examples generate valid HTML that passes visual inspection in a browser.