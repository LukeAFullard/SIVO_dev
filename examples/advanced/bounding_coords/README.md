# Geographic Coordinate Mapping (Bounding Coords)

This example demonstrates how to use the `bounding_coords` parameter to map standard SVG pixel space to real-world geographical coordinates (longitude and latitude). This allows you to position dynamic elements like scatter plots or proportional symbols using actual geo-coordinates rather than arbitrary pixel locations.

## What is being tested/shown:

- **Mapping Pixel Space to Geo-coordinates:** By providing `bounding_coords` (representing the `[minLng, minLat]` and `[maxLng, maxLat]` of the underlying SVG map), ECharts automatically handles the projection of real-world coordinates onto the SVG canvas.
- **Proportional Symbols with Real Coordinates:** Using `apply_proportional_symbols()`, the example passes data points that explicitly define a `"coord"` property alongside their `"value"`. SIVO correctly places these markers on the map using the defined bounding coordinates.
- **Dynamic Element Mapping:** The example loops through the added data points and uses the `.map()` method to bind interactive tooltips and rich HTML content (via `html`) directly to the dynamically created scatter points.

## Relevant Code Snippets:

Defining the bounding coordinates during initialization:

```python
sivo_app = Sivo.from_svg(
    "map.svg",
    bounding_coords=[
        [-125.0, 25.0],  # [minLng, minLat]
        [-65.0, 50.0]    # [maxLng, maxLat]
    ]
)
```

Applying proportional symbols using coordinates:

```python
data = {
    "San Francisco": {"value": 1500, "coord": [-122.4194, 37.7749], "color": "#f87171"},
    # ...
}

sivo_app.apply_proportional_symbols(
    data,
    min_size=10,
    max_size=40,
    is_pulse=True
)
```

Binding interactions to the dynamically created markers:

```python
sivo_app.map(
    element_id="San Francisco",
    tooltip="San Francisco",
    html="<h3>San Francisco</h3><p>Population Index: 1500</p>"
)
```
