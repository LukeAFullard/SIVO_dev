import geopandas as gpd
url = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
world = gpd.read_file(url)
europe = world[world.CONTINENT == 'Europe']
bounds = europe.total_bounds
print(bounds)
