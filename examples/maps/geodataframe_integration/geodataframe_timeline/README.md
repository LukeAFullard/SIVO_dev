# GeoDataFrame Timeline Integration Example

This example demonstrates how to integrate timeline data using `GeoDataFrame` mapping capabilities in SIVO.

## Overview
It builds an interactive map showing European countries, animated over time. We fetch country data using `geopandas` from a remote GeoJSON dataset of the world, filter it to Europe, and generate a timeline tracking simulated 'discovery' dates with associated synthetic population data mapping dynamically mapped to a heatmap over four distinct periods: 1900, 1950, 2000, 2020.

Additionally, it adds two right-hand slideout panels bound to specific countries ('FRA', and 'GBR') that trigger embedded nested timeline and mapping ECharts within the side panel layout container.

## Key Features & Code Snippets

- **Sivo.from_geodataframe()**: Creates the initial SIVO application directly from the `europe` subset GeoDataFrame mapping properties to an ID column (`ISO_A3`), name column (`NAME`), and basic visualization states like disabling zoom controls.

  ```python
  sivo_app = Sivo.from_geodataframe(
      gdf=europe,
      id_col='ISO_A3',
      name_col='NAME',
      title="Interactive Europe Map Over Time",
      subtitle="Animating GeoDataFrames by Year",
      theme="light",
      disable_zoom_controls=False
  )
  ```

- **Timeline Binding (`bind_timeline`)**: Binds timeline dataset dynamically using color ranges across mapped data values (`population`) updating continuously through automatic interval replay loops (`auto_play=True`, `play_interval=1500`, `loop=True`). Missing elements fallback nicely using `outOfRange` mapping definitions or default transparency fallback behaviors built into the timeline visualization mechanism over years specified.

  ```python
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
  ```

- **Nested Dynamic Map Overlays (`sivo_app.map()`)**: Employs `.map()` explicitly applying comprehensive nested `echarts_option` timelines rendering fully scoped independent charts on specific `element_id` clicks (such as clicking France `FRA`), injecting dynamically derived `map_data` back into the context utilizing standard position attributes (`panel_position="right"`).

  ```python
  sivo_app.map(
      element_id="FRA",
      tooltip="France - Click to view Population Timeline",
      echarts_option=sidebar_timeline_option,
      map_name="europe_geojson",
      map_data=json.loads(europe.to_json()), # Pass GeoJSON dict
      panel_position="right",
      open_by_default=False
  )
  ```

## Running the Example
Execute the Python script:

```bash
python example.py
```

It will generate the `interactive_europe_timeline.html` output visualizing the comprehensive animated visualization and sidebar nested map layouts.
