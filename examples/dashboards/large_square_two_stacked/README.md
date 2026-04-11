# Large Square with Two Vertically Stacked Squares Dashboard

This example demonstrates how to build a responsive, multi-block SIVO dashboard layout. It specifically showcases a custom CSS grid implementation where the left column spans vertically to display a single "large square" (a SIVO canvas component), while the right column contains two smaller, vertically stacked panels.

## What is being tested/shown

1. **Custom Grid Layout (`SivoDashboard`):**
   We configure a flexible, responsive dashboard interface by initializing a `SivoDashboard`. Instead of relying on a monolithic SVG, we inject separate visual blocks and UI panels into predefined grid areas using `dashboard.set_grid_layout()`. The layout adjusts dynamically for desktop and mobile views.

2. **Panel Positioning (`default_panel_position`):**
   By default, the internal SIVO side panel is no longer enabled (`default_panel_position="none"`). This example explicitly declares `default_panel_position="none"` when instantiating `Sivo.from_template()`, since the UI details and metrics are offloaded to standalone dashboard blocks rather than the internal canvas panel.

3. **Inter-Component Reactivity:**
   The dashboard maps `callback_payload` data within the SIVO `large_map` instance. When a quadrant on the map is clicked, the `server`, `uptime`, and `load` metrics are emitted and automatically captured by the adjacent `add_metrics_panel`, creating a synchronized, interactive dashboard experience.

## Relevant Code Snippets

**1. Defining the Grid Layout**
```python
dashboard.set_grid_layout(
    desktop='''
"large right1"
"large right2"
    ''',
    mobile='''
"large"
"right1"
"right2"
    '''
)
```
*Here, the desktop grid assigns the `large` area to span both rows on the left side, with `right1` and `right2` stacked on the right. On mobile, all blocks are stacked vertically.*

**2. SIVO Block Initialization & Explicit Panel Settings**
```python
large_map = Sivo.from_template(
    'dashboards/four_quadrants',
    default_panel_position="none", # Explicitly declaring no internal panel
    layout_size="90%",
    lock_zoom_out=True
)
```

**3. Binding Payloads for Metrics Panels**
```python
large_map.map(
    "quadrant_1",
    color="#3b82f6",
    hover_color="#2563eb",
    tooltip="<h3>Primary Server</h3><p>Status: Online</p>",
    callback_payload={"server": "Primary", "uptime": "99.99%", "load": "45%"}
)
```
*The `callback_payload` maps arbitrary data points to the interactive element. This data is rendered inside the dashboard's metrics panel (below) when the user clicks the quadrant.*

**4. Registering the Dashboard Panels**
```python
# The main SIVO instance
dashboard.add_sivo_block("primary_view", large_map, grid_area="large")

# An external details panel that listens to the SIVO block
dashboard.add_details_panel(
    "server_details",
    title="Server Information",
    placeholder="Select a server node to view its detailed information.",
    grid_area="right1"
)

# An external metrics panel that displays callback payloads
dashboard.add_metrics_panel(
    "server_metrics",
    title="Performance Metrics",
    metrics=["server", "uptime", "load"],
    grid_area="right2"
)
```
