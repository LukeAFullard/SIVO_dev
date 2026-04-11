# Template Sidebar Right Layout

This example demonstrates how to create a responsive multi-block dashboard layout using the **SivoDashboard** CSS Grid Builder functionality to construct a Right Sidebar layout.

## What is being tested/shown

1. **Responsive CSS Grid Configuration:**
   Using `dashboard.set_grid_layout()`, the dashboard defines a responsive layout where on desktop, the main content takes up the left space while two interaction panels are stacked vertically on the right. On mobile devices, the items stack vertically.
2. **Assigning Grid Areas:**
   The `Sivo` visualization blocks, as well as the detail and metric panels, are explicitly mapped to these CSS grid areas (e.g. `grid_area="main"` or `grid_area="sidebar1"`).
3. **Interactive Metric and Detail Panels:**
   The map incorporates `tooltip` and `callback_payload` data properties which automatically reflect into the explicitly mapped metric and detail panels on click.

## Code highlights

### Setting up the Grid

```python
    # By specifying the CSS Grid layout, SivoDashboard builds a responsive right-sidebar view
    dashboard = SivoDashboard(title="Right Sidebar Layout HTML Template Example", columns=1)
    dashboard.set_grid_layout(
        desktop='''
    "main sidebar1"
    "main sidebar2"
        ''',
        mobile='''
    "main"
    "sidebar1"
    "sidebar2"
        '''
    )
```

### Adding and Positioning Dashboard Blocks

```python
    # Assign the map to the 'main' content slot
    dashboard.add_sivo_block("global_map", sivo_map, grid_area="main")

    # Assign interaction panels to the 'sidebar' slots
    dashboard.add_metrics_panel("metrics", title="Node Metrics", metrics=["status", "latency"], grid_area="sidebar1")
    dashboard.add_details_panel("details", title="Node Details", grid_area="sidebar2")
```
