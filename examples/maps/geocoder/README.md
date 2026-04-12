# Geocoder Integration Example

This example demonstrates how to integrate a built-in search geocoder within a SIVO map utilizing a downloaded GeoDataFrame from Natural Earth.

## What is being shown
1. **Downloading Remote Shapefile Data:** Using standard Python libraries (`urlopen`, `ZipFile`) to fetch geographical country borders from a remote URL.
2. **Reading GeoDataFrames:** Using `geopandas` to process the `.shp` shapefile.
3. **Enabling Geocoding:** Using the native `enable_geocoder` feature inside the `Sivo.from_geodataframe()` initialization and configuring it to use the `nominatim` provider.

## Code Highlights
The essential parts of enabling the geocoder are found during the setup of the SIVO app:

```python
sivo_app = Sivo.from_geodataframe(
    gdf,
    id_col="ISO_A2",
    name_col="NAME",
    enable_geocoder=True,           # <--- Enables the search geocoder UI component
    geocode_provider="nominatim",   # <--- Uses Nominatim API for geocoding
    default_panel_position="none",  # <--- Hides the default side panel
    layout_size="90%"
)
```

## Running the Example
To run this example and generate the HTML output:

```bash
PYTHONPATH=src python3 examples/maps/geocoder/main.py
```

This will produce an `output.html` file in the same directory, which you can open in a browser to use the interactive SIVO map with search functionality.
