# Basic: Animations and Markers

This example shows how to configure element animations and place custom dynamic markers exactly centered on specific SVG elements using Sivo.

## What is being tested/demonstrated
* Adding predefined CSS animations ("pulse", "fade") directly to specific interactive components via `sivo_app.map()`.
* Generating floating icons and text labels dynamically attached to target elements using `sivo_app.add_marker()`.
* Using marker positional offsets relative to the element center.

## Key Code

```python
# 1. Map typical interactions
sivo_app.map(
    element_id="sun",
    tooltip="A pulsing sun",
    animation="pulse",
    color="orange"
)

sivo_app.map(
    element_id="house",
    tooltip="Fading house",
    animation="fade",
    color="purple"
)

# 2. Add dynamic markers exactly centered on SVG elements
sivo_app.add_marker(
    element_id="mountain1",
    icon="⛰️",
    label="Peak 1",
    offset_y=-30
)
```
