# Hero and Four Layout Example

This example demonstrates how to create a "Hero and Four" dashboard layout using the modern CSS Grid layout system in `SivoDashboard`.

The setup creates a two-column layout on desktop:
- The left section contains a single large "hero" component.
- The right section contains a 2x2 grid of four smaller components (which together can form a square).

On mobile, the layout gracefully degrades into a vertical stack.

## Key Features Demonstrated

- **CSS Grid Layout:** Utilizing `dashboard.set_grid_layout()` to explicitly define the `desktop` and `mobile` grid areas.
- **Sivo Block Placement:** Mapping both large Sivo visualization blocks and smaller dashboard utility panels (like metrics and details panels) to precise grid areas using the `grid_area` parameter.
- **Interactive Maps:** Using `Sivo.from_template` to embed four quadrants maps, disabling default overlay panels by ensuring they are not enabled by default, and assigning custom interactivity directly to SVG regions.

## Code Highlights

### 1. Defining the Grid Layout

The `SivoDashboard` uses a text-based representation of grid areas. To create a hero on the left and four boxes on the right, we use a 5-column (or suitable) layout:

```python
dashboard.set_grid_layout(
    desktop='''
        "hero hero box1 box2"
        "hero hero box3 box4"
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

### 2. Placing Blocks in the Grid

Each element added to the dashboard, whether a standard Sivo map, a metrics panel, or a details panel, is assigned to its respective grid area using the `grid_area` argument:

```python
# The Hero component
main_map = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)
main_map.map("quadrant_1", color="#3b82f6", hover_color="#2563eb", tooltip="<h3>Primary Region</h3><p>Focus Area</p>")

# Add the map to the dashboard and assign it to the 'hero' grid area
dashboard.add_sivo_block("primary_focus", main_map, grid_area="hero")

# Add a metrics panel to the 'box1' grid area
dashboard.add_metrics_panel(
    "q1_metrics",
    title="Revenue",
    metrics=["revenue", "growth"],
    grid_area="box1"
)
```

## Running the Example

To generate the dashboard, run the `main.py` script from the project root:

```bash
PYTHONPATH=src python3 examples/dashboards/template_hero_and_four/main.py
```

This will output an `output.html` file in the example directory, which can be opened in any web browser to interact with the responsive dashboard.
