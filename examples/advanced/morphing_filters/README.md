# Morphing and Filters Example

This example demonstrates how to apply advanced native SVG visual effects, specifically path morphing and applying custom SVG filters (like drop shadows) using SIVO. By enabling `render_mode="svg"`, SIVO preserves and interacts with the native SVG DOM elements.

## Features Demonstrated

1. **Path Morphing (`morph_to_path`)**: An animated morphing transition between distinct SVG path shapes. It morphs a square into a triangle in an infinite yoyo animation using `morph_iterations=float('inf')`.
2. **SVG Filters (`filter`)**: Applying an embedded `<filter>` (in this case, a `<feDropShadow>`) from the `<defs>` tag of the SVG natively onto a specific element.
3. **Overlay Panel**: Ensures the interactive elements trigger correctly by setting `default_panel_position="overlay"`.

## Code Highlights

### Initializing SIVO for Native SVG Modifications
To manipulate path data natively or use SVG filters, SIVO must be instantiated with `render_mode="svg"`. The default panel position is configured to display mapped tooltips properly.

```python
# Enable render_mode='svg' to use native SVG properties
sivo_app = Sivo.from_string(svg_string, render_mode="svg", default_panel_position="overlay")
```

### Morphing an Element
You can morph one path into another by passing the target path `d` string to `morph_to_path` in `sivo_app.map()`. The morph duration, delay, and iterations can also be controlled.

```python
sivo_app.map(
    element_id="myMorphPath",
    tooltip="This path will morph to a triangle",
    morph_to_path="M100,20 L180,180 L100,180 L20,180 Z",
    morph_duration_ms=2000,
    morph_delay_ms=500,
    morph_easing="ease-in-out",
    morph_iterations=float('inf') # Infinite yoyo animation!
)
```

### Applying an SVG Filter
SVG filters defined in `<defs>` can be applied to mapped elements via the `filter` argument.

```python
sivo_app.map(
    element_id="myFilterCircle",
    tooltip="This circle has a blur filter applied",
    filter="url(#dropShadow)"
)
```

## Running the Example

Execute the python script to generate `morphing_filters.html`:

```bash
PYTHONPATH=src python3 examples/advanced/morphing_filters/main.py
```

Then, open `morphing_filters.html` in your web browser to see the morphing animation and the applied shadow filter.