---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# H-14: Advanced Mapping Guide

SIVO provides built-in methods for creating advanced thematic maps effortlessly. These maps allow you to visualize your data through various statistical and geographical representations directly over your SVG base layers.

## 1. Introduction to Thematic Mapping

Thematic mapping involves styling geographic features based on data values. With SIVO, you can automatically convert a base SVG map into a rich data visualization using methods like `apply_choropleth()`, `apply_hexbin()`, and more. These methods abstract away the complexity of calculating color scales, interpolating values, and rendering ECharts series.

## 2. Choropleth Maps

A choropleth map uses color to represent data values across different regions (e.g., states, counties). SIVO automatically interpolates colors between a minimum and maximum value.

```python
from sivo import Sivo

# Load a base SVG map
sivo_app = Sivo.from_svg("us_states.svg")

# Data mapping SVG element IDs to numeric values
population_data = {
    "CA": 39538223,
    "TX": 29145505,
    "FL": 21538187,
    "NY": 20201249,
    "IL": 12812508
}

# Apply choropleth styling
sivo_app.apply_choropleth(
    data_map=population_data,
    min_color="#e0f3db",
    max_color="#0868ac",
    show_legend=True
)
```

## 3. Hexbin & Dot Density

When mapping individual points or densities, SIVO provides clustering and distribution methods.

### Hexbin Layer Overlay

The `apply_hexbin()` method aggregates a list of `[x, y]` coordinates into hexagonal bins, rendering a heat-map style overlay.

```python
point_data = [
    [120.5, 30.2], [121.0, 31.5], [120.8, 30.9],
    # ... more coordinates
]

sivo_app.apply_hexbin(
    points=point_data,
    hex_size=20.0,
    color_palette=["#ffffcc", "#41b6c4", "#253494"],
    min_opacity=0.4,
    max_opacity=0.9
)
```

### Dot Density Map

The `apply_dot_density()` method randomly distributes a specified number of dots within the bounding box of each mapped region to visually represent quantities.

```python
density_data = {
    "region_A": 500,  # 500 dots will be rendered
    "region_B": 1200
}

sivo_app.apply_dot_density(
    data_map=density_data,
    dot_size=4.0,
    dot_color="rgba(255, 165, 0, 0.8)",
    dots_per_value=1.0  # e.g., 1 dot = 100 people if you set this to 0.01
)
```

## 4. Proportional Symbols & Flow Maps

These methods overlay elements based on calculated centers of SVG regions.

### Proportional Symbols (Bubble Map)

The `apply_proportional_symbols()` method sizes circular markers based on data values.

```python
sales_data = {
    "store_1": 15000,
    "store_2": 8500,
    "store_3": {"value": 24000, "color": "#00ff00"} # Custom color for specific marker
}

sivo_app.apply_proportional_symbols(
    data_map=sales_data,
    min_size=10.0,
    max_size=60.0,
    color="rgba(59, 130, 246, 0.7)",
    is_pulse=True  # Adds an animated pulsing effect
)
```
*Note: You can also pass explicit coordinates instead of SVG IDs by passing a dictionary with a `"coord"` key.*

### Flow Maps

Visualize movement or connections between regions using `apply_flow_map()`.

```python
flow_data = [
    {"origin": "ny", "destination": "lon", "value": 100, "label": "Route 1"},
    {"origin": "ny", "destination": "par", "value": 50, "color": "#00ff00"}
]

sivo_app.apply_flow_map(
    data_list=flow_data,
    min_width=2.0,
    max_width=8.0,
    color="rgba(239, 68, 68, 0.6)",
    flow_effect=True,
    effect_symbol="arrow",
    animation_speed=4.0
)
```

## 5. Other Mapping Features

### Spike Maps

Render spikes or bars originating from the center of regions.

```python
spike_data = {
    "city_a": 45.5,
    "city_b": 89.2
}

sivo_app.apply_spike_map(
    data_map=spike_data,
    max_height=150.0,
    base_width=15.0,
    color="rgba(139, 92, 246, 0.8)"
)
```

### Value by Alpha

A bivariate choropleth technique where the base color represents one variable, and the opacity (alpha) represents a second variable.

```python
income_data = {"zip1": 50000, "zip2": 120000}
population_density = {"zip1": 100, "zip2": 5000}

sivo_app.apply_value_by_alpha(
    base_data_map=income_data,
    alpha_data_map=population_density,
    min_color="#fee5d9",
    max_color="#a50f15",
    min_alpha=0.1,
    max_alpha=1.0
)
```

### Categorical Map

Map discrete string categories to specific colors.

```python
land_use_data = {
    "zone_1": "Residential",
    "zone_2": "Commercial",
    "zone_3": "Industrial"
}

palette = {
    "Residential": "#2ca02c",
    "Commercial": "#1f77b4",
    "Industrial": "#ff7f0e"
}

sivo_app.apply_categorical_map(
    data_map=land_use_data,
    color_palette=palette,
    show_legend=True
)
```

## 6. Geocoding integration

SIVO allows you to enable client-side geocoding in your maps, which displays a search bar to find and zoom to locations. SIVO supports 'nominatim' (open, default), 'mapbox', or 'google' as providers.

When instantiating `Sivo`, pass the geocoding parameters:

```python
sivo_app = Sivo.from_string(
    svg_string,
    enable_geocoder=True,
    geocode_provider="mapbox", # or 'google', or 'nominatim'
    geocode_api_key="your_api_key_here" # Not required for 'nominatim'
)
```
When a user searches for an address, SIVO will fetch the coordinates, zoom the map to that location, and temporarily place an animated pulsing marker at the destination.

## SVG Internal Logic

For a deeper technical dive into the SVG parsing and lxml interactions used by SIVO, please refer to [SVG Logic Internals](../ai/svg-logic-internals.md).
