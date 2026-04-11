# Advanced Choropleth Dashboard Example

This example demonstrates how to build an advanced dashboard using `SivoDashboard` and `Sivo`. The dashboard features a responsive multi-block layout integrating an interactive, dynamic data-driven map (Choropleth) alongside standard "No-Code" interactive metrics and detail panels.

## What is being tested/demonstrated
* **Multi-block Grid Layout (`SivoDashboard`)**: Arranging an interactive SIVO block with external "Details" and "Metrics" panels side-by-side using CSS grid.
* **Choropleth Mapping (`apply_choropleth`)**: Automatically rendering a color gradient heatmap based on provided numerical data for specific SVG paths (states). SIVO computes the colors automatically.
* **Path Animations**: Applying a pulsing CSS animation natively to a targeted vector path to highlight performance (`animation="pulse"`).
* **Callbacks and Payload Binding**: Using `.map(..., callback_event="select", callback_payload={...})` to trigger no-code interaction panels built within the `SivoDashboard`. When a map region is clicked, its payload dynamically populates the adjacent details and metrics panels.
* **Default Panel Position**: `Sivo.from_string` operates with a default `panel_position` set to `'none'`. Since we are using an external Details Panel via the Dashboard interface (`add_details_panel`), this default acts correctly by preventing the internal SIVO side panel from opening and obscuring the map. The custom HTML provided in the SIVO map bindings updates the external Details panel directly.

## Relevant Code Snippets
### Creating the Choropleth:
```python
sales_data = {
    "state_ca": 1250000,
    "state_tx": 850000,
    "state_ny": 2100000
}
sivo_map.apply_choropleth(sales_data, min_color="#eff6ff", max_color="#1e3a8a")
```

### Adding Callbacks and Payload Data:
```python
sivo_map.map(
    "state_ny",
    html="<h4>New York Operations</h4><p>Record-breaking sales driven by new B2B partnerships.</p><img src='https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=400&q=80' style='width:100%; border-radius:8px;'/>",
    callback_event="select",
    callback_payload={"revenue": "$2.1M", "growth": "+25%", "status": "Exceeding Targets"}
)
```

### Dashboard Assembly:
```python
dashboard = SivoDashboard(title="Q3 Executive Insights")
dashboard.add_sivo_block("heat_map", sivo_map)
dashboard.add_metrics_panel("performance_metrics", title="Region Performance", metrics=["revenue", "growth", "status"])
dashboard.add_details_panel("region_insights", title="Executive Summary", placeholder="Click a state to view local operational notes.")
```

## Running the Example
To generate the output HTML dashboard file:
```bash
PYTHONPATH=src python3 examples/dashboards/advanced_choropleth/main.py
```
This produces `output.html` in the current directory. Open it in any modern web browser to interact with the interactive map and responsive panels.
