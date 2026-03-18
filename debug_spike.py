import geopandas as gpd
from shapely.geometry import Polygon
from sivo import Sivo

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

app = Sivo.from_geodataframe(gdf=gdf, id_col='id', name_col='name')
spike_data = {
    row['id']: {
        "value": row['cases'],
        "coord": [row.geometry.centroid.x, row.geometry.centroid.y]
    }
    for idx, row in gdf.iterrows()
}
app.apply_spike_map(spike_data, max_height=100.0, base_width=20.0, color="rgba(220, 38, 38, 0.8)")
app.to_html("debug_spike.html")
print("Done")
