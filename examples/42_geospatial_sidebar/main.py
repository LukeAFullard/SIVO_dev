import os
from sivo import Sivo

def main():
    sivo_app = Sivo.from_svg(
        os.path.join(os.path.dirname(__file__), "map.svg"),
        title="Geospatial Sidebar Maps",
        subtitle="Click a location to view its real-world geospatial map in the sidebar."
    )

    # 1. Map to an exact address
    sivo_app.map(
        element_id="hq",
        tooltip="San Francisco HQ",
        html="<h3>Global Headquarters</h3><p>Located in the heart of San Francisco.</p>",
        map_location="1 Market St, San Francisco, CA", # Text address
        hover_color="#60a5fa",
        glow=True
    )

    # 2. Map to a specific Latitude / Longitude coordinate
    sivo_app.map(
        element_id="branch1",
        tooltip="London Office",
        html="<h3>London Branch</h3><p>Coordinates: 51.5074, -0.1278</p>",
        map_location="51.5074, -0.1278", # Exact Lat/Long
        hover_color="#34d399",
        glow=True
    )

    # 3. Map to another famous location
    sivo_app.map(
        element_id="branch2",
        tooltip="Tokyo Office",
        html="<h3>Tokyo Branch</h3><p>Near Tokyo Tower</p>",
        map_location="Tokyo Tower, Japan",
        hover_color="#fbbf24",
        glow=True
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Generated geospatial maps example at {output_path}")

if __name__ == "__main__":
    main()
