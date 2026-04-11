# Draggable Elements in SIVO

This example demonstrates how to make native SVG elements within a SIVO map draggable. It showcases both standard mouse event support (for desktop browsers) and touch event support (`touchstart`, `touchmove`, `touchend`, `touchcancel`) for mobile and touch devices.

## What is being tested/shown

1.  **Draggable Mapping:** Passing `draggable=True` in `sivo_app.map()` to enable dragging of an individual SVG shape.
2.  **Touch Support:** Verifying that elements can be dragged smoothly on mobile devices without triggering standard touch scrolling behavior.
3.  **Tooltip Visibility:** Ensuring that the configured tooltips remain visible, unclipped, and render above everything else (via `appendToBody` and `z-index` modifications).

## Steps Involved

1.  **Define an SVG:** We define a basic SVG string containing a rectangle and a circle.
2.  **Initialize SIVO:** We initialize the map using `Sivo.from_string()` and specify `render_mode="svg"`, which is required for direct SVG element transformations like dragging.
3.  **Map Interactive Elements:** We use `sivo_app.map()` to bind `draggable=True` and a custom `tooltip` to both the rectangle (`#dragRect`) and the circle (`#dragCircle`).
4.  **Export:** The application is compiled to a standalone HTML file.

## Relevant Code Snippet

```python
from sivo import Sivo

svg_string = """
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <rect id="dragRect" x="50" y="50" width="100" height="100" fill="#3498db" />
    <circle id="dragCircle" cx="250" cy="100" r="50" fill="#e74c3c" />
</svg>
"""

# Must use render_mode="svg" for drag and affine transformations
sivo_app = Sivo.from_string(svg_string, render_mode="svg")

sivo_app.map(
    element_id="dragRect",
    tooltip="This rectangle is draggable",
    draggable=True
)

sivo_app.map(
    element_id="dragCircle",
    tooltip="This circle is draggable",
    draggable=True
)

# Export
sivo_app.to_html("draggable_elements.html")
```

## Running the Example

Make sure SIVO is installed or in your python path. Then run:
```bash
PYTHONPATH=src python3 examples/advanced/draggable_elements/main.py
```
Open `draggable_elements.html` in your browser. Try dragging the shapes using your mouse or simulating touch via developer tools. Check that tooltips appear properly over the shapes when hovered.
