# Hero and Four Dashboard Layout Example

This example demonstrates how to build a 2-column dashboard layout using SIVO's CSS Grid `set_grid_layout` functionality. The dashboard features a single large "hero" component on the left and a 2x2 grid of smaller components on the right.

## What is being shown
- **CSS Grid Integration:** Instead of using an external HTML template file, the layout is defined dynamically using `dashboard.set_grid_layout(desktop=..., mobile=...)`, giving precise control over placement of components using the `grid_area` parameter.
- **SIVO Map Interaction:** Three separate `Sivo` blocks map interactive elements (Quadrants 1, 2, and 3).
- **Rich Media Details:** The blocks implement the `html` parameter for rich media info overlays rather than the deprecated `tooltip` argument. When you click on the mapped regions, their `html` content is sent to the `add_details_panel`.
- **Metrics Extraction:** The `callback_payload` parameter is used in the mapped elements, passing structured data (`{"revenue": "$1.2M", "growth": "+15%"}`) that is extracted and rendered automatically by the `add_metrics_panel`.
- **Responsive Layout:** The grid adapts fluidly, with the mobile layout stacking the hero component on top of the 2x2 grid.

## Related Code

### Defining the CSS Grid Layout
```python
dashboard.set_grid_layout(
    desktop='''
    "hero hero"
    "box1 box2"
    "box3 box4"
    ''',
    mobile='''
    "hero"
    "box1"
    "box2"
    "box3"
    "box4"
    '''
)
```

### Adding Interactive SIVO Blocks
When creating a mapping inside a block, we use `html` and `callback_payload`:
```python
main_map.map(
    "quadrant_1",
    color="#3b82f6",
    hover_color="#2563eb",
    html="<h3>Primary Region</h3><p>Focus Area</p>",
    callback_payload={"revenue": "$1.2M", "growth": "+15%"}
)
# Assign the block to the specific grid area "hero"
dashboard.add_sivo_block("primary_focus", main_map, grid_area="hero")
```

### Adding Support Panels for SIVO Blocks
Metrics panels capture the `callback_payload` data automatically when the user clicks on regions in the SIVO blocks:
```python
dashboard.add_metrics_panel(
    "q1_metrics",
    title="Revenue",
    metrics=["revenue", "growth"],
    grid_area="box1"
)
```

Details panels render the `html` content from the mappings:
```python
dashboard.add_details_panel(
    "q4_details",
    title="Quick Analysis",
    placeholder="Select a region to view analysis.",
    grid_area="box4"
)
```

## Running the Example
From the root directory, you can run:
```bash
PYTHONPATH=src python3 examples/dashboards/template_hero_and_four/main.py
```
This will output an `output.html` file that you can view in your browser.
