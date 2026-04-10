# Animations & Markers

This example demonstrates how to apply animations to SVG elements and how to add markers to specific elements.

The `main.py` script maps typical interactions to SVG elements:
- A pulsing animation to the element with ID `sun`
- A fading animation to the element with ID `house`

It also adds dynamic markers exactly centered on SVG elements:
- A marker with a mountain icon and "Peak 1" label above the element with ID `mountain1`
- A marker with a mountain icon and "Peak 2" label above the element with ID `mountain2`

Relevant code:
```python
    sivo_app.map(
        element_id="sun",
        tooltip="A pulsing sun",
        animation="pulse",
        color="orange"
    )

    sivo_app.add_marker(
        element_id="mountain1",
        icon="⛰️",
        label="Peak 1",
        offset_y=-30
    )
```
