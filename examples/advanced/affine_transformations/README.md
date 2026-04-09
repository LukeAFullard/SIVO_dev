# Affine Transformations

## Description
Native SVG rendering required to apply transforms to the DOM elements directly

## Relevant Code
```python
sivo_app = Sivo.from_string(svg_string, render_mode="svg")
sivo_app.map(
    element_id="rectRotate",
    tooltip="Rotated 45 degrees",
    transform="rotate(45 100 100)" # rotate(angle cx cy)
)
sivo_app.map(
    element_id="circleScale",
    tooltip="Scaled by 1.25",
    transform="scale(1.25) translate(-50 -20)" # Scale also affects translation implicitly in SVG, so we offset to keep centered roughly
)
sivo_app.map(
    element_id="polyTranslate",
    tooltip="Translated by (100, 50)",
    transform="translate(100 50)"
)
sivo_app.to_html(output_path)
```
