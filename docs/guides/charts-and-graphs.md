---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# H-13: Charts and Graphs Guide

SIVO provides seamless integration with Apache ECharts, allowing you to embed a wide variety of native, interactive charts directly into your SVG maps and dashboards. Instead of drawing static shapes, you can map data to an SVG region to render a dynamic chart.

## 1. Introduction to ECharts Integration

The SIVO Python API provides specialized `map_*_chart` methods to make embedding charts straightforward. When you call one of these methods on an SVG element ID, SIVO replaces that SVG element with an ECharts instance configured with your data.

This approach gives you the full power of ECharts—tooltips, legends, axes, and interactive features—while preserving the precise layout defined by your SVG template.

## 2. Basic Charts

SIVO supports the most common chart types out of the box. Below are examples of how to map them to your SVG elements.

### Bar Chart

Use `map_bar_chart` to compare quantities across categories.

```python
from sivo import Sivo

sivo_app = Sivo.from_svg("my_template.svg")

sivo_app.map_bar_chart(
    element_id="chart_region_1",
    title="Quarterly Revenue",
    categories=["Q1", "Q2", "Q3", "Q4"],
    data=[12000, 15000, 14000, 18000],
    color="#3b82f6",
    tooltip="Revenue: ${c}"
)
```

### Line Chart

Use `map_line_chart` to show trends over time.

```python
sivo_app.map_line_chart(
    element_id="chart_region_2",
    title="Website Traffic",
    categories=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    data=[150, 230, 224, 218, 135, 147, 260],
    color="#10b981",
    smooth=True
)
```

### Pie Chart

Use `map_pie_chart` to show proportions of a whole.

```python
pie_data = [
    {"value": 1048, "name": "Search Engine"},
    {"value": 735, "name": "Direct"},
    {"value": 580, "name": "Email"},
    {"value": 484, "name": "Union Ads"},
    {"value": 300, "name": "Video Ads"}
]

sivo_app.map_pie_chart(
    element_id="chart_region_3",
    title="Traffic Sources",
    data=pie_data,
    color=["#5470c6", "#91cc75", "#fac858", "#ee6666", "#73c0de"]
)
```

### Scatter Chart

Use `map_scatter_chart` to visualize the relationship between two numerical variables. Data is typically a list of `[x, y]` pairs.

```python
scatter_data = [
    [10.0, 8.04], [8.0, 6.95], [13.0, 7.58], [9.0, 8.81], [11.0, 8.33],
    [14.0, 9.96], [6.0, 7.24], [4.0, 4.26], [12.0, 10.84], [7.0, 4.82]
]

sivo_app.map_scatter_chart(
    element_id="chart_region_4",
    title="Height vs Weight",
    data=scatter_data,
    color="#8b5cf6"
)
```

## 3. Advanced Charts

For more complex data visualization needs, SIVO exposes several advanced ECharts types.

### Radar Chart

Great for comparing multiple quantitative variables.

```python
indicators = [
    {"name": "Sales", "max": 6500},
    {"name": "Administration", "max": 16000},
    {"name": "Information Techology", "max": 30000},
    {"name": "Customer Support", "max": 38000},
    {"name": "Development", "max": 52000},
    {"name": "Marketing", "max": 25000}
]

radar_data = [
    {"value": [4200, 3000, 20000, 35000, 50000, 18000], "name": "Allocated Budget"},
    {"value": [5000, 14000, 28000, 26000, 42000, 21000], "name": "Actual Spending"}
]

sivo_app.map_radar_chart(
    element_id="chart_region_5",
    title="Budget vs Spending",
    indicators=indicators,
    data=radar_data
)
```

### Sunburst Chart

Ideal for visualizing hierarchical data spanning outward from a root node.

```python
sunburst_data = [
    {
        "name": "Grandpa",
        "children": [
            {
                "name": "Uncle Leo",
                "value": 15,
                "children": [{"name": "Cousin Jack", "value": 2}]
            },
            {
                "name": "Aunt Mary",
                "value": 10
            }
        ]
    }
]

sivo_app.map_sunburst_chart(
    element_id="chart_region_6",
    title="Family Tree",
    data=sunburst_data
)
```

