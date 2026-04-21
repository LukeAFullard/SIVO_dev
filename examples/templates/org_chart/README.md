# Organizational Chart / Architecture Hierarchy

This example demonstrates how to use the pyramid hierarchy template to visualize an Enterprise Data Fabric Architecture, including layered elements and interactive performance metrics.

## Key Features Demonstrated

1.  **Pyramid Hierarchy Template**: Uses `pyramid_hierarchy_template.svg` to show distinct layers of architecture.
2.  **Layered Annotations**: Uses `app.add_scalable_text` to label each tier (`poly-tier-1` through `poly-tier-4`) and `app.fill_template_zone` for the main title.
3.  **Embedded Sparklines & Bar Charts**:
    *   Tier 2 features an embedded SVG **Sparkline** representing the compute engine load.
    *   Tier 3 features another SVG **Sparkline** representing storage metrics.
    *   Tier 4 includes an embedded SVG **Bar Chart** representing ingestion pipeline activity.
4.  **Interactive Tooltips & Hover Effects**: Maps interaction to each architectural tier using `app.map`. Each tier has a unique `hover_color` and a descriptive HTML `tooltip` providing more context.
5.  **Interactive Side Panel Chart**: The main interaction maps an ECharts bar chart (`app.map_bar_chart`) to the `info-panel-data` element, configured to open in an overlay (`panel_position="overlay"`). This chart visualizes system throughput and latency metrics.

## Example Code Highlights

**Layer Tooltips & Hover Styling:**

```python
app.map("poly-tier-1",
        hover_color="#fca5a5",
        tooltip="<b>Application Layer</b><br>Provides APIs and visualization tools...")
```

**Side Panel Interactive Bar Chart:**

```python
app.map_bar_chart(
    panel_position="overlay",
    element_id="info-panel-data",
    categories=["Ingest", "Storage", "Compute", "App"],
    data=[
        {"name": "Throughput", "type": "bar", "data": [12.5, 8.2, 45.0, 2.1], "itemStyle": {"color": "#3b82f6"}},
        {"name": "Latency", "type": "bar", "data": [45, 120, 85, 200], "itemStyle": {"color": "#f43f5e"}}
    ],
    # ...
)
```
