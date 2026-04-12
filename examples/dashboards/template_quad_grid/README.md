# Quad Grid Template Example

This example demonstrates how to use the `SivoDashboard` with a CSS grid layout to create a cleanly proportioned 2x2 grid. By utilizing `set_grid_layout()`, developers can assign different blocks to specific quadrants, ensuring a highly symmetrical, high-level overview dashboard on desktop displays and a simple stacked view on mobile displays.

## Purpose

The example highlights how to combine standard `Sivo` blocks with dashboard specific components:
*   Two SVG-based visualizations utilizing the built-in `dashboards/four_quadrants` template.
*   An integrated `metrics_panel` designed to parse and render data emitted by mapping interactions.
*   An integrated `details_panel` designed to capture rich HTML content from selected objects.

This setup prevents the need for a single, monolithic SVG file and shows how separate blocks can interact within the standard SIVO interactive state.

## Implementation Details

1.  **Grid Layout Definition**: The dashboard's structural layout is explicitly mapped via `set_grid_layout()`, mapping `tl`, `tr`, `bl`, and `br` grid areas for desktop and mobile devices.
2.  **Adding Sivo Blocks**: The top-left (`tl`) and bottom-left (`bl`) sections contain individual Sivo blocks. They utilize the `.map()` method to bind interaction handlers, with an added `html` string for the detailed panel and a `callback_payload` dictionary containing the `metric_val`. Note that the `panel_position` is left to its default (`none`), which disables the block's built-in panel in favor of the dashboard panels.
3.  **Metrics Panel**: The top-right (`tr`) quadrant contains a dedicated `add_metrics_panel()`. It is specifically instructed to look for the `metric_val` key inside the `callback_payload` generated when users interact with the map blocks.
4.  **Details Panel**: The bottom-right (`br`) quadrant contains a dedicated `add_details_panel()`. Whenever an element mapped with an `html` property is clicked, the HTML content automatically cascades into this pane.

## Usage

You can review the setup in `main.py`:

```python
from sivo.core.dashboard import SivoDashboard

# Create the Dashboard and configure a 2x2 grid
dashboard = SivoDashboard(title="KPI Overview")
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

# ... Setup tl_map ...

# Bind tl_map to the Top-Left area
dashboard.add_sivo_block("sales_map", tl_map, grid_area="tl")

# Bind a Metrics panel to the Top-Right area
dashboard.add_metrics_panel(
    "sales_metrics",
    title="Sales KPIs",
    metrics=["metric_val"],
    grid_area="tr"
)

# ... Setup bl_map ...

# Bind bl_map to the Bottom-Left area
dashboard.add_sivo_block("issues_map", bl_map, grid_area="bl")

# Bind a Details panel to the Bottom-Right area
dashboard.add_details_panel(
    "analysis_details",
    title="Detailed Analysis",
    placeholder="Select a region on the map.",
    grid_area="br"
)

# Export the completed dashboard
dashboard.to_html("output.html")
```
