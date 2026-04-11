# Analytics Dashboard Example

This example demonstrates how to build a complex, responsive layout using the CSS Grid Builder feature of `SivoDashboard`. It integrates standard SIVO interactive charts with raw HTML blocks and cross-block communication panels (Details and Metrics).

## Purpose

The main goal of this example is to show how to assemble a dashboard using `SivoDashboard.set_grid_layout()`, effectively moving away from the deprecated monolithic template engine to a flexible, user-defined CSS grid. It illustrates how different types of components (raw HTML KPIs, SIVO interactive SVG charts, details viewers, and metrics panels) can be mapped onto specific regions ("grid areas") of a responsive desktop and mobile layout.

Furthermore, it showcases the built-in reactivity of `SivoDashboard`, where `add_details_panel` and `add_metrics_panel` automatically listen to clicks on the `add_sivo_block` charts and dynamically update their content based on the target element's mapped data (`tooltip` -> details, `callback_payload` -> metrics).

## Key Code Snippets

### Setting the Responsive Layout

The dashboard's skeleton is defined using standard CSS `grid-template-areas`. This allows exact placement of widgets. Note the distinction between the desktop layout (multi-column) and mobile layout (single continuous column).

```python
dashboard = SivoDashboard(title="Acme Analytics", columns=3)
dashboard.set_grid_layout(
    desktop='''
"kpi1 kpi2 kpi3 kpi3"
"main main side side"
"bottom1 bottom1 bottom2 bottom2"
    ''',
    mobile='''
"kpi1"
"kpi2"
"kpi3"
"main"
"side"
"bottom1"
"bottom2"
    '''
)
```

### Adding Different Block Types

Components are attached to the dashboard by referencing their designated `grid_area`.

```python
# Raw HTML blocks for static/simple KPIs
dashboard.add_html_block("stat_users", html_stat1, grid_area="kpi1")

# Interactive SIVO SVG charts
dashboard.add_sivo_block("revenue_trend", sivo_bar, grid_area="main")
dashboard.add_sivo_block("user_demographics", sivo_pie, grid_area="side")

# Pre-built panels that listen to clicks on the charts above
dashboard.add_details_panel("quarter_details", title="Quarter Breakdown", grid_area="bottom1")
dashboard.add_metrics_panel("selected_stats", title="Selection Overview", metrics=["selected_quarter", "revenue"], grid_area="bottom2")
```

### Data Mapping for Panels

The charts themselves are mapped with payloads that the Metrics panel extracts upon interaction.

```python
sivo_bar.map("bar1", hover_color="#2563eb", tooltip="Q1 Revenue: $15,000", callback_payload={"selected_quarter": "Q1", "revenue": "$15k"})
```

When `bar1` is clicked, the `selected_stats` metrics panel will automatically update to display the `selected_quarter` and `revenue` values. The `quarter_details` details panel will display the `tooltip` text.

## Running the Example

Make sure SIVO is installed or run the script with `PYTHONPATH=src`:
```bash
PYTHONPATH=src python examples/dashboards/template_analytics_dashboard/main.py
```
This will generate an `output.html` file in the same directory.
