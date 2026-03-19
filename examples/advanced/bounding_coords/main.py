import os
from sivo import Sivo

def main():
    # 1. Initialize Sivo from an SVG file.
    # The SVG represents the bounding box of the USA (roughly [-125, 25] to [-65, 50]).
    # We pass these bounds in `bounding_coords` so ECharts maps the pixel space (0,0 to 800,500)
    # to this coordinate system, allowing us to drop markers using real (longitude, latitude) coordinates.
    sivo_app = Sivo.from_svg(
        os.path.join(os.path.dirname(__file__), "map.svg"),
        title="Geographic Coordinate Mapping",
        subtitle="Using `bounding_coords` to place elements via real (lat, lng)",
        bounding_coords=[
            [-125.0, 25.0],  # [minLng, minLat] (Bottom Left of the SVG map)
            [-65.0, 50.0]    # [maxLng, maxLat] (Top Right of the SVG map)
        ]
    )

    # 2. Apply proportional symbols using real Geographic Coordinates [longitude, latitude]
    # Because bounding_coords is set, ECharts maps these automatically to the SVG.
    data = {
        "San Francisco": {"value": 1500, "coord": [-122.4194, 37.7749], "color": "#f87171"},
        "New York": {"value": 2500, "coord": [-74.0060, 40.7128], "color": "#60a5fa"},
        "Chicago": {"value": 1200, "coord": [-87.6298, 41.8781], "color": "#34d399"},
        "Austin": {"value": 900, "coord": [-97.7431, 30.2672], "color": "#fbbf24"}
    }

    # Proportional symbols calculates a scatter plot internally on the map geometry
    sivo_app.apply_proportional_symbols(
        data,
        min_size=10,
        max_size=40,
        is_pulse=True
    )

    # Add tooltips for the dynamically added points
    for city, props in data.items():
        # ECharts will name the scatter points by their key
        sivo_app.map(
            element_id=city,
            tooltip=city,
            html=f"<h3>{city}</h3><p>Population Index: {props['value']}</p><p>Coordinates: {props['coord'][1]}, {props['coord'][0]}</p>"
        )

    # 3. Export to an interactive HTML bundle
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Generated bounding coords example at {output_path}")

if __name__ == "__main__":
    main()
