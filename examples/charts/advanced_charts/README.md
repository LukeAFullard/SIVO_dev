# Advanced Charts Example

This example demonstrates how to use SIVO to natively map several advanced chart types to SVG elements.

## Features Demonstrated

- **Polar Bar Chart:** A bar chart wrapped around a polar coordinate system. Configured using `app.map_polar_bar_chart()`.
- **Polar Line Chart:** A line chart for cyclical time-series or mathematical functions around a polar coordinate system. Configured using `app.map_polar_line_chart()`.
- **Polar Scatter Chart:** A scatter plot on a polar coordinate system (data format `[radius, angle]`). Configured using `app.map_polar_scatter_chart()`.
- **Liquid Fill Chart:** Represents percentages as waves within a shape, utilizing the `echarts-liquidfill` plugin. Configured using `app.map_liquidfill_chart()`.
- **Radar Chart:** Displays multidimensional data against multiple quantitative variables. Configured using `app.map_radar_chart()`.

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

### Implementing a Radar Chart
```python
radar_indicators = [
    {"name": "Sales", "max": 6500},
    {"name": "Administration", "max": 16000},
    # ... more indicators
]
radar_data = [
    {
        "value": [4200, 3000, 20000, 35000, 50000, 18000],
        "name": "Allocated Budget"
    },
    {
        "value": [5000, 14000, 28000, 26000, 42000, 21000],
        "name": "Actual Spending"
    }
]
app.map_radar_chart(
    element_id="radar_chart",
    title="Budget vs Spending",
    indicators=radar_indicators,
    data=radar_data,
    color=["#f59e0b", "#10b981"]
)
```

## Running the Example

Run the script from the root directory:
```bash
PYTHONPATH=src python3 examples/charts/advanced_charts/main.py
```
This will generate an `output.html` file that you can open in your browser to view and interact with the mapped elements.
