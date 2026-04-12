# Timeline Animation with GeoDataFrames

This example showcases how to create dynamic temporal (timeline) map animations using SIVO and GeoDataFrames.

## What is being tested/shown
- Binding a temporal timeline animation dataset to a map using `sivo_app.bind_timeline()`. This plays through a continuous series of changing datasets over time (e.g., simulating discovery years and population growth).
- Passing custom `echarts_option` objects into a side panel map configuration so that clicking a map area triggers a "nested" drill-down map view showing additional, specialized metrics or timeline animations for the same geographic boundaries.

## Code Snippets

```python
# Bind main timeline dataset
sivo_app.bind_timeline(
    data=timeline_data,
    key="population",
    colors=["#fee0d2", "#fc9272", "#de2d26"], # Color spectrum
    min_val=1000000,
    max_val=80000000,
    auto_play=True,
    play_interval=1500, # ms per year transition
    loop=True
)

# Map nested ECharts timeline options inside side panels
sivo_app.map(
    element_id="FRA",
    tooltip="France - Click to view Population Timeline",
    echarts_option=sidebar_timeline_option,
    map_name="europe_geojson",
    map_data=json.loads(europe.to_json()), # Use GeoJSON natively
    panel_position="right",
    open_by_default=False
)
```
