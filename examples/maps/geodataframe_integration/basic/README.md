# Basic GeoDataFrame Integration

This example demonstrates how to use the SIVO framework to generate an interactive map directly from a GeoPandas `GeoDataFrame`.

## What is being tested/shown
- Converting a GeoDataFrame (`geopandas.GeoDataFrame`) directly to a SIVO map format using `Sivo.from_geodataframe()`.
- Programmatically assigning tooltips, HTML content side panels, and element fill colors to the map using the `sivo_app.map()` function.
- Displaying dynamic HTML metrics in the `panel_position="right"` sidebar.

## Code Snippets

```python
# Create a SIVO map directly from a GeoDataFrame
sivo_app = Sivo.from_geodataframe(
    gdf=europe,
    id_col='ISO_A3',    # Unique ID mapping
    name_col='NAME',    # Display name mapping
    title="Interactive Europe Map",
    subtitle="Generated directly from a GeoPandas GeoDataFrame",
    theme="light",
    enable_minimap=True,
    disable_zoom_controls=False
)

# Map dynamic interactions onto map territories
sivo_app.map(
    element_id=country_id,
    tooltip=country_name,
    html=tooltip_html,
    color=color,
    hover_color="#31a354",
    panel_position="right"
)
```