### Sankey Chart

Used to visualize the flow of data or resources between nodes.

```python
nodes = [{"name": "NodeA"}, {"name": "NodeB"}, {"name": "NodeC"}]
links = [
    {"source": "NodeA", "target": "NodeB", "value": 10},
    {"source": "NodeB", "target": "NodeC", "value": 5}
]

sivo_app.map_sankey_chart(
    element_id="chart_region_7",
    title="Resource Flow",
    nodes=nodes,
    links=links
)
```

### Funnel Chart

Useful for showing stages in a process, like a sales pipeline.

```python
funnel_data = [
    {"value": 60, "name": "Visit"},
    {"value": 40, "name": "Inquiry"},
    {"value": 20, "name": "Order"},
    {"value": 80, "name": "Click"},
    {"value": 100, "name": "Show"}
]

sivo_app.map_funnel_chart(
    element_id="chart_region_8",
    title="Sales Pipeline",
    data=funnel_data
)
```

### Heatmap Chart

Great for displaying data distributions or correlations over a grid (e.g., hours of a day vs days of a week).

```python
heatmap_data = [
    # [x_index, y_index, value]
    [0, 0, 5], [0, 1, 1], [0, 2, 0],
    [1, 0, 3], [1, 1, 2], [1, 2, 6]
]
x_cats = ["12a", "1a"]
y_cats = ["Sat", "Sun", "Mon"]

sivo_app.map_heatmap_chart(
    element_id="chart_region_9",
    title="Punch Card",
    data=heatmap_data,
    x_categories=x_cats,
    y_categories=y_cats
)
```

### Other Available Charts
SIVO also supports mapping the following charts:
- Gauge (`map_gauge_chart`)
- Treemap (`map_treemap_chart`)
- Polar Bar & Line (`map_polar_bar_chart`, `map_polar_line_chart`)
- Liquid Fill (`map_liquidfill_chart`)
- Boxplot (`map_boxplot_chart`)
- Candlestick (`map_candlestick_chart`)
- Word Cloud (`map_word_cloud_chart`)
- Calendar Heatmap (`map_calendar_heatmap_chart`)
- Graph/Network (`map_graph_chart`)
- Parallel Coordinates (`map_parallel_chart`)
- Theme River (`map_theme_river_chart`)
- Effect Scatter (`map_effect_scatter_chart`)
- Lines/Routes (`map_lines_chart`)
- Tree/Dendrogram (`map_tree_chart`)

## 4. Customizing Charts

Most `map_*_chart` methods share a set of optional parameters to customize the appearance of the chart.

- `title`: The title displayed on the chart.
- `title_color`: The color of the title text (e.g., `"#333"`).
- `title_size`: The font size of the title (e.g., `18`).
- `color`: The primary color or list of colors used for the chart series.
- `axis_color`: The color of the axes labels and lines.
- `axis_size`: The font size of the axes labels.
- `tooltip_bg_color`: The background color of the tooltip.
- `grid_margin`: A list of integers `[top, right, bottom, left]` to adjust the chart's margins within the SVG bounding box.
- `universal_transition`: Enables seamless morphing animations when data or chart types change dynamically (defaults to `True`).
- `extra_options`: A dictionary of raw ECharts configuration options to deeply customize or override SIVO's default settings. This is useful for passing specific ECharts properties not covered by the Python API.

```python
sivo_app.map_bar_chart(
    element_id="my_bar",
    title="Customized Bar",
    categories=["A", "B"],
    data=[10, 20],
    title_color="#ff0000",
    grid_margin=[40, 20, 40, 20],
    extra_options={"legend": {"show": True, "bottom": 0}}
)
```

## 5. Interactive Data Zooming

For charts with large datasets (especially line, bar, and scatter charts), you can enable an interactive zooming and panning slider by passing `datazoom=True`.

```python
sivo_app.map_line_chart(
    element_id="large_dataset_chart",
    title="Yearly Data",
    categories=large_category_list,
    data=large_data_list,
    datazoom=True  # Enables the slider at the bottom of the chart
)
```
When `datazoom=True` is provided, ECharts automatically appends a zoom slider control to the chart, allowing users to focus on specific segments of the data.
