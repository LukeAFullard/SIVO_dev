# HTML Overlays Example

This example demonstrates how to add fixed floating HTML elements directly over specific coordinates on your SVG using `add_overlay()`.

## What is being shown?

While standard `map()` bindings attach interactive behaviors (like tooltips or clicks) directly to SVG paths, sometimes you want static, visible HTML elements permanently positioned *on top* of the map. This is particularly useful for things like custom data labels, mini weather widgets, or status indicators that shouldn't be constrained by SVG styling capabilities.

The `add_overlay()` method lets you render standard HTML `<div>`s layered above the ECharts canvas, anchored automatically to the center points of specified SVG elements. These overlays follow the canvas when panning and optionally scaling.

## Key Code Snippets

### Adding a Weather Widget Overlay
This snippet attaches a simple HTML weather widget slightly offset from the "sun" SVG element.

```python
sivo_app.add_overlay(
    element_id="sun",
    html="<div style='background: white; padding: 2px 4px; border-radius: 4px; font-weight: bold;'>☀️ 30°C</div>",
    offset_x=20,  # Offset 20px to the right of the sun's center
    offset_y=-30  # Offset 30px above the sun's center
)
```

### Adding a Location Tag Overlay
This attaches a small label over the "house" element.

```python
sivo_app.add_overlay(
    element_id="house",
    html="<div style='background: #fff; padding: 2px 4px; border: 1px solid #000; font-size: 10px;'>Home</div>",
    offset_x=0,
    offset_y=-20
)
```

## Running the example

Run this example from the root directory of the repository:

```bash
PYTHONPATH=src python examples/basic/html_overlays/main.py
```

Then, open `examples/basic/html_overlays/output.html` in your web browser. You will see the SVG scene with HTML elements floating permanently above the sun and the house, which pan along with the map.