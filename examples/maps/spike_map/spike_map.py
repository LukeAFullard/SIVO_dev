import geopandas as gpd
from shapely.geometry import Polygon
from sivo import Sivo

def create_example():
    print("Creating mock geospatial data...")
    # Creating a simple grid map
    polys = [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0)]),
        Polygon([(10, 0), (10, 10), (20, 10), (20, 0)]),
        Polygon([(0, 10), (0, 20), (10, 20), (10, 10)]),
        Polygon([(10, 10), (10, 20), (20, 20), (20, 10)])
    ]
    data = {
        'id': ['Zone1', 'Zone2', 'Zone3', 'Zone4'],
        'name': ['Northwest', 'Northeast', 'Southwest', 'Southeast'],
        'cases': [5000, 25000, 12000, 48000]
    }
    gdf = gpd.GeoDataFrame(data, geometry=polys)

    app = Sivo.from_geodataframe(
        gdf=gdf,
        id_col='id',
        name_col='name',
        title="Spike Map Demo",
        subtitle="COVID-19 Case Density Representation",
        theme="light",
        default_panel_position="none"
    )

    # Base styling
    app.apply_choropleth({k: 1 for k in data['id']}, min_color="#f0f0f0", max_color="#f0f0f0", show_legend=False)

    # Pass explicit centroid coordinates because GeoDataFrame wrapper groups (<g>)
    # don't inherently calculate bounding boxes in the basic SVGParser.
    spike_data = {
        row['id']: {
            "value": row['cases'],
            "coord": [row.geometry.centroid.x, row.geometry.centroid.y]
        }
        for idx, row in gdf.iterrows()
    }

    print("Applying Spike Map...")
    # Map proportional heights and constant width.
    # Because Echarts maps the logical bounding coordinates (0-20) to the physical screen width/height,
    # the max_height and base_width should be in logical units relative to the GeoDataFrame's total bounds.
    # Since the total width/height of the grid is 20 units, a max height of 10.0 and base width of 2.0
    # will appear proportional on the canvas without blowing up out of bounds.
    app.apply_spike_map(spike_data, max_height=8.0, base_width=2.0, color="rgba(220, 38, 38, 0.8)")

    html_output = "examples/maps/spike_map/spike_map.html"
    app.to_html(html_output)
    print(f"Successfully generated {html_output}")

if __name__ == "__main__":
    create_example()
