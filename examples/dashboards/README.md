# SIVO Dashboards Examples

This folder contains examples demonstrating how to use the `SivoDashboard` feature.

`SivoDashboard` allows you to create responsive, multi-block dashboards using CSS Grid. Instead of being constrained to a single monolithic SVG canvas, you can arrange multiple interactive maps, charts, and dynamically generated data panels side-by-side.

## Key Features Demonstrated

- **Multi-Block Layouts**: How to initialize a dashboard and add multiple standard `Sivo` blocks (`dashboard.add_sivo_block()`).
- **No-Code Interactivity**: How to natively wire up ECharts click interactions to side-panels using Python mappings (`dashboard.add_details_panel()` and `dashboard.add_metrics_panel()`).
- **Rich Media Support**: How to pass standard HTML (including `<img>` and `<iframe>` tags) into a mapping's `html` argument so it renders dynamically in a pre-built Details panel.

## Snippet Highlight

The core structure of a dashboard is built like this:

```python
from sivo import Sivo, SivoDashboard

# Initialize the Dashboard container
dashboard = SivoDashboard(title="Executive Operations Dashboard")

# 1. Add an interactive map (built from an SVG string or file)
dashboard.add_sivo_block("regional_map", sivo_map)

# 2. Add a pre-built Details Panel to render rich media
dashboard.add_details_panel("region_details", title="Region Details", placeholder="Select a region on the map to view rich media details.")

# 3. Add a pre-built Metrics Panel to render payload data
dashboard.add_metrics_panel("region_metrics", title="Key Metrics", metrics=["revenue", "users", "status"])

# 4. Add a secondary SVG block (e.g. a static chart)
dashboard.add_sivo_block("quarterly_chart", sivo_chart)

# Export the entire reactive grid layout to a single HTML file
dashboard.to_html("output/dashboard_blocks_example.html")
```
