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

## Visual Gallery & Use Cases

SIVO is incredibly versatile. It's used for:
*   **Interactive Maps**: Campus layouts, seating charts, architectural diagrams.
*   **Data Dashboards**: Binding live data to floor plans or schematic diagrams.
*   **Presentations**: Scrollytelling and guided visual tours.
*   **Data-driven Visualizations**: Choropleth maps and hexbins without geospatial setups.

See the [Visual Gallery](examples/gallery.md) for screenshots and full code examples!

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
