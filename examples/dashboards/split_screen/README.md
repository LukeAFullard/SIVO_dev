# Split Screen Dashboard Example

This example demonstrates how to build a responsive, split-screen layout suitable for comparing two primary components side-by-side using the `SivoDashboard` CSS Grid builder.

**What is being shown:**
- **Custom CSS Grid Layout:** We use `SivoDashboard.set_grid_layout` to define customized grid-template-areas for both desktop (side-by-side) and mobile (stacked) views. Sivo blocks and detail panels are mapped to these areas using the `grid_area` parameter.
- **Multiple Sivo Blocks:** The dashboard contains two distinct instances of `Sivo` loaded via `Sivo.from_template('dashboards/four_quadrants')`, allowing users to independently interact with left and right "maps".
- **Externalizing Detailed Views:** SIVO's internal map overlay panels are disabled by setting `default_panel_position="none"`. Instead, interactive mapping data (such as the `html` content mapped onto visual quadrants) is captured by the parent dashboard and rendered within external `dashboard.add_details_panel()` components assigned to the grid.

## Relevant Code Snippets

### 1. Setting Responsive Grid Layouts
Instead of utilizing a static template file, `SivoDashboard` layouts are built structurally mapping CSS grid areas:
```python
dashboard.set_grid_layout(
    desktop='''
"left right"
"left_details right_details"
    ''',
    mobile='''
"left"
"left_details"
"right"
"right_details"
    '''
)
```

### 2. Disabling Map Default Overlays
By explicitly setting `default_panel_position="none"`, the `html` detail payload will not be rendered inside the Echarts container on the canvas.
```python
left_map = Sivo.from_template(
    'dashboards/four_quadrants',
    layout_size="90%",
    lock_zoom_out=True,
    default_panel_position="none"
)

left_map.map(
    "quadrant_1",
    color="#3b82f6",
    html="<h3>Region A1</h3><p>Status: Active</p>"
)
```

### 3. Adding and Targeting the Block
The Sivo instance is added to the dashboard, targeted to its designated string area:
```python
dashboard.add_sivo_block("left_view", left_map, grid_area="left")
```

### 4. Creating External Detail Panels
The dashboard automatically listens to any clicks executed on the "left_view" Sivo block and redirects the `html` payload to the detail panel via layout placement.
```python
dashboard.add_details_panel(
    "left_details",
    title="Left View Details",
    grid_area="left_details"
)
```

## Running the Example

Run the main file to generate the dashboard:

```bash
PYTHONPATH=src python3 examples/dashboards/split_screen/main.py
```

Then open `output.html` in your browser.
