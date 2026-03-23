# Basic: HTML Overlays

This example illustrates how to place static, dynamic HTML content directly on top of specific SVG elements in the interactive app.

## What is being tested/demonstrated
* Statically adding persistent HTML overlay panels to SVG components using `sivo_app.add_overlay()`.
* Positioning HTML elements relative to SVG ID coordinates (offsetting X and Y).

## Key Code

```python
# Add HTML overlays over the map coordinates dynamically
sivo_app.add_overlay(
    element_id="sun",
    html="<div style='background: white; padding: 2px 4px; border-radius: 4px; font-weight: bold;'>☀️ 30°C</div>",
    offset_x=20, # offset from the center
    offset_y=-30
)

sivo_app.add_overlay(
    element_id="house",
    html="<div style='background: #fff; padding: 2px 4px; border: 1px solid #000; font-size: 10px;'>Home</div>",
    offset_x=0,
    offset_y=-20
)
```
