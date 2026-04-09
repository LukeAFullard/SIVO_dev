# Bounding Coordinates Example

This example demonstrates how to map the arbitrary pixel space of an SVG file directly to real-world geographic coordinates (longitude and latitude). This allows SIVO and ECharts to accurately place elements, such as proportional symbols or markers, on the SVG using actual geographic coordinate data.

## What is being shown
- An SVG file (`map.svg`) that represents a rough map of the United States.
- We configure the SIVO application with `bounding_coords` to anchor the SVG's bottom-left and top-right pixel corners to specific geographic longitudes and latitudes.
- We then use the `apply_proportional_symbols` method, passing in a dictionary containing cities and their actual longitude and latitude pairs `[lng, lat]`.
- Because the bounding coordinates have been set, the markers are correctly projected onto the SVG drawing automatically.
- We set `default_panel_position="right"` in `Sivo.from_svg(...)` and bind HTML content via `sivo_app.map(...)` so that clicking on any generated point will open an information panel on the right.

## Key Code Snippets

### 1. Defining Geographic Bounding Coordinates
When loading the SVG map, pass the bounding box of the area it covers in `[longitude, latitude]` format (Bottom-Left, then Top-Right).

```python
sivo_app = Sivo.from_svg(
    "map.svg",
    default_panel_position="right", # Panels now default to 'none', so we enable it
    bounding_coords=[
        [-125.0, 25.0],  # [minLng, minLat] (Bottom Left corner)
        [-65.0, 50.0]    # [maxLng, maxLat] (Top Right corner)
    ]
)
```

### 2. Supplying Real Coordinates for Data
With bounding coordinates established, data elements can simply use their real-world `coord` (in `[lng, lat]` format) instead of needing to reference specific SVG element IDs to determine their placement.

```python
data = {
    "San Francisco": {"value": 1500, "coord": [-122.4194, 37.7749], "color": "#f87171"},
    "New York": {"value": 2500, "coord": [-74.0060, 40.7128], "color": "#60a5fa"},
    # ...
}

sivo_app.apply_proportional_symbols(
    data,
    min_size=10,
    max_size=40,
    is_pulse=True
)
```

## Running the Example
To run this example locally and generate the interactive `output.html` file, run:

```bash
PYTHONPATH=src python examples/advanced/bounding_coords/main.py
```