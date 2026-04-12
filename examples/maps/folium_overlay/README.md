# Folium Overlay Example

This example demonstrates how to embed a fully interactive HTML map (Folium/Leaflet) directly into an SVG template using SIVO.

By utilizing the `clip_html_to_shape` method, SIVO automatically generates a CSS data-URI mask derived from the exact SVG path data of the underlying shape. This allows complex HTML components (like iframes or embedded maps) to be perfectly clipped and bounded by non-rectangular SVG artwork, scaling seamlessly alongside ECharts zoom interactions.

## Key Concepts

*   **Loading an SVG Template**: The script uses `Sivo.from_svg()` to load a pre-existing SVG graphic that defines the layout, including specific shapes (like `map_anchor`) intended to hold content.
*   **Generating HTML Content**: A Folium map is created and rendered to an HTML string. This demonstrates how external libraries that output HTML can be integrated.
*   **Clipping HTML to SVG Shapes**: `app.clip_html_to_shape('map_anchor', map_html)` is the core feature. It takes the Folium HTML string and maps it onto the `map_anchor` element within the SVG. The true power here is that ECharts provides precise pixel coordinates to the frontend, allowing the HTML overlay to perfectly follow the SVG shape even when zoomed or panned. It also wraps the HTML in an iframe to isolate CSS.
*   **Scalable Text**: `app.add_scalable_text()` is used to dynamically inject descriptive text into another defined zone (`dynamic_text_zone`) within the SVG. This text scales correctly as a native SVG element.

## How to Run

1.  Ensure you have the required dependencies installed (including `folium`).
2.  Run the script: `PYTHONPATH=src python3 examples/maps/folium_overlay/main.py`
3.  Open the generated `output.html` file in your browser to interact with the map embedded within the custom SVG layout.