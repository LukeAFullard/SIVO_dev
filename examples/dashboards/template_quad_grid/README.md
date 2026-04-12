# Quad Grid Dashboard Example

This example demonstrates how to use the `SivoDashboard.set_grid_layout()` method to create a clean 2x2 grid layout. The explicit grid areas map to corresponding layout areas ensuring that every block correctly displays in a quadrant. It is particularly useful for creating highly symmetrical, high-level overview dashboards.

## Overview

In this example, we configure four components:
1. **Top Left**: A `Sivo` map block. Clicking the `quadrant_1` region dispatches a payload.
2. **Top Right**: A metrics panel. This catches the dispatched payload (e.g., `metric_val`) and displays it.
3. **Bottom Left**: Another `Sivo` map block showing a different focus.
4. **Bottom Right**: A details panel. Clicking on map regions will dynamically update this panel with the details mapped in the `tooltip` property.

By using `default_panel_position='none'` (which is the default when instantiating `Sivo` via `.from_template()`), the internal popup overlays are disabled in favor of using these external dashboard components to render the interaction details.

## Code Summary

```python
from sivo.core.dashboard import SivoDashboard
# ...
dashboard = SivoDashboard(title="KPI Overview")

# Set CSS Grid layout areas for desktop and mobile views
dashboard.set_grid_layout(
    desktop='''
    "tl tr"
    "bl br"
    ''',
    mobile='''
    "tl"
    "tr"
    "bl"
    "br"
    '''
)

# 1. Top Left - Map Block
tl_map = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)
tl_map.map("quadrant_1", color="#3b82f6", hover_color="#2563eb", tooltip="Primary Region", callback_payload={"metric_val": "$1.2M"})
dashboard.add_sivo_block("sales_map", tl_map, grid_area="tl")

# 2. Top Right - Metrics Panel
dashboard.add_metrics_panel(
    "sales_metrics",
    title="Sales KPIs",
    metrics=["metric_val"],
    grid_area="tr"
)

# 3. Bottom Left - Map Block
bl_map = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)
bl_map.map("quadrant_4", color="#ef4444", hover_color="#dc2626", tooltip="Critical Region")
dashboard.add_sivo_block("issues_map", bl_map, grid_area="bl")

# 4. Bottom Right - Details Panel
dashboard.add_details_panel(
    "analysis_details",
    title="Detailed Analysis",
    placeholder="Select a region on the map.",
    grid_area="br"
)
```

## Running the Example

Run the following command from the root directory to generate the dashboard:

```bash
PYTHONPATH=src python examples/dashboards/template_quad_grid/main.py
```

This will generate an `output.html` file within this example directory. You can open it in any web browser to see the interactive 2x2 grid layout and test the clicks between the map regions and the detailed panels.
