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
        'id': ['Hub1', 'Hub2', 'Hub3', 'Hub4'],
        'name': ['Seattle', 'Denver', 'Chicago', 'New York']
    }
    gdf = gpd.GeoDataFrame(data, geometry=polys)

    app = Sivo.from_geodataframe(
        gdf=gdf,
        id_col='id',
        name_col='name',
        title="Flow Map Demo",
        subtitle="Domestic Flight Volume Simulation",
        theme="dark",
        disable_panel=True
    )

    app.apply_choropleth({k: 1 for k in data['id']}, min_color="#1e293b", max_color="#1e293b", show_legend=False)

    print("Applying Flow Map...")

    # Calculate explicit centroids since GeoDataFrame groups bypass SVG bounding box calculations
    centroids = {row['id']: [row.geometry.centroid.x, row.geometry.centroid.y] for idx, row in gdf.iterrows()}

    flow_data = [
        {"origin": "Hub1", "destination": "Hub4", "value": 3200, "label": "SEA-JFK", "color": "#38bdf8", "source_coord": centroids["Hub1"], "target_coord": centroids["Hub4"]},
        {"origin": "Hub1", "destination": "Hub2", "value": 1500, "color": "#38bdf8", "source_coord": centroids["Hub1"], "target_coord": centroids["Hub2"]},
        {"origin": "Hub4", "destination": "Hub3", "value": 2800, "label": "JFK-ORD", "color": "#fbbf24", "source_coord": centroids["Hub4"], "target_coord": centroids["Hub3"]},
        {"origin": "Hub3", "destination": "Hub2", "value": 900, "color": "#fbbf24", "source_coord": centroids["Hub3"], "target_coord": centroids["Hub2"]},
        {"origin": "Hub2", "destination": "Hub1", "value": 1200, "color": "#a3e635", "source_coord": centroids["Hub2"], "target_coord": centroids["Hub1"]}
    ]

    app.apply_flow_map(flow_data, min_width=1.0, max_width=6.0, flow_effect=True, effect_symbol="arrow", animation_speed=2.0)

    print("Adding nodes (circles) for origins/destinations...")
    nodes_data = {
        "Hub1": {"value": 1, "coord": centroids["Hub1"], "color": "#38bdf8"},
        "Hub2": {"value": 1, "coord": centroids["Hub2"], "color": "#a3e635"},
        "Hub3": {"value": 1, "coord": centroids["Hub3"], "color": "#fbbf24"},
        "Hub4": {"value": 1, "coord": centroids["Hub4"], "color": "#fbbf24"}
    }
    app.apply_proportional_symbols(nodes_data, min_size=12.0, max_size=12.0, is_pulse=True)

    html_output = "examples/68_flow_map/flow_map.html"
    app.to_html(html_output)
    print(f"Successfully generated {html_output}")

if __name__ == "__main__":
    create_example()
