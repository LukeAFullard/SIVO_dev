---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Infographics

The `Infographic` class (`src/sivo/core/infographic.py`) provides tools for building static and dynamic data visualizations. While standard `Sivo` maps and `SivoDashboard` projects focus heavily on UI layouts and general interactivity, the `Infographic` class adds specialized capabilities like thematic mapping, data binding, and programmatic overlays to transform SVG graphics into data-rich stories.

## Initializing an Infographic

Initialization is similar to standard `Sivo` maps, starting from an SVG file, a raw string, or a JSON configuration.

```python
from sivo.core.infographic import Infographic

# Initialize from an SVG file
info = Infographic.from_svg("my_base_map.svg")
```

## Data Binding

You can bind quantitative datasets directly to your map elements to create thematic color scales automatically.

```python
# Bind data to dynamically color IDs based on a scale
info.bind_data(
    data={
        "region_1": {"value": 50},
        "region_2": {"value": 85},
        "region_3": {"value": 20}
    },
    key="value",
    colors=["#e0f3f8", "#014636"], # Light blue to dark green
    min_val=0,
    max_val=100
)
```

For animated timelines, you can use `bind_timeline` with temporal data:

```python
# Bind time-series data for an animated map
timeline_data = {
    "2020": {"region_1": {"value": 10}, "region_2": {"value": 20}},
    "2021": {"region_1": {"value": 15}, "region_2": {"value": 30}}
}

info.bind_timeline(
    data=timeline_data,
    key="value",
    colors=["#fee5d9", "#a50f15"],
    min_val=0,
    max_val=50,
    auto_play=True
)
```

## Advanced Mapping Layers

`Infographic` implements several `apply_*` methods for generating complex thematic map layers.

### Hexbin Maps

Creates a hexagonal binning overlay by aggregating `[x, y]` coordinates.

```python
# Apply a hexbin overlay
points = [[100, 200], [105, 205], [300, 400]]
info.apply_hexbin(
    points=points,
    hex_size=15.0,
    color_palette=["#e0f3f8", "#014636"]
)
```

### Dot Density Maps

Randomly distributes dots within the bounding box of mapped elements to represent density.

```python
# Apply a dot density map
density_data = {
    "region_1": 500, # 500 dots
    "region_2": {"value": 200}
}
info.apply_dot_density(
    data_map=density_data,
    dot_color="rgba(0, 0, 255, 0.8)",
    dots_per_value=1.0
)
```

### Proportional Symbols (Bubble Maps)

Creates markers scaled by value at the center of mapped SVG elements or at specific coordinates.

```python
# Apply proportional symbols
symbol_data = {
    "city_1": 100,
    "city_2": {"value": 250, "color": "#ff0000"} # Override color
}
info.apply_proportional_symbols(
    data_map=symbol_data,
    min_size=10.0,
    max_size=50.0
)
```

### Choropleth Maps

Applies a continuous color gradient across SVG elements based on a data mapping, including an optional legend.

```python
# Apply a choropleth map
choro_data = {"state_a": 150.5, "state_b": 42.0}
info.apply_choropleth(
    data_map=choro_data,
    min_color="#ffffff",
    max_color="#ff0000",
    show_legend=True
)
```

### Additional Thematic Maps

- **`apply_flow_map`**: Draws animated flow lines between elements (`origin` and `destination`).
- **`apply_spike_map`**: Renders 3D-like spikes representing values.
- **`apply_categorical_map`**: Maps discrete categories to specific colors with a generated legend.
- **`apply_value_by_alpha`**: Bivariate choropleth where base color maps to one variable and transparency (alpha) maps to a second variable.

## Dynamic UI Injection

The `Infographic` class provides powerful methods to programmatically augment SVGs with HTML/CSS components and new vector shapes relative to existing bounding boxes.

- **`add_card`**: Generates a perfectly scaled, native SVG card (KPI) relative to a target element.
- **`add_scalable_progress_bar`**: Generates an SVG progress bar anchored to a target element.
- **`add_overlay`**: Positions custom HTML over an SVG element's center coordinate.
- **`clip_html_to_shape`**: Clips raw HTML (like an iframe) perfectly to the exact shape of a target SVG element using a CSS mask.
- **`clip_image_to_shape`**: Clips an image to the exact shape of a target SVG element.

### Adding an SVG Shape Programmatically
```python
# Add a new vector shape to the SVG and make it interactive
info.add_shape("circle", {"id": "new_node", "cx": "100", "cy": "100", "r": "20", "fill": "blue"})
info.map("new_node", tooltip="I am a new node!")
```

## Compiling to HTML

Like other SIVO classes, you finalize your infographic by exporting it to a standalone HTML file.

```python
# Generate the interactive visualization
info.to_echarts_html(output_path="infographic.html")
```
