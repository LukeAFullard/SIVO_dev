# Custom Geospatial Sidebar Example

This example demonstrates how to embed interactive, third-party mapping libraries or web components inside a SIVO sidebar using the `social` embedding feature with the `"website"` provider.

## What is being tested/demonstrated
- Instantiating a SIVO app from a native SVG map using `Sivo.from_svg()`.
- Setting a global default sidebar location via `default_panel_position="right"`.
- Mapping specific SVG elements (`hq`, `spike_demo`) to interactive actions.
- Embedding local HTML files (like a Leaflet map exported from Folium) inside the sidebar iframe using `social={"provider": "website", "url": "folium_map.html"}`.
- Embedding external, remote web visualizations (like an Observable HQ D3 spike map) using `social={"provider": "website", "url": "..."}`.

## Relevant Code

The core of the logic happens within the `sivo_app.map()` function. When a user clicks on an element, the mapped interactive content displays in the sidebar.

```python
sivo_app = Sivo.from_svg(
    "map.svg",
    title="Custom Map Embeds",
    default_panel_position="right"
)

# Embed a local interactive HTML map
sivo_app.map(
    element_id="hq",
    html="<h3>Global HQ</h3><p>This is a custom Leaflet map embedded via iframe.</p>",
    social={"provider": "website", "url": "folium_map.html"}
)

# Embed an external data visualization
sivo_app.map(
    element_id="spike_demo",
    html="<h3>D3 Spike Map</h3><p>An interactive, data-driven visualization from Observable embedded seamlessly.</p>",
    social={"provider": "website", "url": "https://observablehq.com/embed/@d3/spike-map?cells=chart"}
)
```

## Running the Example

Run the following command from the root directory to generate the `output.html` artifact:

```bash
PYTHONPATH=src python3 examples/maps/custom_geospatial_sidebar/main.py
```
