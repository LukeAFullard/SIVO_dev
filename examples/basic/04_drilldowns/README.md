# 04 Drilldowns

This example illustrates the "drill-down" feature. By clicking on a mapped SVG element, SIVO will transition and load another SVG file, simulating navigating into a deeper level of detail (like entering a house).

### Key Code

```python
# Drill down logic - click on the house to load another SVG.
sivo_app.map(
    element_id="house",
    tooltip="Click to enter the house",
    drill_to="floor1.svg",
    hover_color="orange",
    glow=True
)
```
