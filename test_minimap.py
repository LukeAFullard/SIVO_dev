from sivo.core.sivo import Sivo
import geopandas as gpd

url = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
world = gpd.read_file(url)
europe = world[world.CONTINENT == 'Europe']

sivo_app = Sivo.from_geodataframe(
    gdf=europe,
    id_col='ISO_A3',
    name_col='NAME',
    enable_minimap=True,
    render_mode='canvas' # or SVG
)

sivo_app.map(element_id="France", tooltip="France", zoom_on_click=True, zoom_level=3)

sivo_app.to_html("test_minimap.html")
print("Done")
