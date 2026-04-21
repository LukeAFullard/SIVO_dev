# Bento Grid Dashboard

This example demonstrates the creation of a modern "Bento Grid" dashboard, highlighting different types of embedded visualizations within the SIVO framework.

## Key Features Demonstrated

1.  **SVG Template Loading**: Loads the `bento_grid_dashboard_2026.svg` template.
2.  **Dark Theme & Styling**: Utilizes the `dark` theme and `stars` ambient effect. It also manually overrides the fill and border colors of specific card elements (`card-main`, `rect-users`, etc.) using `app.map` to ensure visual consistency.
3.  **Nested Map Chart**: Maps a full ECharts geographical map visualization onto the main card area (`card-main`) using `app.map_nested_map_chart`. This displays active maritime cargo routes.
4.  **Scalable Text**: Overlays responsive text on the grid cards using `app.add_scalable_text`.
5.  **Custom HTML Overlays**: Embeds diverse visualizations using HTML/SVG strings:
    *   **Radar/Spider Chart** on `rect-users`.
    *   **Animated Glowing Alert** on `rect-conversion`.
    *   **Area Trend Chart** on `card-bounce`.
    *   **Gauge Chart** on `card-satisfaction`.

## Example Code Highlights

**Mapping a Nested ECharts Map:**

```python
app.map_nested_map_chart(
    element_id="card-main",
    title="Active Maritime Cargo Routes & Congestion",
    map_name="world",
    map_data="world",
    data=[
        {"name": "United States", "value": 1500},
        # ... other countries ...
    ],
    # ... visual configuration ...
)
```

**Animated HTML Overlay:**

```python
alert_html = """
<div style='...'>
    <div style='... animation: pulse 2s infinite;'>
        <span>!</span>
    </div>
    <!-- CSS Keyframes included within the string -->
    <style>@keyframes pulse { ... }</style>
</div>
"""
app.add_overlay("rect-conversion", alert_html)
```
