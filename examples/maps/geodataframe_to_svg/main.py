import geopandas as gpd
from shapely.geometry import Polygon
import os
from sivo.core.sivo import Sivo

def create_example():
    print("Generating GeoDataFrame...")

    # Create some polygons (e.g. regions on a simple map)
    p1 = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
    p2 = Polygon([(2, 0), (4, 0), (4, 2), (2, 2)])

    # Intentionally add detailed vertices to p3 so we can simplify it
    p3 = Polygon([(0, 2), (0.1, 2.1), (0.2, 2.05), (0.5, 2.5), (1.0, 2.8), (1.5, 2.5), (1.8, 2.1), (2, 2), (0, 2)])

    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame({
        'id': ['region_1', 'region_2', 'region_3'],
        'name': ['West Sector', 'East Sector', 'North Sector'],
        'value': [100, 200, 300],
        'geometry': [p1, p2, p3]
    })

    # Use Sivo to generate the SVG. We pass simplify_tolerance=0.2 to smooth out the detailed geometry of p3.
    print("Converting GeoDataFrame to SVG with simplification...")
    app = Sivo.from_geodataframe(
        gdf,
        id_col='id',
        name_col='name',
        simplify_tolerance=0.2
    )

    # Let's map some data for good measure
    app.apply_choropleth(
        data_map={'region_1': 100, 'region_2': 200, 'region_3': 300},
        min_color="#e0f3f8",
        max_color="#014636"
    )

    # Export to SVG
    output_path = os.path.join(os.path.dirname(__file__), "output.svg")
    app.to_svg(output_path=output_path)
    print(f"SVG saved to: {output_path}")

    # Also export the standard HTML for comparison
    html_path = os.path.join(os.path.dirname(__file__), "output.html")
    app.to_html(output_path=html_path)
    print(f"HTML saved to: {html_path}")

if __name__ == "__main__":
    create_example()