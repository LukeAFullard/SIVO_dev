# Dashboard Blocks Example

## Overview
This example demonstrates how to build a complex, multi-block responsive dashboard without writing any HTML or JavaScript using SIVO. It introduces `SivoDashboard` as a way to construct web pages using interactive "Blocks."

This is particularly useful when you need to assemble different visualizations (maps, charts, images) alongside dedicated context panes, creating a cohesive visual application.

## What is being tested/shown
1. **`SivoDashboard` composition**: Shows how to group multiple SIVO elements.
2. **`add_sivo_block`**: Maps standalone SVGs into a responsive dashboard grid.
3. **`add_details_panel`**: Pre-built block that automatically renders rich media `html` content mapped onto SIVO elements when they are clicked.
4. **`add_metrics_panel`**: Pre-built block that extracts structured data passed into `callback_payload` and presents it dynamically.
5. **Overriding side panels**: Demonstrates how specific elements (e.g., `"region_south"`) can override the inline grid panels to reveal a sliding global sidebar.

## Key Code Snippets

```python
from sivo import Sivo, SivoDashboard

# Create individual SIVO blocks
sivo_map = Sivo.from_string(map_svg, theme="light", default_panel_position="none")
sivo_chart = Sivo.from_string(chart_svg, theme="light", default_panel_position="none")

# Map rich content
sivo_map.map(
    "region_north",
    html=north_html_content,  # Contains <img>
    panel_position="none",    # Update the details panel inside the grid
    callback_payload={"revenue": "$1.2M"}
)

sivo_map.map(
    "region_south",
    html=south_html_content,  # Contains <iframe>
    panel_position="right",   # Overrides the grid with a sliding side panel
    callback_payload={"revenue": "$0.8M"}
)

# Assemble dashboard
dashboard = SivoDashboard(title="Executive Operations Dashboard")

dashboard.add_sivo_block("regional_map", sivo_map)
dashboard.add_details_panel("region_details", title="Region Details")
dashboard.add_metrics_panel("region_metrics", title="Key Metrics", metrics=["revenue", "users", "status"])
dashboard.add_sivo_block("quarterly_chart", sivo_chart)

# Export
dashboard.to_html("output.html")
```

## How to Run

From the repository root, ensuring your PYTHONPATH is set to resolve internal modules:

```bash
PYTHONPATH=src python3 examples/dashboards/dashboard_blocks_example/main.py
```
This generates `output.html`. Open it in any modern web browser to interact with the multi-block layout.
