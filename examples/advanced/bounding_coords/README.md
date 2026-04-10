# Bounding Coords Example

This example demonstrates how to use the `bounding_coords` parameter in `Sivo.from_svg` to map real-world geographical coordinates (longitude and latitude) directly onto an SVG map. It correctly scales a set of proportional symbol markers based on provided data points.

## What is tested/shown
- **Dynamic ECharts `geo` Object Construction:** Verifies that SIVO properly constructs a background ECharts `geo` object by providing `boundingCoords` to it when dynamic map layers (e.g., proportional symbols/scatter plots) are applied. This ensures markers are placed in the correct locations on the map geometry, rather than huddling in the top-left corner (pixel space).
- **Y-Axis Inversion:** Demonstrates the formula to invert geographical latitude (which counts upwards from the equator) into SVG pixel coordinates (which count downwards from the top-left corner).
- **Default Panel Position:** Showcases using `default_panel_position="right"` to correctly display dynamically mapped HTML content in a side panel.

## The Y-Axis Inversion Logic
Since standard map coordinates have a Y-axis pointing up (latitude) while SVG pixels point down, mapping raw geographic coordinates onto an SVG directly would cause them to render upside-down. To combat this, the script applies an inversion algorithm to the mapped points before they are rendered:

```python
mapped_data = {}
for city, props in data.items():
    # Correct the SVG Y-Axis Inversion
    # Formula: (maxLat + minLat) - actual_lat
    inverted_lat = (50.0 + 25.0) - props["coord"][1]
    mapped_data[city] = {
        "value": props["value"],
        "coord": [props["coord"][0], inverted_lat],
        "color": props["color"]
    }

sivo_app.apply_proportional_symbols(
    mapped_data,
    min_size=10,
    max_size=40,
    is_pulse=True
)
```

The original, un-inverted coordinates are maintained for the tooltip displays:

```python
sivo_app.map(
    element_id=city,
    tooltip=city,
    html=f"<h3>{city}</h3><p>Population Index: {props['value']}</p><p>Coordinates: {props['coord'][1]}, {props['coord'][0]}</p>"
)
```

## Running the Example
To test this functionality, build the application bundle by running:

```bash
PYTHONPATH=src python3 examples/advanced/bounding_coords/main.py
```

This compiles the interactive map to `output.html`. Open the generated `output.html` in a browser to see the proportional symbols scattered accurately over the USA map, with correct hover tooltips and a right-aligned info panel appearing on click.
