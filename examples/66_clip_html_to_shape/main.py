import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from sivo import Sivo

try:
    import folium
except ImportError:
    print("Please install folium to run this example: pip install folium")
    sys.exit(1)

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "layout.svg")

    sivo_app = Sivo.from_svg(
        svg_path,
        disable_panel=True,
        render_mode="canvas"
    )

    # Generate a Folium map
    print("Generating Folium map...")
    m = folium.Map(location=[48.8584, 2.2945], zoom_start=13, control_scale=True, tiles="CartoDB positron")
    folium.Marker([48.8584, 2.2945], popup="Eiffel Tower").add_to(m)

    # We must render the Folium map to HTML
    folium_html = m.get_root().render()

    # Folium map HTML needs to fill the space
    iframe_html = f"""
    <div style="width: 100%; height: 100%;">
        <iframe style="width: 100%; height: 100%; border: none;" srcdoc="{folium_html.replace('"', '&quot;')}"></iframe>
    </div>
    """

    print("Clipping HTML to SVG shape...")
    # Clip the Folium map HTML exactly to the bounds of the "map_container" path
    sivo_app.clip_html_to_shape(
        element_id="map_container",
        html=iframe_html,
        pointer_events="auto" # Important to allow map interactions (pan/zoom)
    )

    # We map the text to hide itself or change color, though the map will cover it
    # SIVO naturally handles standard mappings along with the clip
    sivo_app.map(
        element_id="hover_info",
        tooltip="This text is beneath the Folium map"
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported interactive HTML with Folium to {output_path}")

if __name__ == "__main__":
    main()
