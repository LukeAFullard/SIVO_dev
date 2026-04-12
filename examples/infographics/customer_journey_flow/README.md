# Customer Journey Flow Infographic

This example demonstrates how to build an interactive, stylized flowchart from a pre-designed template (`minimalist_journey_flow_2026.svg`). It highlights how SIVO can be used to construct process infographics and bind complex data visualization directly to parts of the graphic.

## What is being tested/shown:
1. **Template Parsing & Styling**: Loading an existing structural template (`Sivo.from_svg(...)`) with specific style overrides (`app.apply_template_style("minimalist")`).
2. **Zone Filling (`fill_template_zone`)**: Programmatically injecting text strings into predefined placeholder zones of the template (e.g., headers, nodes, and descriptions) and adjusting their typographic styles (font size, weight, color).
3. **Interactive Chart Mapping (`map_funnel_chart`)**: Taking an external data structure (`funnel_data`) and binding it to a visual element (`node-3-conversion`) as an ECharts funnel chart.
4. **Side Panel Triggering (`panel_position="right"`)**: When the user interacts with the conversion node, the funnel chart opens in a right-hand side panel, avoiding visual clutter on the main diagram until interacted with.

## Key Code Snippets:

**1. Filling Text Nodes:**
```python
# Node 1
app.fill_template_zone("node-1-step-placeholder", "1. Awareness", font_size=20, font_weight="600", color="#1e293b", align="left")
```

**2. Mapping Interactive Funnel Chart:**
```python
app.map_funnel_chart(
    element_id="node-3-conversion",
    title="Overall Funnel Drop-off",
    data=funnel_data,
    color=["#e2e8f0", "#94a3b8", "#3b82f6", "#10b981", "#ec4899"],
    tooltip="Click to view step-by-step conversion funnel drop-off rates.",
    panel_position="right"  # Ensures the funnel is rendered in a side panel
)
```

## Running the Example
To generate the final HTML output:
```bash
PYTHONPATH=src python3 examples/infographics/customer_journey_flow/main.py
```
This will produce a `customer_journey.html` file in the same directory, which can be opened in any modern web browser.
