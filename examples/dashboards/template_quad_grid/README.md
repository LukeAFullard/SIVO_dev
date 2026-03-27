# Quad Grid Template Example

This example demonstrates how to use the `quad_grid.html` dashboard template. The template provides a clean 2x2 grid layout where every block automatically assumes a square aspect ratio. It is useful for creating highly symmetrical, high-level overview dashboards.

## Usage

```python
from sivo.core.dashboard import SivoDashboard
# ...
dashboard = SivoDashboard(title="KPI Overview", template="quad_grid")
# Add exactly 4 blocks to fill the grid
dashboard.add_sivo_block("sales_map", tl_map)
dashboard.add_metrics_panel("sales_metrics", title="Sales KPIs", metrics=["metric_val"])
dashboard.add_sivo_block("issues_map", bl_map)
dashboard.add_details_panel("analysis_details", title="Detailed Analysis", placeholder="Select a region on the map.")
```
