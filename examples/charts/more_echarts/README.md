# More ECharts Types Demo

This example demonstrates how to use `sivo` to map different types of advanced ECharts to various SVG elements.

## What is being shown
- An interactive SVG canvas created programmatically.
- **Effect Scatter Chart**: Mapped to `rect1` using `map_effect_scatter_chart()`. This shows how to plot scatter points with ripple effects.
- **Lines Chart**: Mapped to `rect2` using `map_lines_chart()`. This displays connected lines across coordinates.
- **Funnel Chart**: Mapped to `rect3` using `map_funnel_chart()`. This showcases a funnel or pyramid-style layout for progressive data.
- **Tree Chart**: Mapped to `rect4` using `map_tree_chart()`. This illustrates hierarchical data as an organization tree structure.

## Relevant Code
In `main.py`, note the setup and the different mapping functions:

```python
# Setup config
config = ProjectConfig(
    svg_file=SVG_FILE,
    title="More ECharts Types Demo",
    subtitle="Demonstrating effectScatter, lines, funnel, and tree",
    theme="light",
    default_panel_position="right"
)

sivo_app = Sivo.from_config(config)

# Map Effect Scatter
sivo_app.map_effect_scatter_chart(
    element_id="rect1",
    title="Effect Scatter",
    data=[...],
    color="#ff3333",
    panel_position="right"
)

# Map Lines
sivo_app.map_lines_chart(
    element_id="rect2",
    title="Lines",
    data=[...],
    color="#3399ff",
    panel_position="right"
)

# Map Funnel
sivo_app.map_funnel_chart(
    element_id="rect3",
    title="Sales Funnel",
    data=[...],
    panel_position="right"
)

# Map Tree
sivo_app.map_tree_chart(
    element_id="rect4",
    title="Organization Tree",
    data=[...],
    panel_position="right"
)
```

## How to run
From the repository root, run:
```bash
PYTHONPATH=src python3 examples/charts/more_echarts/main.py
```
This will output `output.html` in this folder, which you can open in your browser to interact with the different charts.
