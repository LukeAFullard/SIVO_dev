# SIVO Examples Plan

This document outlines a structured plan for creating example scripts and applications that demonstrate how to use SIVO (SVG Interactive Vector Objects). These examples will serve as practical tutorials for users, ranging from basic setup to advanced Streamlit integrations.

> **Status Update:** All examples listed in this document have been **fully implemented and tested**. They are located in their respective subdirectories within the `examples/` folder.

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

### Example 2.3: HTML/DOM Overlays
*   **Location:** `examples/06_html_overlays/`
*   **Description:** Automatically calculate the center coordinate of SVG paths and attach absolutely positioned HTML overlays (like floating badges or micro-charts) directly over the map elements.
*   **Key Concepts:** `add_overlay()`, bounding box metadata processing.

### Example 2.4: Multi-View Standalone HTML
*   **Location:** `examples/07_multi_view_standalone/`
*   **Description:** Use the `SivoProject` class to bundle a Building, Floor, and Room SVG into a single, offline-capable interactive HTML file. Clicking a building navigates directly to the floorplan without needing external network fetches or a Python backend.
*   **Key Concepts:** `SivoProject`, `add_view()`, `map(drill_to="view_id")`.

### Example 2.5: Data-Driven Choropleths & Legends
*   **Location:** `examples/08_choropleth/`
*   **Description:** Load a US Map SVG and apply a data dictionary mapping state IDs to population values to automatically generate a heatmap and an interactive legend overlay.
*   **Key Concepts:** `apply_choropleth()`, `show_legend`.

### Example 2.6: Animations & Dynamic Markers
*   **Location:** `examples/09_animations_markers/`
*   **Description:** Load a factory floor SVG, use the animation API to make a broken machine pulse red, and use the marker API to drop a warning pin at its calculated center point.
*   **Key Concepts:** `add_marker()`, `animation="pulse"`.

---

## Phase 3: Streamlit Integration

**Objective:** Demonstrate bidirectional communication between interactive SVGs and a live Python backend using Streamlit.

### Example 3.1: Basic Callbacks (Click Events)
*   **Location:** `examples/10_streamlit_callbacks/`
*   **Description:** A simple dashboard where clicking an SVG element updates a Streamlit text metric or chart.
*   **Key Concepts:** `sivo_component()`, `map()` with `callback_event` and `callback_payload`, reading the return value in Streamlit.

### Example 3.2: Hover Events & Real-time State
*   **Location:** `examples/11_streamlit_hover/`
*   **Description:** A dashboard that reacts instantly as the user hovers over different SVG regions, updating side panels without requiring a click.
*   **Key Concepts:** `map()` with `hover_callback_event`, performance considerations with frequent state updates.

### Example 3.3: Dynamic Color Updates (Zero Re-render)
*   **Location:** `examples/12_dynamic_colors/`
*   **Description:** Streamlit app that rapidly updates the colors of multiple SVG elements based on a simulated live data feed (e.g., server load heatmaps), using `dynamic_colors` to avoid full component re-renders.
*   **Key Concepts:** `sivo_component(dynamic_colors={"element_id": "#ff0000"})`, `postMessage` state sync.

### Example 3.4: Programmatic Zooming & Panning
*   **Location:** `examples/13_streamlit_zoom/`
*   **Description:** A Streamlit app with a dropdown menu or buttons. Selecting an item in the Streamlit UI programmatically centers and zooms the SVG map to that specific element.
*   **Key Concepts:** `sivo_component(zoom_to="element_id")`.

### Example 3.5: Comprehensive Dashboard
*   **Location:** `examples/14_comprehensive_dashboard/`
*   **Description:** A culmination of all features: A "Smart Factory" or "Campus Management" dashboard featuring tooltips, HTML overlays for sensor badges, dynamic color updates for live alerts, hover callbacks to update side panels, drill-downs into specific building zones, and programmatic zooming based on external events.

---

## Phase 4: Advanced Infographic Narratives

**Objective:** Demonstrate narrative storytelling features and specific infographic visual controls natively available in standalone HTML exports.

### Example 4.1: Scrollytelling
*   **Location:** `examples/26_scrollytelling/`
*   **Description:** An interactive presentation where the SVG stays sticky on the left while a text column scrolls on the right, automatically triggering map zooms and color changes as paragraphs cross the viewport.
*   **Key Concepts:** `bind_scrollytelling()`, `ScrollytellingStepConfig`.

### Example 4.2: Guided Tours
*   **Location:** `examples/27_guided_tour/`
*   **Description:** An automatic step-by-step UI "Next/Prev" dialog overlay that walks a user through specific areas of a map without needing them to scroll or explore manually.
*   **Key Concepts:** `bind_tour()`, `TourStepConfig`.

### Example 4.3: Dynamic Text Odometers
*   **Location:** `examples/28_odometers/`
*   **Description:** Utilizes native SVG mode and requestAnimationFrame to smoothly count up large KPI numbers directly within the SVG canvas.
*   **Key Concepts:** `odometer_value`, `odometer_duration_ms`, `render_mode="svg"`.

### Example 4.4: Minimaps and High-Res Exports
*   **Location:** `examples/29_minimap_export/`
*   **Description:** Shows a global viewport tracking minimap in the corner that syncs with ECharts georoam state, and adds a camera button to download the state as PNG/SVG.
*   **Key Concepts:** `enable_minimap=True`, `enable_export=True`.

### Example 4.5: Interactive Layer Toggles
*   **Location:** `examples/30_layer_toggles/`
*   **Description:** Generates an absolute positioned checklist legend overlay that manipulates the visibility and opacity of distinct layer groups.
*   **Key Concepts:** `add_layer_toggle()`.

### Example 4.6: Hexbin Maps
*   **Location:** `examples/31_hexbin_map/`
*   **Description:** Generates a dense point data grid by aggregating overlapping markers into distinct, color-scaled hexagonal regions using an internal hex grid algorithm.
*   **Key Concepts:** `apply_hexbin()`.

### Example 4.7: Dot Density Maps
*   **Location:** `examples/32_dot_density_map/`
*   **Description:** Translates scalar values into scattered points that strictly adhere to the irregular polygonal bounds of an SVG path using HTML5 Canvas raycasting (`isPointInPath`).
*   **Key Concepts:** `apply_dot_density()`.

---

## Process for Creating Examples

1.  **Create Directory:** Create a new subfolder for the example (e.g., `examples/01_hello_world/`). Place any required `.svg` files inside this directory to ensure path isolation.
2.  **Write Code:** Implement the example script clearly, with extensive inline comments explaining the *why* behind each SIVO API call.
3.  **Update README:** Link the new examples in the main project `README.md` under a "Tutorials / Examples" section.
4.  **Test:** Ensure Streamlit examples run cleanly via `streamlit run <script.py>` and standalone examples generate valid HTML that passes visual inspection in a browser.