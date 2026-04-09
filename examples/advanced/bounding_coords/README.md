# Bounding Coords

## Description
1. Initialize Sivo from an SVG file. The SVG represents the bounding box of the USA (roughly [-125, 25] to [-65, 50]). We pass these bounds in `bounding_coords` so ECharts maps the pixel space (0,0 to 800,500) to this coordinate system, allowing us to drop markers using real (longitude, latitude) coordinates. 2. Apply proportional symbols using real Geographic Coordinates [longitude, latitude] Because bounding_coords is set, ECharts maps these automatically to the SVG. Proportional symbols calculates a scatter plot internally on the map geometry Add tooltips for the dynamically added points ECharts will name the scatter points by their key 3. Export to an interactive HTML bundle

## Relevant Code
```python
    sivo_app = Sivo.from_svg(
        os.path.join(os.path.dirname(__file__), "map.svg"),
        title="Geographic Coordinate Mapping",
        subtitle="Using `bounding_coords` to place elements via real (lat, lng)",
        bounding_coords=[
            [-125.0, 25.0],  # [minLng, minLat] (Bottom Left of the SVG map)
            [-65.0, 50.0]    # [maxLng, maxLat] (Top Right of the SVG map)
        ]
    )
    sivo_app.apply_proportional_symbols(
        data,
        min_size=10,
        max_size=40,
        is_pulse=True
    )
    sivo_app.to_html(output_path)
        sivo_app.map(
            element_id=city,
            tooltip=city,
            html=f"<h3>{city}</h3><p>Population Index: {props['value']}</p><p>Coordinates: {props['coord'][1]}, {props['coord'][0]}</p>"
        )
```
