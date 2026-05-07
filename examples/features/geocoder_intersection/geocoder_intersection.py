from sivo.core.sivo import Sivo

def create_example():
    svg_str = '''<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
        <rect width="800" height="600" fill="#f0fdf4"/>
        <text id="zone_result" x="400" y="300" font-size="24" text-anchor="middle" fill="#333">Search your address using the geocoder in the top right.</text>
    </svg>'''

    app = Sivo.from_string(
        svg_str,
        enable_geocoder=True,
        geocode_country_codes="nz", # Restrict searches to New Zealand
        title="Find your management zone"
    )

    app.bind_geocoder_intersection(
        geojson_url="https://maps.horizons.govt.nz/arcgis/rest/services/LocalMapsPublic/Public_OnePlan/MapServer/3/query?where=1%3D1&outFields=*&f=geojson",
        display_element_id="zone_result",
        property_name="SurfaceWaterManageSubareaName",
        no_result_text="You are outside the management zone."
    )

    output_path = "geocoder_intersection_example.html"
    app.to_html(output_path=output_path)
    print(f"Generated example at {output_path}")

if __name__ == "__main__":
    create_example()
