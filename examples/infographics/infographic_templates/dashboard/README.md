# Dashboard Infographic Template Example

This example demonstrates how to build an interactive dashboard infographic using SIVO's built-in `3_2/dashboard` template.

## Features Demonstrated

*   **`Sivo.from_template()`**: Loading a built-in template SVG.
*   **HTML Overlays**: Adding rich HTML content (headers, metrics) directly onto specific areas of the dashboard template using `add_overlay()`. The HTML is styled to be responsive using `container-type: inline-size` and `clamp()`.
*   **Interactive ECharts**: Binding interactive ECharts (a line chart for performance and a pie chart for regional sales) to specific SVG elements (e.g., `main_chart_area`, `sidebar_area_top`) using the `map()` method. The `panel_position="overlay"` is used to show these details upon interaction.
*   **Interactive Widgets**: Binding a simple HTML widget (Markdown/Info) to a sidebar area.

## Code Highlights

```python
# Load the dashboard template
dashboard = Sivo.from_template("3_2/dashboard", default_panel_position="none")

# Add a metric overlay
metric1_html = """
<div style="text-align: center; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; box-sizing: border-box; padding: 5%; container-type: inline-size;">
    <h3 style="margin: 0; color: #888; font-family: sans-serif; font-size: clamp(8px, 5cqw, 18px);">Total Revenue</h3>
    <p style="margin: 5px 0 0 0; color: #2ecc71; font-family: sans-serif; font-size: clamp(16px, 12cqw, 48px); font-weight: bold;">$12.5M</p>
</div>
"""
dashboard.add_overlay("metric_1", metric1_html)

# Map an interactive EChart to an area
dashboard.map(
    element_id="main_chart_area",
    panel_position="overlay",
    html="<h3>Monthly Sales Performance</h3><p>Click to view full sales chart</p>",
    echarts_option=main_chart_option,
    hover_color="#f1f5f9"
)
```

## Running the Example

Run the following command from the root directory:

```bash
PYTHONPATH=src python3 examples/infographics/infographic_templates/dashboard/main.py
```

This will generate an `output.html` file in the same directory, containing the interactive dashboard.
