import os
from sivo import Sivo

def main():
    sivo_app = Sivo.from_svg(
        os.path.join(os.path.dirname(__file__), "map.svg"),
        title="Custom Map Embeds",
        subtitle="Click a location to view interactive Leaflet/D3 maps inside the SIVO sidebar.",
        default_panel_position="right"
    )

    # 1. Embed a custom local HTML map (e.g., exported from Folium/Leaflet)
    # The 'website' provider injects an iframe that can point to any local or remote HTML file.
    sivo_app.map(
        element_id="hq",
        html="<h3>Global HQ</h3><p>This is a custom Leaflet map embedded via iframe.</p>",
        social={"provider": "website", "url": "folium_map.html"},
        hover_color="#60a5fa",
        glow=True
    )

    # 2. Embed an external remote website inside the iframe
    sivo_app.map(
        element_id="spike_demo",
        html="<h3>Data Visualization</h3><p>An embedded external web page detailing topics related to this map element.</p>",
        social={"provider": "website", "url": "https://en.wikipedia.org/wiki/Data_visualization"},
        hover_color="#f87171",
        glow=True
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Generated custom geospatial maps example at {output_path}")

if __name__ == "__main__":
    main()
