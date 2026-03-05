# SIVO Examples Plan

This document outlines a structured plan for creating example scripts and applications that demonstrate how to use SIVO (SVG Interactive Vector Objects). These examples will serve as practical tutorials for users, ranging from basic setup to advanced Streamlit integrations.

## Phase 1: Basic Usage (Standalone HTML Export)

**Objective:** Demonstrate the simplest way to use SIVO's Python API to transform an SVG into an interactive HTML file.

### Example 1.1: Hello World (Tooltips and Colors)
*   **File:** `examples/01_hello_world.py`
*   **Description:** Load a basic SVG (e.g., a simple geometric shape or a map outline). Map tooltips with simple HTML content and assign custom base/hover colors. Export to a standalone HTML file.
*   **Key Concepts:** `Sivo.from_svg()`, `map()` with `tooltip`, `html`, `color`, `hover_color`, `to_html()`.

### Example 1.2: URL Navigation
*   **File:** `examples/02_url_navigation.py`
*   **Description:** Map SVG elements to external URLs. Clicking a specific path opens a new tab.
*   **Key Concepts:** `map()` with `url`.

### Example 1.3: Declarative Configuration (JSON)
*   **File:** `examples/03_json_config.py`
*   **Description:** Show how to initialize a SIVO project entirely from a `config.json` file instead of writing Python mapping code.
*   **Key Concepts:** `Sivo.from_config()`, `ProjectConfig`.

---

## Phase 2: Advanced Standalone Features

**Objective:** Showcase complex interactivity within the exported HTML, requiring no backend server.

### Example 2.1: SVG Drill-Downs (Hierarchical Navigation)
*   **File:** `examples/04_drilldowns.py`
*   **Description:** Create a multi-level experience (e.g., World Map -> Country Map -> State Map). Clicking a region loads a secondary SVG file dynamically in the browser.
*   **Key Concepts:** `map()` with `drill_to`, ECharts dynamic map registration.

### Example 2.2: Custom Asset Injection
*   **File:** `examples/05_custom_assets.py`
*   **Description:** Inject custom CSS and JavaScript into the generated HTML to overlay custom floating UI elements or change the default tooltip styling beyond the standard API.
*   **Key Concepts:** `to_html(custom_css=..., custom_js=...)`.

---

## Phase 3: Streamlit Integration

**Objective:** Demonstrate bidirectional communication between interactive SVGs and a live Python backend using Streamlit.

### Example 3.1: Basic Callbacks (Click Events)
*   **File:** `examples/06_streamlit_callbacks.py`
*   **Description:** A simple dashboard where clicking an SVG element updates a Streamlit text metric or chart.
*   **Key Concepts:** `sivo_component()`, `map()` with `callback_event` and `callback_payload`, reading the return value in Streamlit.

### Example 3.2: Hover Events & Real-time State
*   **File:** `examples/07_streamlit_hover.py`
*   **Description:** A dashboard that reacts instantly as the user hovers over different SVG regions, updating side panels without requiring a click.
*   **Key Concepts:** `map()` with `hover_callback_event`, performance considerations with frequent state updates.

### Example 3.3: Programmatic Zooming & Panning
*   **File:** `examples/08_streamlit_zoom.py`
*   **Description:** A Streamlit app with a dropdown menu or buttons. Selecting an item in the Streamlit UI programmatically centers and zooms the SVG map to that specific element.
*   **Key Concepts:** `sivo_component(zoom_to="element_id")`.

### Example 3.4: Comprehensive Dashboard
*   **File:** `examples/09_comprehensive_dashboard.py`
*   **Description:** A culmination of all features: A "Smart Factory" or "Campus Management" dashboard featuring tooltips, click/hover callbacks to update live data graphs, drill-downs into specific buildings, and programmatic zooming based on external sensor data simulated in Streamlit.

---

## Process for Creating Examples

1.  **Create Assets:** For each example, ensure a simple, clear SVG file exists in an `examples/assets/` directory.
2.  **Write Code:** Implement the example script clearly, with extensive inline comments explaining the *why* behind each SIVO API call.
3.  **Update README:** Link the new examples in the main project `README.md` under a "Tutorials / Examples" section.
4.  **Test:** Ensure Streamlit examples run cleanly via `streamlit run <script.py>` and standalone examples generate valid HTML that passes visual inspection in a browser.