# Minimalist Journey Flow

This example demonstrates how to use the SIVO framework to create a minimalist, 5-step journey flow infographic with interactive data visualizations.

## Key Features Demonstrated

1.  **SVG Template Loading**: Uses `Sivo.from_svg` to load the `minimalist_journey_flow_2026.svg` template.
2.  **Custom Styling & Effects**: Enables `stars` ambient effect and uses a `light` theme to enhance visual appeal.
3.  **Template Filling**: Populates predefined text zones (e.g., `header-title-placeholder`, `node-1-step-placeholder`) with custom text, styling, and alignment using `app.fill_template_zone`.
4.  **Custom HTML Overlays**: Directly embeds custom HTML/SVG code to create visually distinct charts overlaying specific nodes:
    *   **Funnel Chart** on Node 1 (`node-1-card`)
    *   **Gauge Chart** on Node 2 (`node-2-card`)
    *   **Progress Bar** on Node 3 (`node-3-card`)
5.  **Interactive Tooltips & Effects**: Maps interactions directly to elements using `app.map`. This includes custom tooltips, hover colors, and a `confetti` effect when interacting with Node 3.
6.  **Interactive Side Panel Chart**: Maps a pie chart to Node 5 (`node-5-card`) using `app.map_pie_chart`. Clicking this node triggers an overlay panel displaying the "Account Status" chart.

## Example Code Highlights

**HTML Overlay Integration:**

```python
node_1_funnel = """
<div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 2cqh; gap: 2px; container-type: size;">
    <div style="width: 15cqw; height: 3cqh; background-color: #93c5fd; border-radius: 2px;"></div>
    <!-- ... more funnel segments ... -->
</div>
"""
app.add_overlay("node-1-card", node_1_funnel)
```

**Interactive Side Panel Chart Mapping:**

```python
app.map_pie_chart(
    element_id="node-5-card",
    panel_position="overlay",
    title="Account Status",
    data=[
        {"name": "Renewed", "value": 85},
        {"name": "At Risk", "value": 10},
        {"name": "Churn", "value": 5}
    ],
    # ... additional options ...
)
```
