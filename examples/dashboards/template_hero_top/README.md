# Template Hero Top Dashboard

This example demonstrates how to create a responsive dashboard with a "hero top" layout using the CSS Grid functionality in `SivoDashboard.set_grid_layout()`.

## Purpose
The purpose of this example is to show how to use the `SivoDashboard` to arrange multiple interactive Sivo blocks into a structured, responsive layout where a single primary visualization spans the full width at the top (the "hero" section), followed by smaller secondary blocks displayed in a grid below.

This approach is highly useful for analytics dashboards that feature a global overview map or key metrics at the top, paired with drill-down charts underneath.

## Key Features Demonstrated

- **CSS Grid Layouts:** Using `dashboard.set_grid_layout()` to define structured `'hero'` and `'col'` areas.
- **Responsive Design:** Using different layout definitions for `desktop` and `mobile` views, collapsing the columns onto new rows on mobile.
- **Block Assignment:** Adding independent interactive `Sivo` blocks into designated grid areas via `dashboard.add_sivo_block(..., grid_area="hero")`.
- **Layout Sizing:** Modifying the `layout_size` argument to make certain views fill their containers completely (`layout_size="100%"` for the hero) while adding padding to others (`layout_size="80%"` for secondary blocks).

## Relevant Code Snippets

Creating the dashboard layout and assigning blocks to grid areas:

```python
# Create the dashboard
dashboard = SivoDashboard(title="Hero Top HTML Template Example")

# Define responsive CSS grid layout
dashboard.set_grid_layout(
    desktop='''
    "hero hero hero"
    "col1 col2 col3"
    ''',
    mobile='''
    "hero"
    "col1"
    "col2"
    "col3"
    '''
)

# Assign Sivo blocks to specific grid areas
dashboard.add_sivo_block("fleet_map", sivo_map, grid_area="hero")

# Add a Details Panel to automatically render `html` details from map clicks
dashboard.add_details_panel("log_details", title="Data Center Logs", placeholder="Select a region to view its logs.", grid_area="col3")

dashboard.add_sivo_block("chart_1", sivo_chart, grid_area="col1")
dashboard.add_sivo_block("chart_2", sivo_chart, grid_area="col2")
```

The example maps regions using `.map()` on the "fleet_map" Sivo instance, assigning custom `html` payloads. Because the default `panel_position` is explicitly set to `"none"` on the Sivo object, clicks will interact natively with the overall dashboard grid structure, routing those `html` payloads directly into the `.add_details_panel()` instance without triggering duplicate internal side panels on the ECharts canvas itself.
