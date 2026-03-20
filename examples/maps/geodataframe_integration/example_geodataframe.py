import geopandas as gpd
from sivo.core.sivo import Sivo
import os

def main():
    print("Fetching Natural Earth LowRes dataset...")
    # Fetching the GeoJSON directly since geopandas 1.0 removed built-in datasets
    url = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
    world = gpd.read_file(url)

    # Let's filter to just Europe to keep the HTML smaller and cleaner for the example
    europe = world[world.CONTINENT == 'Europe']

    print(f"Loaded {len(europe)} European countries.")

    # Convert the GeoDataFrame directly into a SIVO interactive map
    # We use 'iso_a3' as the unique ID and 'name' as the display name
    # We use 'ISO_A3' as the unique ID and 'NAME' as the display name
    sivo_app = Sivo.from_geodataframe(
        gdf=europe,
        id_col='ISO_A3',
        name_col='NAME',
        title="Interactive Europe Map",
        subtitle="Generated directly from a GeoPandas GeoDataFrame",
        theme="light",
        enable_minimap=True,
        disable_zoom_controls=False
    )

    # Let's map some interactions!
    # Let's add tooltips showing population and GDP for each country
    for idx, row in europe.iterrows():
        country_id = row['ISO_A3']
        country_name = row['NAME']
        pop = row['POP_EST']
        gdp = row['GDP_MD']

        # Color countries by population
        if pop > 50000000:
            color = "#de2d26" # High pop
        elif pop > 10000000:
            color = "#fc9272" # Med pop
        else:
            color = "#fee0d2" # Low pop

        tooltip_html = f"""
        <div style="font-family: sans-serif; padding: 10px;">
            <h3>{country_name}</h3>
            <p><strong>Population:</strong> {pop:,}</p>
            <p><strong>GDP (MD EST):</strong> ${gdp:,}</p>
        </div>
        """

        # We handle any missing ISO codes gracefully by wrapping in try/except or just mapping directly
        try:
            sivo_app.map(
                element_id=country_id,
                tooltip=country_name,
                html=tooltip_html,
                color=color,
                hover_color="#31a354"
            )
        except ValueError:
            # Some entries might lack a valid ISO code in the dataset
            pass

    # Save to HTML
    output_path = os.path.join(os.path.dirname(__file__), 'interactive_europe.html')
    sivo_app.to_html(output_path)
    print(f"Successfully generated interactive HTML at: {output_path}")

if __name__ == "__main__":
    main()
