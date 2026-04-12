# Geospatial Sidebar Example

This example demonstrates how to integrate external interactive geospatial maps within a SIVO side panel natively. This is particularly useful when mapping real-world locations from simplified abstract diagrams or non-geospatial SVG representations.

When you interact with the mapped elements (like `hq`, `branch1`, `branch2`) on the abstract main map, SIVO intercepts the interaction and renders a live, interactive geospatial map embedded within a side panel.

## Key Features Demonstrated

- **`map_location` property**: Maps a native SVG element to a geospatial location to be dynamically shown in an embedded iframe/map block.
- **Address resolution**: You can pass raw strings like `1 Market St, San Francisco, CA` or famous landmarks like `Tokyo Tower, Japan`. The backend resolves this to show the correct map.
- **Lat/Long resolution**: You can pass exact decimal coordinates such as `51.5074, -0.1278` which are useful for precise dropping.
- **`panel_position` enforcement**: We explicitly set `default_panel_position="right"` in `Sivo.from_svg` (and on `.map()`) so that the dynamically loaded geospatial map renders in a clean sidebar on the right instead of acting as an overlay or defaulting to none.

## Relevant Code snippet

```python
sivo_app = Sivo.from_svg(
    "map.svg",
    title="Geospatial Sidebar Maps",
    subtitle="Click a location to view its real-world geospatial map in the sidebar.",
    default_panel_position="right"
)

# 1. Map to an exact address
sivo_app.map(
    element_id="hq",
    html="<h3>Global Headquarters</h3><p>Located in the heart of San Francisco.</p>",
    map_location="1 Market St, San Francisco, CA", # Text address
    hover_color="#60a5fa",
    glow=True,
    panel_position="right"
)
```

## Running the Example

Run the following command from the root of the repository:

```bash
PYTHONPATH=src python3 examples/maps/geospatial_sidebar/main.py
```

This will parse the `map.svg`, apply the interactions and layout logic, and generate a self-contained `output.html` that you can open in any browser.
