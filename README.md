# SIVO (SVG Interactive Vector Objects)

SIVO is a powerful Python framework that transforms static vector graphics (SVGs) into responsive, interactive web infographics and data-driven dashboards—all without writing a single line of JavaScript.

## What Problem Does SIVO Solve?
Designers and data analysts frequently create beautiful vector maps, diagrams, and illustrations, but making these assets interactive on the web usually requires tedious front-end development. You have to handle DOM events, responsive scaling across devices, viewport zooming, and coordinate mapping.

SIVO solves this by letting you define interactions directly from Python or via declarative JSON. Whether you need to turn an architectural floor plan into a live occupancy dashboard, or make a static infographic clickable with pop-up charts, SIVO automatically handles the heavy lifting. It bridges the gap between static vector design tools and rich, interactive web visualization.

## Capabilities
* **Zero-JavaScript Interactivity:** Attach tooltips, external links, animations, and custom HTML side-panels to any element in an SVG just by referencing its ID.
* **Complex SVG Handling:** Automatically normalizes complex SVGs, natively supporting nested `<g>` groups and `<use>` symbol references.
* **Dynamic Visuals:** Instantly build data-driven choropleths (heatmaps) and drop programmatic text/icon markers exactly where you need them.
* **Animations:** Apply standard CSS keyframe animations (like `pulse`, `glow`, and `fade`) to highlight critical SVG paths or regions.
* **Responsive & Mobile-Ready:** Interactive elements adapt flawlessly inside flexible layouts, complete with built-in UI zoom controls.
* **Two Operating Modes:** Use SIVO to build standalone **Infographics** or embed them inside rich **Dashboards** with side-by-side metric panels.
* **Streamlit Integration:** Seamlessly embed your creations into Streamlit apps with a native V2 Custom Component that supports bidirectional data flow.
* **External Integrations:** Easily hook into Google Analytics, data sources (Google Sheets, Notion APIs), and embeds for YouTube, Vimeo, Typeform, and more.
* **Export Anywhere:** Bundle your visualizations into single, offline-capable HTML files, perfect for sharing or embedding via iframes.

---

## 🎨 1. Infographic Mode

**Infographic Mode** focuses on the graphic itself. It creates a rich, full-screen interactive asset out of a single or multiple connected SVGs. This mode is perfect for storytelling, scrollytelling, or creating interactive maps with pop-up tooltips and drill-downs.

### Key Features of Infographic Mode:
* **Rich Tooltips & Popups:** Hover over regions to see text, dynamic data, or even rich HTML content.
* **Drill-Downs:** Click on a region (e.g., a country) to smoothly transition to a secondary SVG (e.g., a state map), creating hierarchical visual storytelling.
* **Choropleths & Heatmaps:** Pass a dictionary of numerical values to automatically color-code SVG elements.
* **Built-in Presentation:** Guide users through specific SVG elements using custom camera pans and zooms.

### Example: Interactive Campus Map
```python
from sivo import Sivo

# 1. Initialize Sivo from a static SVG file
sivo_app = Sivo.from_svg("campus_map.svg")

# 2. Attach interactions to an SVG element ID
sivo_app.map(
    element_id="buildingA",
    tooltip="Main Administrative Building",
    html="<h3>Building A</h3><p>Capacity: 500</p>",
    hover_color="#ff9999",
    glow=True
)

# 3. Create a drill-down experience
sivo_app.map(
    element_id="floor1",
    drill_to="buildingA_floor1.svg"
)

# 4. Generate a choropleth map automatically
sivo_app.apply_choropleth({"buildingA": 100, "floor1": 50}, min_color="#ffffff", max_color="#ff0000")

# 5. Export as a standalone interactive HTML file
sivo_app.to_html("interactive_map.html")
```

---

## 📊 2. Dashboard Mode

**Dashboard Mode** takes your infographics to the next level by placing them inside a responsive CSS Grid layout alongside other content blocks. While an infographic is a single visual, a **Dashboard** lets you build a full analytical application around it.

Clicking an element on your SVG infographic can dynamically update text panels, image blocks, and metric readouts elsewhere on the screen!

### Key Features of Dashboard Mode:
* **Responsive CSS Grid Layout:** Build side-by-side or stacked layouts without writing CSS. It automatically stacks gracefully on mobile devices.
* **Interconnected Blocks:** Configure "Details Panels" or "Metrics Panels" that listen for clicks on your SIVO map to reveal deeper insights.
* **Rich Component Library:** Add markdown text blocks, raw HTML blocks, image blocks, and external embeds around your main visualization.

### Example: Campus Overview Dashboard
```python
from sivo import Sivo, SivoDashboard

# 1. Create the base infographic
sivo_map = Sivo.from_svg("campus_map.svg")
sivo_map.map(
    "buildingA",
    html="<p>This is the main facility.</p>",
    callback_payload={"revenue": "$1.2M", "status": "Active"}
)

# 2. Initialize the Dashboard layout
dashboard = SivoDashboard(title="Campus Overview")

# 3. Add the infographic to the dashboard
dashboard.add_sivo_block("map", sivo_map)

# 4. Add interactive side-panels that respond to map clicks
dashboard.add_details_panel("details", title="Building Details")
dashboard.add_metrics_panel("metrics", title="Live Data", metrics=["revenue", "status"])

# 5. Export the entire dashboard application
dashboard.to_html("dashboard.html")
```

---

## 🚀 Streamlit Integration

Need more than a static HTML export? SIVO includes a native Streamlit component to embed your interactive SVGs into your Streamlit apps and receive click events directly back into your Python runtime.

```python
import streamlit as st
from sivo import Sivo
from sivo.streamlit.component import sivo_component

st.title("Streamlit Interactive Map")

sivo_app = Sivo.from_svg("campus_map.svg")
sivo_app.map(
    element_id="buildingB",
    tooltip="Engineering Block",
    callback_payload={"building_id": "B"}
)

# The component returns data when a user clicks the map!
result = sivo_component(sivo_app, key="campus_map")

if result:
    st.write("You clicked on:", result)
```

## ⚙️ Installation

To install SIVO, run:

```bash
pip install -r requirements.txt
```
*(A PyPI release will be available soon as `pip install sivo`)*

## 📚 Structure & Advanced Usage

SIVO is built on solid foundations, parsing and normalizing SVGs using `lxml`, managing structured configurations with `pydantic`, and using `Jinja2` with `Apache ECharts` on the frontend for high-performance rendering.

Advanced capabilities include:
* **End-to-End Testing:** Enable `ProjectConfig.enable_e2e_testing` for comprehensive Playwright visual regression tests across your interactives.
* **Local Asset Bundling:** Want to avoid CDN dependencies? SIVO can bundle JS and CSS locally for strict offline deployments.
* **Real-time Telemetry:** Connect directly to WebSocket or PubSub brokers to update graphics live without refreshing.
* **JSON Configuration:** Instead of Python scripts, entire interactives can be defined declaratively in JSON files and built via the command line (`python -m sivo export config.json`).

Check the `examples/` directory in this repository for over 30 complete project tutorials spanning basic "Hello World" implementations to complex Hexbin Maps, Guided Tours, and Timeline UI playbacks.

## 📄 License
MIT
