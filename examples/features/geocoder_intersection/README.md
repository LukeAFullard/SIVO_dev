# Geocoder Point-in-Polygon (PIP) Intersection

This example demonstrates how to use the `bind_geocoder_intersection()` method to perform a client-side point-in-polygon (PIP) analysis when a user searches for an address.

## Overview

SIVO includes built-in geocoding functionality via the `geocode_provider` configuration (e.g., Nominatim, Mapbox, Google). Usually, when a user searches for an address, SIVO pans and zooms the ECharts map to drop a marker at that location.

However, in some dashboard scenarios, you may not want a map marker at all. Instead, you might want to silently look up the user's coordinates, check if those coordinates fall within a specific geographic zone (like a local voting district, environmental management area, or delivery zone), and just return the name of that zone as text on the screen.

SIVO achieves this by allowing you to bind a remote GeoJSON URL. When the user searches for an address:
1. SIVO looks up the `[longitude, latitude]` of the address using the geocoding provider.
2. It fetches the remote GeoJSON dataset (which can contain complex `Polygons` and deeply nested `MultiPolygons`).
3. It performs a client-side ray-casting Point-in-Polygon intersection.
4. If the point intersects a feature, it extracts a specific property (e.g., the zone's name) and displays it on the screen.

SIVO handles all of this natively using a high-z-index HTML overlay, bypassing map behavior completely, and providing built-in "Calculating zone..." UI loading states to accommodate large remote datasets.

## Key Code Snippets

```python
from sivo.core.sivo import Sivo
import textwrap

# 1. Create a blank SVG as the base
svg_content = textwrap.dedent("""\
    <svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
        <rect width="800" height="600" fill="#f0fff4"/>
        <text id="main_text" x="400" y="300" text-anchor="middle" font-size="24" fill="#333">
            Search your address in the top right.
        </text>
    </svg>
""")

# 2. Initialize SIVO with a geocoder, restricted to a specific country
app = Sivo.from_string(
    svg_content,
    enable_geocoder=True,
    geocode_provider="nominatim",
    geocode_country_codes="nz", # Restrict search to New Zealand
    geocode_placeholder="Find your management zone"
)

# 3. Bind the geocoder intersection logic
#    We will use a real remote GeoJSON of environmental management zones
app.bind_geocoder_intersection(
    geojson_url="https://maps.horizons.govt.nz/arcgis/rest/services/LocalMapsPublic/Public_OnePlan/MapServer/3/query?where=1%3D1&outFields=*&f=geojson",
    display_element_id="main_text",
    property_name="WMA_NAME",
    no_result_text="Address not found in any management zone."
)

app.to_html("output.html")
```

## Running the Example
Run the script to generate the interactive bundle:
```bash
python geocoder_intersection.py
```
Then open `output.html` in your web browser. Try searching for `107 Hillcrest Drive, Kelvin Grove` to see the intersection succeed.
