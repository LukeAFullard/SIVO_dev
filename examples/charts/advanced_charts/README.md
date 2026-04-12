# Advanced Charts Example

This example demonstrates how to use SIVO to natively map several advanced chart types to SVG elements.

## Features Demonstrated

- **Polar Bar Chart:** A bar chart wrapped around a polar coordinate system. Configured using `app.map_polar_bar_chart()`.
- **Polar Line Chart:** A line chart for cyclical time-series or mathematical functions around a polar coordinate system. Configured using `app.map_polar_line_chart()`.
- **Polar Scatter Chart:** A scatter plot on a polar coordinate system (data format `[radius, angle]`). Configured using `app.map_polar_scatter_chart()`.
- **Liquid Fill Chart:** Represents percentages as waves within a shape, utilizing the `echarts-liquidfill` plugin. Configured using `app.map_liquidfill_chart()`.
- **Custom Series (Gantt Chart):** Uses a completely custom JavaScript `renderItem` function (`app.map_custom_chart()`) to draw non-standard shapes or diagrams, allowing you to create customized visual mappings like timelines.

## Key Code Snippets

### Mapping a Polar Chart
```python
app.map_polar_bar_chart(
    element_id="polar_bar",
    title="Revenue by Region",
    data=[120, 200, 150, 80],
    categories=["North", "South", "East", "West"],
    color=["#38bdf8", "#818cf8", "#c084fc", "#e879f9"]
)
```

### Implementing a Custom Series (Gantt Chart)
```python
custom_render_js = """
function (params, api) {
    // ... custom geometry definition ...
    return rectShape && {
        type: 'rect',
        transition: ['shape'],
        shape: rectShape,
        style: api.style({ fill: api.visual('color') })
    };
}
"""

app.map_custom_chart(
    element_id="custom_series",
    title="Project Timeline (Custom Gantt)",
    render_item_js=custom_render_js,
    data=gantt_data,
    extra_options={
        "xAxis": {"type": "value", "scale": True},
        "yAxis": {"type": "category", "data": ["Team 1", "Team 2", "Team 3"]},
        "tooltip": {
            "formatter": "function(params) { return params.name + ': ' + params.value[1] + ' to ' + params.value[2]; }"
        }
    }
)
```

## Running the Example

Run the script from the root directory:
```bash
PYTHONPATH=src python3 examples/charts/advanced_charts/main.py
```
This will generate an `output.html` file that you can open in your browser to view and interact with the mapped elements.
