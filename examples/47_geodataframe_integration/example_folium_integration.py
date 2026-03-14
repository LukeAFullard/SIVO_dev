import os
import random
import geopandas as gpd
import folium
from folium.plugins import TimestampedGeoJson
from sivo.core.sivo import Sivo

def create_folium_maps():
    """Generates standalone Leaflet HTML files using Folium."""
    print("Generating standalone Folium/Leaflet maps...")

    # 1. Standard Leaflet Map for France
    m_france = folium.Map(location=[46.603354, 1.888334], zoom_start=5)
    folium.Marker([48.8566, 2.3522], popup='Paris').add_to(m_france)
    folium.Marker([45.7640, 4.8357], popup='Lyon').add_to(m_france)
    france_path = os.path.join(os.path.dirname(__file__), 'folium_france.html')
    m_france.save(france_path)

    # 2. Timeline Leaflet Map for Germany (using TimestampedGeoJson)
    m_germany = folium.Map(location=[51.165691, 10.451526], zoom_start=5)

    # Generate some fake temporal GeoJSON data for points in Germany
    lines = [
        {
            'coordinates': [
                [13.404954, 52.520008], # Berlin
                [9.993682, 53.551086],  # Hamburg
                [11.581981, 48.135125], # Munich
            ],
            'dates': [
                '2021-01-01T00:00:00',
                '2021-02-01T00:00:00',
                '2021-03-01T00:00:00'
            ],
            'color': 'red'
        }
    ]

    features = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'LineString',
                'coordinates': line['coordinates'],
            },
            'properties': {
                'times': line['dates'],
                'style': {'color': line['color'], 'weight': 5}
            }
        } for line in lines
    ]

    TimestampedGeoJson(
        {'type': 'FeatureCollection', 'features': features},
        period='P1M',
        add_last_point=True,
        auto_play=True,
        loop=True,
        max_speed=1,
        loop_button=True,
        date_options='YYYY/MM/DD',
        time_slider_drag_update=True
    ).add_to(m_germany)

    germany_path = os.path.join(os.path.dirname(__file__), 'folium_germany_timeline.html')
    m_germany.save(germany_path)

    return france_path, germany_path

def main():
    print("Fetching Natural Earth dataset for the main SIVO map...")
    url = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
    world = gpd.read_file(url)
    europe = world[world.CONTINENT == 'Europe'].copy()

    # Generate the Folium maps that we will embed
    france_path, germany_path = create_folium_maps()

    # Create the main SIVO Map (ECharts SVG native)
    sivo_app = Sivo.from_geodataframe(
        gdf=europe,
        id_col='ISO_A3',
        name_col='NAME',
        title="Interactive Europe Map with Leaflet Embeds",
        subtitle="Click France or Germany to open a nested Leaflet/Folium map in the sidebar.",
        theme="light",
        enable_minimap=True,
        disable_zoom_controls=False
    )

    # We map 'France' to open the standard folium map in the sidebar
    # We use the 'social' (website iframe) embed action which cleanly sandboxes external HTML.
    # Note: 'from_geodataframe' sets the SVG element names. In the dataset, the column is 'NAME'.
    sivo_app.map(
        element_id="France",
        tooltip="France - Click to view standard Folium Map",
        social={"provider": "website", "url": "folium_france.html"},
        color="#a6bddb" # Light blue to highlight interactivity
    )

    # We map 'Germany' to open the folium timeline map in the sidebar
    sivo_app.map(
        element_id="Germany",
        tooltip="Germany - Click to view Folium Timeline Map",
        social={"provider": "website", "url": "folium_germany_timeline.html"},
        color="#a6bddb"
    )

    # Save to HTML
    output_path = os.path.join(os.path.dirname(__file__), 'interactive_europe_with_folium.html')
    sivo_app.to_html(output_path)
    print(f"Successfully generated main interactive HTML at: {output_path}")

if __name__ == "__main__":
    main()
