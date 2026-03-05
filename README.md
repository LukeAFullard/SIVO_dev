# SIVO (SVG Interactive Vector Objects)

SIVO is a powerful Python framework designed to transform static SVG graphics into responsive, interactive web infographics seamlessly. It allows developers, designers, and data analysts to attach dynamic behaviors—such as tooltips, drill-downs, URL navigation, and dynamic updates—to individual SVG paths or groups without needing to write any complex JavaScript logic.

SIVO acts as the bridge between vector design tools and interactive web data visualization. It supports integration with **Streamlit** for live operational dashboards, and can export standalone interactive HTML bundles.

## Features
*   **Zero-JavaScript Setup**: Define interactions purely in Python or via declarative JSON configurations.
*   **Streamlit Integration**: A native V2 Custom Component is provided for seamless embedding and bidirectional data flow in Streamlit applications.
*   **Complex SVG Handling**: Automatically normalizes complex SVGs, including correctly handling nested `<g>` tags and `<use>` symbol references.
*   **Rich Behaviors**: Attach custom tooltips (supporting HTML content via Shadow DOM), URL navigation, state/callback events, and visual styling changes to any SVG element.
*   **SVG Drill-downs**: Load and seamlessly transition to secondary SVGs, creating hierarchical visual storytelling experiences (e.g. Campus Map -> Building -> Floor).
*   **Responsive Scaling**: Interactive elements adapt flawlessly inside flexible layouts.

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

sivo_app.map(
    element_id="floor1",
    drill_to="buildingA_floor1.svg"
)

# 3. Export to an interactive HTML bundle
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

## License
MIT
