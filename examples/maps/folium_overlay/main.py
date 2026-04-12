import os
import folium
from sivo import Sivo

def create_example():
    # 1. Load the SVG template
    template_path = os.path.join(os.path.dirname(__file__), "template.svg")
    # Initialize the SIVO app with the template
    # We do not need a panel for this example, so we leave default_panel_position="none"
    app = Sivo.from_svg(template_path)

    # 2. Create an interactive Folium Map
    m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
    folium.Marker([45.5236, -122.6750], popup="Portland").add_to(m)

    # 3. Render Folium Map to an HTML string
    # We must get the HTML without saving to a file to inject it seamlessly
    map_html = m.get_root().render()

    # 4. Bind and clip the HTML directly over the `map_anchor` shape.
    # The true power of SIVO: the underlying ECharts renderer will provide the precise
    # pixel coordinates of `map_anchor` automatically to the frontend, even when the SVG is zoomed or panned.
    # `clip_html_to_shape` ensures it conforms strictly to the path boundary.
    # It will also automatically encode the raw HTML string into an iframe to prevent CSS collisions.
    app.clip_html_to_shape('map_anchor', map_html)

    # 5. Fill some dummy text in the other zone using SIVO's native SVG scalable text
    app.add_scalable_text(
        'dynamic_text_zone',
        "This is an example of embedding a fully interactive HTML map (Folium/Leaflet) directly into an SVG template.\n\n"
        "By utilizing the `clip_html_to_shape` method, SIVO automatically generates a CSS data-URI mask "
        "derived from the exact SVG path data of the underlying shape. This allows complex HTML components (like iframes or embedded maps) "
        "to be perfectly clipped and bounded by non-rectangular SVG artwork, scaling seamlessly alongside ECharts zoom interactions.",
        font_size="6%",
        color="#475569"
    )

    # 6. Export the bundled SIVO application
    output_html = os.path.join(os.path.dirname(__file__), "output.html")
    app.to_html(output_html)
    print(f"Generated {output_html}")

if __name__ == "__main__":
    create_example()
