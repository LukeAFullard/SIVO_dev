# Flow Map Example

This example demonstrates how to create an interactive Flow Map (or network map) using SIVO.
Flow maps are incredibly powerful for visualizing the movement of goods, people, or information between different geographic locations.

## What is being tested/shown

1. **Geospatial Data Mocking**: We use `geopandas` and `shapely.geometry` to quickly mock up a grid map consisting of 4 hubs.
2. **Base Choropleth Layer**: We apply a dark choropleth background to the map.
3. **Flow Map Implementation**: Using `app.apply_flow_map()`, we plot trajectories indicating movement from an origin to a destination hub, applying arrow animations along the paths using the `flow_effect=True` and `effect_symbol="arrow"` parameters.
4. **Proportional Symbols**: Using `app.apply_proportional_symbols()`, we overlay pulsating nodes onto the origin and destination hubs, highlighting them clearly on the map.

## Code highlights

### Creating a map from a GeoDataFrame

We initialize `Sivo` directly from the `geopandas.GeoDataFrame`:

```python
    app = Sivo.from_geodataframe(
        gdf=gdf,
        id_col='id',
        name_col='name',
        title="Flow Map Demo",
        subtitle="Domestic Flight Volume Simulation",
        theme="dark",
        disable_panel=True
    )
```

### Drawing Flow Lines

We create our array of connections (origin, destination, value, coordinates) and pass it to SIVO to generate animated lines:

```python
    flow_data = [
        {"origin": "Hub1", "destination": "Hub4", "value": 3200, "label": "SEA-JFK", "color": "#38bdf8", "source_coord": centroids["Hub1"], "target_coord": centroids["Hub4"]},
        ...
    ]

    app.apply_flow_map(flow_data, min_width=1.0, max_width=6.0, flow_effect=True, effect_symbol="arrow", animation_speed=2.0)
```

### Adding Animated Nodes

To emphasize the nodes, we add pulsating circles at the origin/destination coordinates:

```python
    nodes_data = {
        "Hub1": {"value": 1, "coord": centroids["Hub1"], "color": "#38bdf8"},
        ...
    }
    app.apply_proportional_symbols(nodes_data, min_size=12.0, max_size=12.0, is_pulse=True)
```
