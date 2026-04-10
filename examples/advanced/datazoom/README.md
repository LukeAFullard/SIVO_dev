# High-Density Scatter Chart with DataZoom

This example demonstrates how to create a high-density scatter chart in SIVO with interactive data zooming enabled. The visualization shows a generated dataset of 1000 points mapped to an SVG container.

## Key Features Showcased
*   **Data Zooming**: The example explicitly enables the ECharts datazoom feature, which adds an interactive slider below the chart, allowing the user to zoom into specific sections of the high-density dataset and pan across the x-axis and y-axis dynamically.
*   **Programmatic Canvas Creation**: A blank SVG container `<svg><rect id="chart-container" .../></svg>` is dynamically constructed as a string in Python, eliminating the need for an external file.

## Code Highlights

### 1. Generating a Large Dataset
A dataset with 1000 data points is generated with mathematical functions to create a pattern that looks appealing when visualized:
```python
data = []
for i in range(1000):
    x = i
    y = math.sin(i / 10.0) * 100 + random.uniform(-10, 10)
    data.append([x, y])
```

### 2. Rendering the Scatter Chart with DataZoom
The `map_scatter_chart` method binds the data to the SVG `chart-container` element. Data zoom functionality is toggled on using `datazoom=True`. Scaling properties are added via `extra_options` to ensure that standard axis mappings dynamically recalculate points:
```python
app.map_scatter_chart(
    element_id="chart-container",
    title="High-Density Scatter with DataZoom",
    data=data,
    color="#43a2ca",
    tooltip="Value: {c}",
    datazoom=True,
    extra_options={
        "xAxis": {"type": "value", "scale": True},
        "yAxis": {"type": "value", "scale": True}
    }
)
```

## Running the Example
To generate the `output.html` file, run the script from the root of the repository:
```bash
PYTHONPATH=src python3 examples/advanced/datazoom/datazoom_example.py
```
After executing, open `examples/advanced/datazoom/output.html` in your browser.
