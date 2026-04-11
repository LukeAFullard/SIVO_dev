# New 2D ECharts Wrappers

This example demonstrates how to use the advanced 2D ECharts wrappers in Sivo. It maps various complex chart types to SVG elements on a grid, allowing users to click each box to reveal a different type of interactive chart in the side panel.

## Key Features Tested
- **Advanced ECharts Integration**: Showcases the use of multiple high-level charting wrappers.
- **Interactive SVG Mapping**: Maps each specific chart type to an individual SVG rectangle (`box1` through `box8`).
- **Side Panel Rendering**: Demonstrates rendering complex visualizations in the default right side panel.
- **Hover Effects**: Adds a visual glow and color change when hovering over the SVG elements.

## Code Highlights

### Initialization
The Sivo application is initialized with `default_panel_position="right"`. This is crucial because the default panel position has changed to `"none"`, which would cause the charts not to display upon clicking if not overridden.

```python
sivo_app = Sivo.from_svg(
    os.path.join(os.path.dirname(__file__), "grid.svg"),
    title="New 2D ECharts Wrappers",
    subtitle="Click any box to view the corresponding advanced ECharts visualization",
    default_panel_position="right"
)
```

### Mapping Charts
Each chart type is mapped to a specific SVG element ID (`element_id`). Sivo provides dedicated methods for each chart type:

*   **Boxplot**: `map_boxplot_chart()`
*   **Candlestick**: `map_candlestick_chart()`
*   **Heatmap**: `map_heatmap_chart()`
*   **Graph (Network)**: `map_graph_chart()`
*   **Sankey Diagram**: `map_sankey_chart()`
*   **Sunburst**: `map_sunburst_chart()`
*   **Parallel Coordinates**: `map_parallel_chart()`
*   **Theme River**: `map_theme_river_chart()`

```python
# Example: Mapping a Sankey Diagram
sankey_nodes = [{"name": "Start"}, {"name": "Path 1"}, {"name": "Path 2"}, {"name": "End"}]
sankey_links = [
    {"source": "Start", "target": "Path 1", "value": 60},
    {"source": "Start", "target": "Path 2", "value": 40},
    {"source": "Path 1", "target": "End", "value": 50},
    {"source": "Path 2", "target": "End", "value": 30}
]
sivo_app.map_sankey_chart(
    element_id="box5",
    title="User Flow Sankey",
    nodes=sankey_nodes,
    links=sankey_links,
    tooltip="View Sankey"
)
```

### Adding Interactive Feedback
A simple loop is used to add hover effects (a color change and a glow) to all the boxes, providing immediate visual feedback to the user.

```python
# Make them interactive on hover
for i in range(1, 9):
    sivo_app.map(f"box{i}", hover_color="#cbd5e1", glow=True)
```
