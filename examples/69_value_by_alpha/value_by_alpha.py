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
        'id': ['A', 'B', 'C', 'D'],
        'name': ['County A', 'County B', 'County C', 'County D'],
        'income_rate': [45000, 120000, 60000, 35000],
        'population_density': [500, 10000, 2000, 100]
    }
    gdf = gpd.GeoDataFrame(data, geometry=polys)

    app = Sivo.from_geodataframe(
        gdf=gdf,
        id_col='id',
        name_col='name',
        title="Value-by-Alpha Map Demo",
        subtitle="Income Level vs Population Density",
        theme="light",
        disable_panel=True
    )

    print("Applying Value-by-Alpha Map...")
    # Base color is Income, Alpha is Population Density
    income_map = {row['id']: row['income_rate'] for idx, row in gdf.iterrows()}
    density_map = {row['id']: row['population_density'] for idx, row in gdf.iterrows()}

    app.apply_value_by_alpha(
        base_data_map=income_map,
        alpha_data_map=density_map,
        min_color="#fee2e2",
        max_color="#7f1d1d",
        min_alpha=0.2,
        max_alpha=1.0,
        show_legend=True
    )

    html_output = "examples/69_value_by_alpha/value_by_alpha.html"
    app.to_html(html_output)
    print(f"Successfully generated {html_output}")

if __name__ == "__main__":
    create_example()
