---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# SIVO (SVG Interactive Vector Objects) Documentation

Welcome to the SIVO documentation hub! SIVO is a powerful Python framework designed to transform static SVG graphics into responsive, interactive web infographics seamlessly.

SIVO allows developers, designers, and data analysts to attach dynamic behaviors—such as tooltips, drill-downs, URL navigation, and dynamic updates—to individual SVG paths or groups without needing to write any complex JavaScript logic.

## Key Value Proposition
* **100% Serverless**: SIVO compiles your Python definitions directly into standalone, interactive HTML bundles. No backend server required.
* **Declarative Python API**: Define interactive behaviors, colors, styles, and data bindings purely in Python.
* **AI-Friendly**: Fully declarative and structured, making it easy for LLMs to generate or modify configurations.
* **Seamless Integration**: Easily embed your SIVO outputs in Streamlit or other web applications.

## Installation

Requirements: Python 3.8+

Install SIVO via pip:

```bash
pip install sivo
```

## Quick Start: Hello World

Creating your first interactive map with SIVO is incredibly simple. You load a static SVG, attach an action to an element (like adding a color and tooltip), and export the interactive HTML.

```python
from sivo import Sivo

# 1. Initialize Sivo from an SVG file
sivo_app = Sivo.from_svg("campus_map.svg")

# 2. Map interactions to an SVG element ID
sivo_app.map(
    element_id="buildingA",
    color="blue",
    tooltip="Hello Region 1"
)

# 3. Export to an interactive HTML bundle
sivo_app.to_html("interactive_map.html")
```

For more details on building your first project, check out our [Getting Started Tutorial](tutorials/getting-started.md).

## Responsive CSS Grid Dashboards (No-Code)
SIVO supports building responsive dashboards with multiple SVG blocks and dynamically generated data panels without writing custom HTML or JS. It uses CSS Grid to natively stack blocks on mobile devices.

```python
from sivo import Sivo, SivoDashboard

sivo_map = Sivo.from_svg("campus_map.svg")
sivo_map.map(
    "buildingA",
    html="<p>This is the main facility.</p><img src='building.jpg'>",
    callback_payload={"revenue": "$1.2M", "status": "Active"}
)

dashboard = SivoDashboard(title="Campus Overview")

# 1. Add the interactive map
dashboard.add_sivo_block("map", sivo_map)

# 2. Add a pre-built Details Panel (automatically renders the `html` content of clicked elements)
dashboard.add_details_panel("details", title="Building Details")

# 3. Add a pre-built Metrics Panel (automatically renders keys from `callback_payload`)
dashboard.add_metrics_panel("metrics", title="Live Data", metrics=["revenue", "status"])

dashboard.to_html("dashboard.html")
```

## Streamlit Integration
Render your interactive SVGs directly inside your Streamlit apps and receive callback data.

```python
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component

st.title("Interactive Campus Dashboard")

# Initialize and map interactions
sivo_app = Sivo.from_svg("campus_map.svg")

sivo_app.map(
    element_id="buildingB",
    tooltip="Engineering Block",
    callback_event="select_building",
    callback_payload={"building_id": "B"}
)

# Render the SIVO component
result = sivo_component(sivo_app, key="campus_dashboard")

if result:
    st.write("You clicked on:", result)
```

## Advanced Usage

### End-to-End (E2E) Browser Testing (Non-Default)
For enterprise use-cases, it is highly recommended to enable E2E testing to ensure custom interactive SVGs scale correctly across browsers without regressions.

To enable scaffolding for Playwright, set the `enable_e2e_testing` flag in `ProjectConfig` to `True`. Then run tests using:
```bash
playwright install --with-deps chromium
pytest tests/e2e
```

### JavaScript Bundling (Non-Default)
By default, SIVO relies on CDN links (e.g., ECharts) to render the map quickly. If you want to bundle JS locally for offline environments or better minify assets, set `build_js=True` in your `ProjectConfig` or call `sivo_app.build_javascript()`. SIVO will invoke a JS bundler pipeline before generating the HTML output.

### Real-time Telemetry (LiveBindingConfig)
SIVO supports native WebSocket/PubSub integration to push real-time state changes directly to the browser (bypassing Streamlit). Use `sivo_app.bind_live("wss://your-broker", "sensor_data")` to connect the interactive canvas to a live data feed.

### Declarative Configuration (JSON)
For complex deployments or low-code environments, SIVO can be entirely configured via a JSON file.

