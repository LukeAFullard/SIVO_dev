import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon
import os

url = "https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_state_20m.zip"
print("Reading shapefile...")
gdf = gpd.read_file(url)

non_contiguous = ['02', '15', '72', '60', '66', '69', '78']
gdf = gdf[~gdf['STATEFP'].isin(non_contiguous)]

bounds = gdf.total_bounds
minx, miny, maxx, maxy = bounds

def coord_to_svg(x, y):
    # Output raw geographic coordinates directly to the SVG!
    # Because ECharts boundingCoords is set to [[minx, miny], [maxx, maxy]],
    # it expects the SVG itself to be in this coordinate system.
    # Note: SVG Y-axis points down. Wait, if ECharts Y-axis points down in SVG, and latitude points up...
    # The prompt said: "Because standard map coordinates have a Y-axis pointing up (latitude) while SVG pixels point down, mapping raw geographic coordinates onto an SVG causes them to render upside-down. Do not alter the bounding_coords parameter structure in Sivo.from_svg (ECharts strictly requires [[minLng, minLat], [maxLng, maxLat]]). Instead, dynamically invert the latitude of each data point inside the Python script using the formula (maxLat + minLat) - actual_lat before calling apply_proportional_symbols."
    # Wait, if I dynamically invert the latitude of each data point, I MUST ALSO dynamically invert the latitude of the SVG path!
    # YES! The map.svg MUST have inverted latitudes so it matches the inverted data points!
    inverted_y = (maxy + miny) - y
    return f"{x:.4f},{inverted_y:.4f}"

def polygon_to_svg_path(poly):
    if poly.is_empty:
        return ""
    coords = list(poly.exterior.coords)
    d = "M " + coord_to_svg(*coords[0])
    for x, y in coords[1:]:
        d += " L " + coord_to_svg(x, y)
    d += " Z"
    return d

svg_paths = []
for geom in gdf.geometry:
    if isinstance(geom, Polygon):
        svg_paths.append(polygon_to_svg_path(geom))
    elif isinstance(geom, MultiPolygon):
        for poly in geom.geoms:
            svg_paths.append(polygon_to_svg_path(poly))

# ViewBox should match the geographic bounding box!
# viewBox="minX minY width height"
width = maxx - minx
height = maxy - miny
# But wait, inverted Y changes the bounds?
# No, min inverted Y is still miny! Because (maxy+miny)-maxy = miny.
svg_content = f"""<svg viewBox="{minx:.4f} {miny:.4f} {width:.4f} {height:.4f}" xmlns="http://www.w3.org/2000/svg">
    <!-- Background must NOT have a name attribute -->
    <rect x="{minx:.4f}" y="{miny:.4f}" width="{width:.4f}" height="{height:.4f}" fill="#e0f2fe" />
    <path id="usa_mainland" name="usa_mainland" d="{' '.join(svg_paths)}" fill="#bae6fd" stroke="#0ea5e9" stroke-width="0.05" />
</svg>"""

with open("map.svg", "w") as f:
    f.write(svg_content)

print(f"Generated SVG. Bounds: {minx:.4f}, {miny:.4f}, {maxx:.4f}, {maxy:.4f}")
