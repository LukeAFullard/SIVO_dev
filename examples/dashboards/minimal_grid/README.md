# Minimal Grid Dashboard Example

This example demonstrates how to build a responsive, custom dashboard using `SivoDashboard`.
It focuses on a high-contrast, cleanly structured grid layout that is ideal for operations, data centers, and technical monitoring.

## What is being shown
- **CSS Grid Layout:** Defines a responsive grid layout using `dashboard.set_grid_layout(desktop='...', mobile='...')`. The layout creates specific named areas such as `metrics`, `map`, and `details`.
- **Pre-built Dashboard Panels:** Uses `add_metrics_panel()` to automatically extract and display active data payloads on click, and `add_details_panel()` to display rich HTML content tied to SIVO elements.
- **SIVO Block Integration:** Binds a standalone Sivo map instance (`cluster_map`) generated from an SVG template (`dashboards/four_quadrants`) into the grid area `"map"` using `dashboard.add_sivo_block()`.
- **Payload Mapping:** Demonstrates how to map interactive data elements within the SIVO map. By mapping the `callback_payload` (e.g. `{"cpu_load": "45%", ...}`) and the `html` properties for each element, clicking an element automatically triggers the respective `metrics` and `details` panels in the dashboard layout.

## Code Highlights
The following block demonstrates how to define the dashboard grid areas for both desktop and mobile using the internal layout builder:

```python
    dashboard.set_grid_layout(
        desktop='''
    "metrics metrics metrics metrics"
    "map map map details"
        ''',
        mobile='''
    "metrics"
    "map"
    "details"
        '''
    )
```

The data payload and click content are added to individual mapped segments of the SVG using both `html` and `callback_payload` parameters:
```python
    cluster_map.map(
        "quadrant_1",
        color="#10b981",
        hover_color="#059669",
        tooltip="<h3>Cluster Alpha</h3><p>Status: Healthy<br>Nodes: 120</p>",
        html="<h3>Cluster Alpha</h3><p>Status: Healthy<br>Nodes: 120</p>",
        callback_payload={"cpu_load": "45%", "memory_usage": "62%", "network_io": "1.2 GB/s", "active_connections": "4,502"}
    )
```

The panels are attached using their corresponding `grid_area` settings:
```python
    # Attaches the payload metrics
    dashboard.add_metrics_panel(
        "system_metrics",
        title="Live Telemetry",
        metrics=["cpu_load", "memory_usage", "network_io", "active_connections"],
        grid_area="metrics"
    )

    # Attaches the HTML details panel
    dashboard.add_details_panel(
        "node_details",
        title="Cluster Logs",
        placeholder="Select a cluster quadrant to view active logs and status.",
        grid_area="details"
    )
```

## Running the example

Run the script directly using Python:

```bash
python main.py
```

This will generate an `output.html` file in this directory. Open it in a web browser to see the interactive dashboard.