```json
{
  "svg_file": "campus_map.svg",
  "mappings": {
    "buildingA": {
      "tooltip": "Main Admin",
      "color": "#ff0000"
    }
  }
}
```

Load it directly in Python:
```python
from sivo import Sivo

sivo_app = Sivo.from_config("project.json")
sivo_app.to_html("output.html")
```

### Command Line Interface (CLI)
SIVO includes a helpful CLI to speed up the workflow:

**Initialize a config from an SVG:**
```bash
python -m sivo init campus_map.svg -o project.json
```

**Validate a config against its SVG:**
```bash
python -m sivo validate project.json
```

**Export an HTML bundle from a config:**
```bash
python -m sivo export project.json -o interactive_map.html
```

## Structure
SIVO parses and normalizes SVGs using `lxml`, manages configurations with `pydantic`, and uses `Jinja2` with `Apache ECharts` on the frontend for rendering the SVG interactions.


## Visual Gallery & Use Cases

SIVO is incredibly versatile. It's used for:
*   **Interactive Maps**: Campus layouts, seating charts, architectural diagrams.
*   **Data Dashboards**: Binding live data to floor plans or schematic diagrams.
*   **Presentations**: Scrollytelling and guided visual tours.
*   **Data-driven Visualizations**: Choropleth maps and hexbins without geospatial setups.

See the [Visual Gallery](examples/gallery.md) for screenshots and full code examples!

We provide extensive examples ranging from basic setup to comprehensive Streamlit dashboards. Check the `examples/` directory for full scripts:

*   **Phase 1: Basic Usage:** Hello World (`examples/01_hello_world`), URL Navigation (`examples/02_url_navigation`), Declarative Configuration (`examples/03_json_config`).
*   **Phase 2: Advanced Standalone Features:** SVG Drill-Downs (`examples/04_drilldowns`), Custom Asset Injection (`examples/05_custom_assets`), HTML/DOM Overlays (`examples/06_html_overlays`), Multi-View Standalone HTML (`examples/07_multi_view_standalone`), Static Choropleths (`examples/08_choropleth`), Dynamic Data Binding & Legend (`examples/08_data_binding`), Animations & Dynamic Markers (`examples/09_animations_markers`), Document Embeds (`examples/10_document_and_map_embed`).
*   **Phase 3: Streamlit Integration:** Basic Callbacks (`examples/10_streamlit_callbacks`), Hover Events (`examples/11_streamlit_hover`), Dynamic Color Updates (`examples/12_dynamic_colors`), Programmatic Zooming (`examples/13_streamlit_zoom`), Comprehensive Dashboard (`examples/14_comprehensive_dashboard`).
*   **Phase 4: External Integrations:** Analytics & Live Data (`examples/22_analytics_and_data`), Forms & E-commerce (`examples/23_forms_and_ecommerce`), Rich Media & Business Intelligence (`examples/24_rich_media_and_bi`), New Integrations (`examples/25_new_integrations`), Nested ECharts Action (`examples/15_echarts_action`), Zoom on Click (`examples/16_zoom_on_click`).
*   **Phase 5: Infographic Narratives:** Scrollytelling (`examples/26_scrollytelling`), Guided Tours (`examples/27_guided_tour`), Dynamic Odometers (`examples/28_odometers`), Minimap & Export (`examples/29_minimap_export`), Layer Toggles (`examples/30_layer_toggles`), Hexbin Maps (`examples/31_hexbin_map`), Dot Density Maps (`examples/32_dot_density_map`), Timeline UI (`examples/46_timeline_playback_ui`).

These examples demonstrate the fully implemented Phase 1, 2, 3, 4, and 5 project goals.


## Project Architecture Map

SIVO's architecture is divided into two parts:

1.  **The Python Core (`src/sivo/core`)**: The declarative API where you define configurations, state actions, styling, and data handling. SIVO validates these using Pydantic.
2.  **The JS Runtime (`src/sivo/runtime`)**: The Jinja2 templates (using ECharts) that are injected with your configurations to generate the final standalone HTML file.

For a deeper dive, read our [Core Concepts Guide](guides/core-concepts.md).
*   **AI Agents**: If you are an AI assistant, refer to our [AI Manifest](ai/manifest.md).
*   **Developers**: Refer to our [Technical API Reference](api/core_models.md).

## Contributing & Community

SIVO is released under the permissive [MIT License](https://opensource.org/licenses/MIT).

We welcome contributions! Please see our [Contributing Guidelines](api/developer_contributing.md) for information on running tests, issue tracking, and PR guidelines.
