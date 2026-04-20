# Spike Map Example

This example demonstrates how to create a 3D-like "spike map" visualization using the `sivo` library. It reads simulated COVID-19 case density geospatial data from a `GeoDataFrame` and applies the `apply_spike_map` method to overlay triangular spikes proportional to the value of each region.

## Purpose

The main purpose of this test/example is to demonstrate:
1.  **Geospatial Integration:** Reading directly from a GeoPandas GeoDataFrame.
2.  **Spike Map Layering:** Overlaying ECharts `apply_spike_map` visualization using centroids and varying heights.
3.  **UI Configuration:** Disabling default sliding panels on click events (`default_panel_position="none"`).

## Key Code Components

1.  **GeoDataFrame Instantiation:**
    ```python
    app = Sivo.from_geodataframe(
        gdf=gdf,
        id_col='id',
        name_col='name',
        title="Spike Map Demo",
        subtitle="COVID-19 Case Density Representation",
        theme="light",
        default_panel_position="none"
    )
    ```
    This initializes the interactive SIVO application directly from the geometries and properties.

2.  **Spike Value Extraction:**
    ```python
    spike_data = {
        row['id']: {
            "value": row['cases'],
            "coord": [row.geometry.centroid.x, row.geometry.centroid.y]
        }
        for idx, row in gdf.iterrows()
    }
    ```
    It evaluates the required structure for `apply_spike_map`, dynamically inserting specific centroid locations to bypass basic bounding box calculations.

3.  **Applying the Spike Map Effect:**
    ```python
    app.apply_spike_map(spike_data, max_height=8.0, base_width=2.0, color="rgba(220, 38, 38, 0.8)")
    ```
    The height dynamically adjusts based on the value in relation to the global `max_height` and logical map bounds, creating an intuitive 3D density effect.

## How to Run

Ensure you have installed the required dependencies, primarily `sivo`, `geopandas`, and `shapely`. Then run:

```bash
python examples/maps/spike_map/spike_map.py
```

This will regenerate `examples/maps/spike_map/spike_map.html`, which can be opened in any modern web browser to view the visualization.