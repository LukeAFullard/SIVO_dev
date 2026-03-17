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
        Polygon([(10, 10), (10, 20), (20, 20), (20, 10)]),
        Polygon([(20, 0), (20, 10), (30, 10), (30, 0)]),
        Polygon([(20, 10), (20, 20), (30, 20), (30, 10)])
    ]
    data = {
        'id': ['Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6'],
        'name': ['Forest', 'Lake', 'City', 'Suburbs', 'Plains', 'Forest'],
        'land_cover': ['Forest', 'Water', 'Urban', 'Urban', 'Agriculture', 'Forest']
    }
    gdf = gpd.GeoDataFrame(data, geometry=polys)

    app = Sivo.from_geodataframe(
        gdf=gdf,
        id_col='id',
        name_col='name',
        title="Categorical Map Demo",
        subtitle="Land Cover Classification",
        theme="light",
        disable_panel=True
    )

    print("Applying Categorical Map...")
    category_map = {row['id']: row['land_cover'] for idx, row in gdf.iterrows()}

    # Custom color palette mapping categories to hex colors
    palette = {
        'Forest': '#22c55e',
        'Water': '#3b82f6',
        'Urban': '#cbd5e1',
        'Agriculture': '#fef08a'
    }

    app.apply_categorical_map(
        data_map=category_map,
        color_palette=palette,
        show_legend=True
    )

    html_output = "examples/70_categorical_map.html"
    app.to_html(html_output)
    print(f"Successfully generated {html_output}")

if __name__ == "__main__":
    create_example()
