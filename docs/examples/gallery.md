---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# SIVO Visual Gallery & Examples

Welcome to the SIVO Example Gallery! This page provides a curated list of example scripts demonstrating the wide range of interactive features you can build.

All examples are located in the `examples/` directory of the SIVO repository and are grouped by category.

## Table of Contents

1. [Basic Usage](#basic-usage-standalone-html-export)
2. [Advanced Features](#advanced-standalone-features)
3. [Streamlit Integrations](#streamlit-integrations)
4. [Infographics & Narratives](#infographic-narratives)
5. [Maps & Charts](#maps--charts)

---

## Basic Usage (Standalone HTML Export)

These examples demonstrate the fundamental concepts of mapping Python configurations to SVG elements.

### 1. Hello World (Tooltips and Colors)
*   **Location:** `examples/basic/01_hello_world/main.py`
*   **Description:** Load a basic SVG, map tooltips with HTML content, and assign custom base/hover colors. Export to a standalone HTML file.
```python
from sivo import Sivo

sivo_app = Sivo.from_svg("sample.svg", enable_search=True)

sivo_app.map(
    element_id="sun",
    tooltip="The Sun",
    html="<h3>The Sun</h3><p>It is very bright and hot.</p>",
    color="gold",
    hover_color="yellow",
    glow=True
)

sivo_app.to_html("output.html")
```

### 2. URL Navigation
*   **Location:** `examples/basic/02_url_navigation/`
*   **Description:** Map SVG elements to external URLs. Clicking a specific path opens a new tab.

### 3. Declarative Configuration (JSON)
*   **Location:** `examples/basic/03_json_config/`
*   **Description:** Show how to initialize a SIVO project entirely from a `config.json` file instead of writing Python mapping code.

---

## Advanced Standalone Features

Showcase complex interactivity within the exported HTML, requiring no backend server.

### 1. SVG Drill-Downs (Hierarchical Navigation)
*   **Location:** `examples/basic/04_drilldowns/`
*   **Description:** Create a multi-level experience. Clicking a region loads a secondary SVG file dynamically in the browser.

### 2. Custom Asset Injection
*   **Location:** `examples/basic/05_custom_assets/`
*   **Description:** Inject custom CSS and JavaScript into the generated HTML to overlay custom floating UI elements or change the default tooltip styling.

### 3. HTML/DOM Overlays
*   **Location:** `examples/basic/06_html_overlays/`
*   **Description:** Automatically calculate the center coordinate of SVG paths and attach absolutely positioned HTML overlays directly over the map elements.

### 4. Multi-View Standalone HTML
*   **Location:** `examples/basic/07_multi_view_standalone/`
*   **Description:** Use the `SivoProject` class to bundle a Building, Floor, and Room SVG into a single, offline-capable interactive HTML file.

### 5. Bounding Coordinates (Geospatial Mapping)
*   **Location:** `examples/advanced/bounding_coords/`
*   **Description:** Demonstrates mapping real-world geographical coordinates (longitude and latitude) onto an SVG map and properly scaling dynamically generated proportional symbol scatter markers.

### 6. Animations & Dynamic Markers
*   **Location:** `examples/basic/09_animations_markers/`
*   **Description:** Load an SVG, use the animation API to make elements pulse, and use the marker API to drop pins at calculated center points.

---

## Streamlit Integrations

Demonstrate bidirectional communication between interactive SVGs and a live Python backend using Streamlit.

### 1. Basic Callbacks (Click Events)
*   **Location:** `examples/streamlit/10_streamlit_callbacks/`
*   **Description:** A simple dashboard where clicking an SVG element updates a Streamlit text metric or chart.

### 2. Hover Events & Real-time State
*   **Location:** `examples/streamlit/11_streamlit_hover/`
*   **Description:** A dashboard that reacts instantly as the user hovers over different SVG regions, updating side panels without requiring a click.

### 3. Dynamic Color Updates
*   **Location:** `examples/streamlit/12_dynamic_colors/`
*   **Description:** Rapidly update the colors of multiple SVG elements based on a simulated live data feed using `dynamic_colors` to avoid full component re-renders.

### 4. Programmatic Zooming & Panning
*   **Location:** `examples/streamlit/13_streamlit_zoom/`
*   **Description:** A Streamlit app with UI controls. Selecting an item programmatically centers and zooms the SVG map to that specific element.

### 5. Comprehensive Dashboard
*   **Location:** `examples/streamlit/14_comprehensive_dashboard/`
*   **Description:** A culmination of all features: tooltips, HTML overlays, dynamic color updates, hover callbacks, and programmatic zooming.

---

## Infographic Narratives

Demonstrate narrative storytelling features and specific infographic visual controls natively available in standalone HTML exports.

### 1. Scrollytelling
*   **Location:** `examples/infographics/26_scrollytelling/`
*   **Description:** An interactive presentation where the SVG stays sticky while a text column scrolls, automatically triggering map zooms and color changes.

### 2. Guided Tours
*   **Location:** `examples/infographics/27_guided_tour/`
*   **Description:** An automatic step-by-step UI "Next/Prev" dialog overlay that walks a user through specific areas of a map.

---

## Maps & Charts

Advanced spatial and data visualization techniques applied to custom SVGs.

### 1. Data-Driven Choropleths
*   **Location:** `examples/maps/08_choropleth/`
*   **Description:** Load an SVG and apply a data dictionary to automatically generate a heatmap and an interactive legend overlay.

### 2. Hexbin Maps
*   **Location:** `examples/maps/31_hexbin_map/`
*   **Description:** Generates a dense point data grid by aggregating overlapping markers into distinct, color-scaled hexagonal regions.

### 3. Dot Density Maps
*   **Location:** `examples/maps/32_dot_density_map/`
*   **Description:** Translates scalar values into scattered points that strictly adhere to the irregular polygonal bounds of an SVG path.

---

## Running the Examples

To run the standalone examples, simply execute the Python script from your terminal:

```bash
cd examples/basic/01_hello_world
python main.py
```

This will generate an `output.html` file in the same directory, which you can open in your web browser.

To run Streamlit examples, use the `streamlit run` command:

```bash
cd examples/streamlit/10_streamlit_callbacks
streamlit run main.py
```
