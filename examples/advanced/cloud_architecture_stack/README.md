# Cloud Architecture Stack Example

This example demonstrates how to use SIVO to build an interactive cloud architecture diagram using a built-in premium SVG template.

## Features Demonstrated

- **Template Loading**: `Sivo.from_svg` is used to load a specific SVG template (`premium_layer_stack_2026.svg`).
- **Template Styling**: `app.apply_template_style("cyberpunk")` applies a predefined visual style to the template.
- **Dynamic Text Placement**: `app.fill_template_zone()` replaces placeholder text elements in the SVG with custom labels, descriptions, and styling (fonts, colors, alignment).
- **Embedded Charts**:
  - `app.map_treemap_chart()` replaces an SVG element with an interactive ECharts Treemap to represent the "Data Tier" storage distribution.
  - `app.map_graph_chart()` replaces an SVG element with a Force-Directed Graph to visualize "Logic Tier" microservice topology.

## Running the Example

From the root of the repository, run:

```bash
PYTHONPATH=src python3 examples/advanced/cloud_architecture_stack/main.py
```

This will generate a `cloud_architecture.html` file in this directory.
