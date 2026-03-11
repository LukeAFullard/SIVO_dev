# SIVO (SVG Interactive Vector Objects)

SIVO is a powerful Python framework designed to transform static SVG graphics into responsive, interactive web infographics seamlessly. It allows developers, designers, and data analysts to attach dynamic behaviors—such as tooltips, drill-downs, URL navigation, and dynamic updates—to individual SVG paths or groups without needing to write any complex JavaScript logic.

SIVO acts as the bridge between vector design tools and interactive web data visualization. It supports integration with **Streamlit** for live operational dashboards, and can export standalone interactive HTML bundles.

## Features
*   **Zero-JavaScript Setup**: Define interactions purely in Python or via declarative JSON configurations.
*   **Streamlit Integration**: A native V2 Custom Component is provided for seamless embedding and bidirectional data flow in Streamlit applications.
*   **Complex SVG Handling**: Automatically normalizes complex SVGs, including correctly handling nested `<g>` tags and `<use>` symbol references.
*   **Rich Behaviors**: Attach custom tooltips (supporting HTML content via Shadow DOM), URL navigation, state/callback events, and visual styling changes to any SVG element.
*   **External Integrations**: Easily embed and configure Analytics (Google Analytics, PostHog, Plausible), Data Sources (Google Sheets, Airtable, Notion APIs), E-commerce (Stripe, Shopify), Forms (Typeform, Jotform, HubSpot, Google Forms, SurveyMonkey, Qualtrics, Calendly), Rich Media & Social (Vimeo, Wistia, Spotify, SoundCloud, Twitch, Pinterest, Apple Music, Reddit), Replit embeds, and Business Intelligence dashboards (Metabase, Tableau, PowerBI) directly into the info panel.
*   **SVG Drill-downs**: Load and seamlessly transition to secondary SVGs, creating hierarchical visual storytelling experiences (e.g. Campus Map -> Building -> Floor).
*   **Responsive Scaling**: Interactive elements adapt flawlessly inside flexible layouts.
*   **Secure by Design**: Implements mitigations against XXE injections during SVG parsing, and sanitizes/escapes JSON configurations to prevent Cross-Site Scripting (XSS).
*   **Multi-View HTML Export**: Bundle multiple SVG views and their logic into a single standalone, offline-capable interactive HTML file.
*   **Data-Driven Choropleths**: Automatically compute and apply color gradients to SVG elements based on a dictionary of numerical values.
*   **Dynamic Markers**: Calculate element bounding boxes and programmatically drop text/icon markers exactly on the SVG map.
*   **Built-in Zoom UI**: Responsive user interface zoom controls natively included in exported interactives, with optional `lock_zoom_out` support to prevent zooming beyond the original scale.
*   **Animation API**: Apply standard CSS keyframe animations (like `pulse` and `fade`) directly to SVG paths to highlight critical regions.
*   **Auto-Generated Legends**: Automatically display interactive data-scale legends for generated choropleth maps.

## Installation

To install SIVO, run:

```bash
pip install -r requirements.txt
```
*(A PyPI release will be available soon as `pip install sivo`)*

## Quick Start

### 1. The Python API (`Sivo`)
SIVO uses a clean, declarative API. Load an SVG, map actions to SVG IDs, and export the interactive web asset.

```python
from sivo import Sivo

# 1. Initialize Sivo from an SVG file
sivo_app = Sivo.from_svg("campus_map.svg")

# 2. Map interactions to SVG element IDs
sivo_app.map(
    element_id="buildingA",
    tooltip="Main Administrative Building",
    html="<h3>Building A</h3><p>Capacity: 500</p>",
    color="#ffcccc",
    hover_color="#ff9999",
    glow=True
)

# Example of an external integration (Data Source & Analytics)
sivo_app.map(
    element_id="buildingC",
    tooltip="Live Occupancy",
    datasource={"provider": "google_sheets", "api_endpoint": "https://api.example.com/buildingC/occupancy"},
    analytics={"provider": "google_analytics", "event_name": "viewed_buildingC"}
)

sivo_app.map(
    element_id="floor1",
    drill_to="buildingA_floor1.svg"
)

# 3. Automatically drop a marker and create a heatmap
sivo_app.add_marker("buildingA", icon="📍", label="Admin")
sivo_app.apply_choropleth({"buildingA": 100, "floor1": 50}, min_color="#ffffff", max_color="#ff0000")

# 4. Export to an interactive HTML bundle
sivo_app.to_html("interactive_map.html")
```

### 2. Streamlit Integration
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

## Tutorials / Examples

We provide extensive examples ranging from basic setup to comprehensive Streamlit dashboards. Check the `examples/` directory for full scripts:

*   **Phase 1: Basic Usage:** Hello World (`examples/01_hello_world`), URL Navigation (`examples/02_url_navigation`), Declarative Configuration (`examples/03_json_config`).
*   **Phase 2: Advanced Standalone Features:** SVG Drill-Downs (`examples/04_drilldowns`), Custom Asset Injection (`examples/05_custom_assets`), HTML/DOM Overlays (`examples/06_html_overlays`), Multi-View Standalone HTML (`examples/07_multi_view_standalone`), Static Choropleths (`examples/08_choropleth`), Dynamic Data Binding & Legend (`examples/08_data_binding`), Animations & Dynamic Markers (`examples/09_animations_markers`), Document Embeds (`examples/10_document_and_map_embed`).
*   **Phase 3: Streamlit Integration:** Basic Callbacks (`examples/10_streamlit_callbacks`), Hover Events (`examples/11_streamlit_hover`), Dynamic Color Updates (`examples/12_dynamic_colors`), Programmatic Zooming (`examples/13_streamlit_zoom`), Comprehensive Dashboard (`examples/14_comprehensive_dashboard`).
*   **Phase 4: External Integrations:** Analytics & Live Data (`examples/22_analytics_and_data`), Forms & E-commerce (`examples/23_forms_and_ecommerce`), Rich Media & Business Intelligence (`examples/24_rich_media_and_bi`), New Integrations (`examples/25_new_integrations`), Nested ECharts Action (`examples/15_echarts_action`), Zoom on Click (`examples/16_zoom_on_click`).
*   **Phase 5: Infographic Narratives:** Scrollytelling (`examples/26_scrollytelling`), Guided Tours (`examples/27_guided_tour`), Dynamic Odometers (`examples/28_odometers`), Minimap & Export (`examples/29_minimap_export`), Layer Toggles (`examples/30_layer_toggles`), Hexbin Maps (`examples/31_hexbin_map`), Dot Density Maps (`examples/32_dot_density_map`), Timeline UI (`examples/46_timeline_playback_ui`).

These examples demonstrate the fully implemented Phase 1, 2, 3, 4, and 5 project goals.

## License
MIT
