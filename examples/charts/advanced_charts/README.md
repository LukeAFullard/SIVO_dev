# Advanced Chart Types

This example demonstrates how to integrate various advanced chart types into an interactive SVG visualization using SIVO.
These advanced chart types provide rich visualizations for multi-dimensional data, cyclical trends, comparisons, and custom plotting.

## Overview

The script initializes a SIVO orchestrator from an inline SVG layout that contains multiple defined shapes (`polar_bar`, `polar_line`, `polar_scatter`, `liquid_fill`, and `custom_series`).

When you run this example, it generates an `output.html` file which features an interactive canvas. By clicking on these shapes, a side panel (rendered by setting `default_panel_position="right"` in the instantiation) opens, revealing corresponding Apache ECharts visualizations.

### What is Being Demonstrated:

1. **Polar Bar Chart:** A standard bar chart, but wrapped around a polar coordinate system. This is mapped to the `polar_bar` shape.
   ```python
   app.map_polar_bar_chart(
       element_id="polar_bar",
       title="Revenue by Region",
       data=[120, 200, 150, 80],
       categories=["North", "South", "East", "West"],
       color=["#38bdf8", "#818cf8", "#c084fc", "#e879f9"]
   )
   ```

2. **Polar Line Chart:** Great for continuous cyclical time-series data or math functions mapped in polar coordinates. A sine wave is mathematically generated and mapped to `polar_line`.
   ```python
   import math
   math_data = [math.sin(i * math.pi / 180) * 10 for i in range(0, 360, 5)]
   app.map_polar_line_chart(
       element_id="polar_line",
       title="Cyclical Trends",
       data=math_data,
       color="#10b981"
   )
   ```

3. **Polar Scatter Chart:** For plotting data points natively around an origin. This is mapped to the `polar_scatter` shape using a set of radial coordinates `[radius, angle]`.

4. **Liquid Fill Chart:** This chart renders engaging animated wave charts to display percentage thresholds. It is mapped to the `liquid_fill` element.

5. **Custom Series Chart:** Demonstrates how you can use JavaScript inside Python to build highly customized visual components (like a Gantt Chart) inside ECharts via SIVO, and map them to the `custom_series` shape.

### Key Settings

- `default_panel_position="right"` ensures that all clicked interactive charts render cleanly in a side panel on the right side of the screen.
- `disable_zoom_controls=True` focuses the view on simple clicking interactions without canvas panning/zooming.
- Note how general theme options like `hover_color` are mapped independently using `app.map()` to apply standardized hover states across all SVG elements before their specific chart data is injected.

## Running the Example

Make sure SIVO and its dependencies are installed, then run:

```bash
PYTHONPATH=src python examples/charts/advanced_charts/main.py
```

Open the generated `output.html` in your browser.