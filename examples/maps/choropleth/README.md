# Choropleth Map Example

This example demonstrates how to create an interactive choropleth map by applying a color gradient to SVG elements based on mapped numeric values.

## What is being tested/shown

- `Sivo.from_svg(...)`: Loading a base SVG graphic map (`sample.svg`).
- Setting `default_panel_position="right"` so that any interactive elements (like the HTML side panels) will display on the right side of the visualization.
- `apply_choropleth(...)`: Automatically generating a heat map by interpolating colors for SVG elements from a minimum color to a maximum color based on values from a data mapping.
- Automatically generating and displaying a UI legend mapping colors to values using `show_legend=True`.
- `sivo_app.map(...)`: Binding interactive HTML panels (`html="..."`) and adding a glow hover effect (`glow=True`) to each feature mapped in the data.

## Code structure

1. **Load SVG**: We load `sample.svg` and specify the right-side panel layout.
2. **Data Definition**: A Python dictionary simulates numeric data for different regions/features of the map.
3. **Color Coding**: `sivo_app.apply_choropleth()` is called with `min_color` and `max_color` bounds, coloring the SVG paths and generating a gradient legend.
4. **Interaction**: We loop through the data and call `sivo_app.map()` on each feature ID to attach descriptive HTML panels that appear when the feature is clicked.

## How to run

Run the example using:
```bash
PYTHONPATH=src python3 examples/maps/choropleth/main.py
```
This will regenerate the `output.html` file, which you can then open in a browser to see the interactive choropleth map.
