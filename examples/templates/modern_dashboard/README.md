# Modern Dashboard (ESG Theme)

This example illustrates building a comprehensive ESG (Environmental, Social, and Governance) dashboard using a modern layout template and integrating a complex dot-density map visualization.

## Key Features Demonstrated

1.  **SVG Template Loading**: Uses the `dashboard_template.svg` base.
2.  **Thematic Integration**: Applies a `light` theme with a `snow` ambient effect, fitting for a sustainability-focused dashboard.
3.  **Data Overlays**:
    *   Uses `app.add_scalable_text` extensively for metrics.
    *   Embeds a custom **Stacked Bar** HTML chart (`metric_2`).
    *   Adds a native SIVO **Progress Bar** (`metric_3`) using `app.add_scalable_progress_bar`.
4.  **Complex Nested Map (Dot Density/Scatter)**:
    *   Initializes an empty base map using `app.map_nested_map_chart` on the `main_chart_area`.
    *   Layers a complex ECharts `scatter` and `effectScatter` series over the base map by subsequently calling `app.map("main_chart_area", echarts_option={...})`. This technique creates a rich dot-density map showing global facility emissions.
5.  **Absolute Positioning of Overlays**: Demonstrates placing custom HTML overlays (a Donut chart and a Line chart) directly onto the infographic via coordinate definition (`app.infographic.overlays`), rather than pinning them to a specific SVG element ID.

## Example Code Highlights

**Layering Data on a Nested Map:**

```python
# Initialize empty map
app.map_nested_map_chart(element_id="main_chart_area", data=[], ...)

# Layer custom ECharts options (scatter series)
app.map("main_chart_area", echarts_option={
    "series": [{
        "name": "Emissions",
        "type": "scatter",
        "coordinateSystem": "geo",
        "data": cities,
        # ... styling ...
    },
    # ... additional effectScatter series ...
    ]
})
```

**Direct Overlay Coordinate Positioning:**

```python
app.infographic.overlays["anchor_sidebar_top"] = {
    "html": donut_html,
    "coord": [810 + 350/2, 340 + 200/2],
    "bbox": [810, 340, 810+350, 340+200],
    "offset": [0, 0],
    "scale_with_zoom": False
}
```
