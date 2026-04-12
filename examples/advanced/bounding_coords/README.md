# Bounding Coordinates Example

This example demonstrates how to correctly map real-world geographic coordinates onto a native SVG using the `bounding_coords` parameter in SIVO.

## What This Tests
1. **Accurate Geographic Vector SVG**: Instead of a dummy background, this example uses mathematically accurate `<path>` polygons derived from US Census Shapefiles, which have been scaled to match an SVG `viewBox`.
2. **Proper Bounding Coords**: The `bounding_coords` align perfectly to the geographic `[minLng, minLat]` and `[maxLng, maxLat]` bounding box, ensuring ECharts dynamically plots symbols at the correct mathematical positions.
3. **SVG Y-Axis Inversion**: Standard geographic map coordinates map latitude upward, whereas SVG pixels increase downward. This script dynamically inverts the latitude of each data point prior to plotting so it accurately aligns with the top-to-bottom SVG drawing without mutating the global ECharts mapping matrix.

## Implementation Details

### Bounding Coords Parameter
When calling `Sivo.from_svg()`, `bounding_coords` must strictly be the bounds of the geographic map (not arbitrary values).

```python
sivo_app = Sivo.from_svg(
    "map.svg",
    bounding_coords=[
        [-124.7258, 24.4981],  # Bottom Left [minLng, minLat]
        [-66.9499, 49.3844]    # Top Right [maxLng, maxLat]
    ]
)
```

### Inverting Y-Axis Points
Because ECharts applies a strict linear map for projections when `bounding_coords` is specified, it assumes a Cartesian plane where Y goes UP. But the SVG `<path>` elements have Y pointing DOWN.

```python
# Formula: (maxLat + minLat) - actual_lat
inverted_lat = (49.3844 + 24.4981) - props["coord"][1]
mapped_data[city] = {
    "value": props["value"],
    "coord": [props["coord"][0], inverted_lat]
}
```

### Proper Map Geometry Names
In `map.svg`, background elements (`<rect>`) must **not** have a `name` attribute so ECharts ignores them when looking for region geometry to cast scatter plots onto. The actual map paths must have a `name` (e.g., `<path name="usa_mainland" ...>`).
