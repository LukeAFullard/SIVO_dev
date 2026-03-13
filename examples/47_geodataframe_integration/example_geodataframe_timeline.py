import geopandas as gpd
from sivo.core.sivo import Sivo
import os
import json

def main():
    print("Fetching Natural Earth LowRes dataset to create a dummy temporal dataset...")
    # Fetching the GeoJSON directly since geopandas 1.0 removed built-in datasets
    url = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
    world = gpd.read_file(url)

    # Let's filter to just Europe to keep it manageable
    europe = world[world.CONTINENT == 'Europe'].copy()

    # Create a synthetic dataset showing "Discovered Territories" over time
    # To demonstrate animating geometries appearing over time, we will assign
    # different random "discovery" years to countries.
    import random
    random.seed(42)

    # We create a dictionary of timeline data
    # format: { "Year": { "CountryName": { "population": metric_value } } }
    # NOTE: SIVO's data/timeline binding maps data onto the visualMap using the SVG 'name' attribute, not 'id'.
    timeline_data = {}
    years = ["1900", "1950", "2000", "2020"]

    # Assign each country a random discovery year
    europe['discovery_year'] = [random.choice(years) for _ in range(len(europe))]

    for year in years:
        timeline_data[year] = {}
        for idx, row in europe.iterrows():
            country_name = row['NAME']
            base_pop = row['POP_EST']
            disc_year = row['discovery_year']

            # If the country was discovered in or before this year, it gets a value
            # Otherwise, we leave it out of the dictionary.
            # SIVO's timeline binding will update the ECharts series data per year.
            # If an item is missing in that year's data, its value becomes undefined.
            # We use the visualMap's "outOfRange" setting to hide undefined items completely.
            if int(year) >= int(disc_year):
                # Simulate population growth: Starts small at discovery and grows to base_pop by 2020
                years_since_discovery = int(year) - int(disc_year)
                total_years = 2020 - int(disc_year)

                # To make the animation obvious, the color will scale dramatically
                if total_years > 0:
                    growth_factor = 0.2 + (0.8 * (years_since_discovery / total_years))
                else:
                    growth_factor = 1.0 # 2020 discovery

                current_pop = int(base_pop * min(growth_factor, 1.0))
                timeline_data[year][country_name] = {"population": current_pop}

    print(f"Loaded {len(europe)} European countries across {len(years)} years.")

    # 1. Main Frame Animation: Convert the entire GeoDataFrame into a SIVO map
    sivo_app = Sivo.from_geodataframe(
        gdf=europe,
        id_col='ISO_A3',
        name_col='NAME',
        title="Interactive Europe Map Over Time",
        subtitle="Animating GeoDataFrames by Year",
        theme="light",
        enable_minimap=True,
        disable_zoom_controls=False
    )

    # Bind the timeline data
    # We provide a color scale for the population.
    sivo_app.bind_timeline(
        data=timeline_data,
        key="population",
        colors=["#fee0d2", "#fc9272", "#de2d26"], # Light red to Dark red
        min_val=1000000,
        max_val=80000000,
        auto_play=True,
        play_interval=1500, # 1.5 seconds per year
        loop=True
    )

    # To ensure countries that haven't been "discovered" yet are completely hidden,
    # we can map the `outOfRange` property directly into the global visualMap via an overlay,
    # or rely on SIVO's default "transparent" for missing values.
    # Let's add tooltips for all countries:
    for idx, row in europe.iterrows():
        country_id = row['ISO_A3']
        country_name = row['NAME']
        sivo_app.map(
            element_id=country_id,
            tooltip=country_name,
            html=f"<h3>{country_name}</h3><p>Appears in: {row['discovery_year']}</p>"
        )

    # 2. Sidebar Animation (Nested Map):
    # The user also asked how to do this in the side bar.
    # We can embed an ECharts Option object with a timeline into an element's side panel.

    # Let's pick France as a trigger to open the sidebar with a temporal map.
    # To animate a nested map in the sidebar, we construct an ECharts timeline option.
    sidebar_base_option = {
        "title": {"text": "Temporal Population Density (Sidebar)"},
        "tooltip": {"trigger": "item"},
        "visualMap": {
            "min": 1000000,
            "max": 80000000,
            "inRange": {"color": ["#fee0d2", "#fc9272", "#de2d26"]},
            "outOfRange": {"opacity": 0} # Hide elements not in the current year
        },
        "series": [{
            "type": "map",
            "map": "europe_geojson", # We will register this name
            "roam": True
        }]
    }

    # Construct the full ECharts option with timeline
    sidebar_timeline_option = {
        "baseOption": sidebar_base_option,
        "options": []
    }

    # Build the options array for each year
    for year in years:
        year_series_data = []
        for idx, row in europe.iterrows():
            country_name = row['NAME']

            # ECharts timeline merges series data. We MUST explicitly include all geometries
            # and set their value to '-' if they are missing, otherwise they inherit the previous year's value.
            if country_name in timeline_data[year]:
                val = timeline_data[year][country_name]["population"]
            else:
                val = '-'

            year_series_data.append({
                "name": country_name,
                "value": val
            })

        sidebar_timeline_option["options"].append({
            "title": {"text": f"Year: {year}"},
            "series": [{"data": year_series_data}]
        })

    sidebar_timeline_option["baseOption"]["timeline"] = {
        "axisType": 'category',
        "autoPlay": True,
        "playInterval": 1500,
        "data": years
    }

    # Map the nested chart to a specific element (e.g., clicking France opens the sidebar)
    # Note: Echarts requires the GeoJSON data to register the nested map. We use the Europe dataframe.
    try:
        sivo_app.map(
            element_id="FRA",
            tooltip="France - Click to view Sidebar Timeline",
            echarts_option=sidebar_timeline_option,
            map_name="europe_geojson",
            map_data=json.loads(europe.to_json()), # Pass GeoJSON dict
            panel_position="right",
            open_by_default=False
        )
    except ValueError:
        pass # In case FRA isn't in the dataset

    # Save to HTML
    output_path = os.path.join(os.path.dirname(__file__), 'interactive_europe_timeline.html')
    sivo_app.to_html(output_path)
    print(f"Successfully generated interactive HTML at: {output_path}")

if __name__ == "__main__":
    main()
