# Hexbin Map

This example demonstrates how to use SIVO to generate an interactive hexagonal binning map by aggregating raw `[x, y]` coordinates.

## What is being tested/shown
- The automatic calculation of a hex grid and aggregation of dense point data into bins.
- The use of the `apply_hexbin` method to visualize cluster densities natively on an SVG background.
- Adjusting visualization settings such as hex size, color palette (from low to high density), opacity, and stroke styling.
- Setting `default_panel_position="none"` since no interactive HTML mapped items are present on a simple overlay map.

## Steps involved
1. **Initialize Map**: A simple SVG with a background rectangle is loaded using `Sivo.from_string(...)`, explicitly setting `default_panel_position="none"`.
2. **Simulate Data**: A list of random normal and uniform points is generated to simulate traffic incidents or check-ins.
3. **Apply Hexbin**: `sivo_app.apply_hexbin(...)` takes the points and aggregates them into visually styled hexagons.
4. **Export**: The resulting map is rendered to `interactive_hexbin.html`.

## Relevant code snippet
```python
# Create Sivo App
sivo_app = Sivo.from_string(svg_data, title="City Traffic Incidents", subtitle="Hexagonal Binning Map", default_panel_position="none")

# ... simulate points data ...

# Apply hexbin map overlay
sivo_app.apply_hexbin(
    points=points,
    hex_size=4.0, # The radius of each hexagon
    color_palette=["#fee0d2", "#de2d26", "#a50f15"], # Color gradient (low -> high)
    min_opacity=0.6,
    max_opacity=0.9,
    stroke_color="#ffffff",
    stroke_width=0.5
)
```
