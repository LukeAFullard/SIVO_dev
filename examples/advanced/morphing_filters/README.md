# Morphing Filters

## Description
Enable render_mode='svg' to use native SVG properties Map path morphing (native SMIL animate requires the exact same number and type of path commands) Source path has 5 commands: M, L, L, L, Z Target path must have 5 commands too, so we duplicate a point to make a triangle: M, L, L, L, Z Map an SVG filter

## Relevant Code
```python
sivo_app = Sivo.from_string(svg_string, render_mode="svg")
sivo_app.map(
    element_id="myMorphPath",
    tooltip="This path will morph to a triangle",
    morph_to_path="M100,20 L180,180 L100,180 L20,180 Z",
    morph_duration_ms=2000,
    morph_delay_ms=500,
    morph_easing="ease-in-out",
    morph_iterations=float('inf') # Infinite yoyo animation!
)
sivo_app.map(
    element_id="myFilterCircle",
    tooltip="This circle has a blur filter applied",
    filter="url(#dropShadow)"
)
sivo_app.to_html(output_path)
```
