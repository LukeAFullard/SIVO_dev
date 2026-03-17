import geopandas as gpd
from shapely.geometry import Polygon
from sivo import Sivo
import os

def create_example():
    print("Creating mock geospatial data...")

    polys = [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0)]),
        Polygon([(10, 0), (10, 10), (20, 10), (20, 0)]),
        Polygon([(0, 10), (0, 20), (10, 20), (10, 10)]),
        Polygon([(10, 10), (10, 20), (20, 20), (20, 10)])
    ]
    data = {
        'id': ['A', 'B', 'C', 'D'],
        'name': ['Region A', 'Region B', 'Region C', 'Region D'],
        'population': [5000, 25000, 12000, 48000],
        'income': [35000, 85000, 60000, 120000],
        'category': ['Urban', 'Rural', 'Urban', 'Suburban']
    }
    gdf = gpd.GeoDataFrame(data, geometry=polys)

    print("Initializing Sivo from GeoDataFrame...")
    app = Sivo.from_geodataframe(
        gdf=gdf,
        id_col='id',
        name_col='name',
        title="Advanced Mapping Techniques Demo",
        subtitle="Spike Maps, Flow Maps, Bivariate & Categorical",
        theme="light",
        disable_panel=True
    )

    print("1. Applying Spike Map...")
    spike_data = {
        'A': 5000,
        'B': 25000,
        'C': 12000,
        'D': 48000
    }
    app.apply_spike_map(spike_data, max_height=8.0, base_width=2.0, color="rgba(255, 0, 0, 0.7)")

    print("2. Applying Flow Map...")
    flow_data = [
        {"origin": "A", "destination": "D", "value": 1500, "label": "Migration"},
        {"origin": "C", "destination": "B", "value": 800, "color": "#0000ff"}
    ]
    app.apply_flow_map(flow_data, min_width=1.0, max_width=5.0, color="#ffaa00", flow_effect=True)

    print("3. Applying Value-by-Alpha Map...")
    income_map = {row['id']: row['income'] for idx, row in gdf.iterrows()}
    pop_map = {row['id']: row['population'] for idx, row in gdf.iterrows()}
    app.apply_value_by_alpha(income_map, pop_map, min_color="#ffffff", max_color="#0066cc", min_alpha=0.2, max_alpha=1.0)

    print("Exporting HTML...")
    html_output = "advanced_mapping_demo.html"
    app.to_html(html_output)
    print(f"Successfully generated {html_output}")

if __name__ == "__main__":
    create_example()
