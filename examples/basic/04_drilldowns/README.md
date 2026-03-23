# Basic: Drilldowns

This example showcases how to set up navigational drill-downs between SVG files in Sivo. Clicking on an element loads a completely new SVG canvas.

## What is being tested/demonstrated
* Connecting an SVG element to trigger a view transition by loading a new underlying SVG file (`drill_to`).
* Demonstrating user feedback (tooltip, hover color, glow) to indicate the interactive nature of a drilldown.

## Key Code

```python
# Drill down logic - click on the house to load another SVG.
# We will use floor1.svg to simulate going inside the house.
sivo_app.map(
    element_id="house",
    tooltip="Click to enter the house",
    drill_to="floor1.svg",
    hover_color="orange",
    glow=True
)
```
