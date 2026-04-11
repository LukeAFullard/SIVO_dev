# Chart Helpers Example

This example demonstrates how to use the built-in chart helper methods in Sivo to quickly and easily map standard chart types (like Bar, Line, Pie, and Gauge charts) to elements in an SVG canvas without writing verbose ECharts configuration objects.

## Overview

The purpose of this script is to show how you can attach different types of dynamic charts to specific regions in an SVG map (in this case, simplified state rectangles) and how these charts are rendered in the overlay panel on the right upon interaction. It also tests various customization options like titles, colors, palettes, tooltips, and morphing transitions.

## Key Features Tested

1.  **Bar Chart `map_bar_chart`:**
    *   Creates a bar chart with custom colors for each individual bar using a color palette (`color=["#ef4444", "#f97316", "#eab308", "#22c55e"]`).
    *   Mapped to the `TX` element.

2.  **Line Chart `map_line_chart`:**
    *   Creates a smoothed line chart representing growth trend.
    *   Enables ECharts `universal_transition` to smoothly morph from the Bar chart to the Line chart when switching views.
    *   Injects raw ECharts configuration via `extra_options` to add an area style to the line series.
    *   Mapped to the `CA` element.

3.  **Pie Chart `map_pie_chart`:**
    *   Generates a pie chart to display demographics with its own specific color palette.
    *   Mapped to the `NY` element.

4.  **Gauge Chart `map_gauge_chart`:**
    *   Creates a simple gauge chart representing a single value out of a maximum.
    *   Mapped to the `WY` element.

5.  **Overlay Position:**
    *   Because the default panel position in Sivo is `none`, all `map_*_chart` calls explicitly define `panel_position="right"` (or you can use the global `default_panel_position="right"` when instantiating the app).

## Run the Example

```bash
PYTHONPATH=src python examples/charts/chart_helpers/main.py
```

This will generate `output.html` in the current folder. Open it in a browser to interact with the different regions.
