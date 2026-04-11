# Sidebar Left Layout Dashboard Example

This example demonstrates how to build a responsive dashboard with a "sidebar left" layout using `SivoDashboard` and its modern CSS Grid functionality.

## Purpose

The main goal of this example is to show how to arrange interactive components using `dashboard.set_grid_layout()`. The dashboard contains a central SVG map and two sidebar panels (a metrics panel and a details panel) that update interactively based on clicks in the SVG map.

## Key Features Demonstrated

- **CSS Grid Layout (`set_grid_layout`)**: Defines a robust layout with custom responsive arrangements for desktop (`sidebar1 main main`) and mobile (`main`, `sidebar1`, `sidebar2`).
- **Fixed Grid Tracks (Preventing Jumps)**: By default, a CSS grid auto-sizes columns based on its content. This means clicking an interactive node and populating a sidebar panel with text could cause the grid to awkwardly shift and resize. We prevent this by injecting `grid-template-columns: 350px 1fr 1fr;` into the layout string, ensuring a rigid layout.
- **Sivo Block Integration**: Assigning a primary interactive canvas to a specific grid area using `dashboard.add_sivo_block(..., grid_area="main")`.
- **Metrics Panel**: Extracting specific data fields (`status`, `latency`) from the `callback_payload` and displaying them dynamically using `dashboard.add_metrics_panel(..., grid_area="sidebar1")`.
- **Details Panel**: Showing rich text or custom HTML bound to specific SVG nodes using `dashboard.add_details_panel(..., grid_area="sidebar2")`.
- **Panel Position Default Context**: As `SivoDashboard` manages external layouts, the underlying `Sivo` map correctly operates with `panel_position="none"` internally (which is the default), preventing duplicated or interfering internal map overlays.

## Relevant Code Snippets

```python
# Configure the responsive grid. Notice the semi-colon and explicit column track definition!
dashboard.set_grid_layout(
    desktop='''
    "sidebar1 main main"
    "sidebar2 main main";
    grid-template-columns: 350px 1fr 1fr;
    ''',
    mobile='''
    "main"
    "sidebar1"
    "sidebar2";
    grid-template-columns: 1fr;
    '''
)

# Connect Sivo block and panels to their respective areas
dashboard.add_sivo_block("global_map", sivo_map, grid_area="main")
dashboard.add_metrics_panel("metrics", title="Node Metrics", metrics=["status", "latency"], grid_area="sidebar1")
dashboard.add_details_panel("details", title="Node Details", grid_area="sidebar2")
```

## Running the Example

Run the script from the root directory to generate the standalone dashboard:

```bash
PYTHONPATH=src python3 examples/dashboards/template_sidebar_left/main.py
```

Then open the generated `output.html` in your web browser. Try clicking the circles on the map to see the sidebar panels react smoothly without jumping!
