# Cards Layout Example

This example demonstrates how to build a modular dashboard using the modern `SivoDashboard` CSS Grid Layout, replacing the deprecated pre-configured HTML templates.

## What is being shown?

- **CSS Grid Builder Layout:** We construct a fully custom 2x3 grid structure on desktop (`card1` to `card6`) and stack the elements vertically on mobile.
- **Multiple SIVO Instances:** The grid contains two distinct SIVO visual interactables (`geographic_overview` and `quick_links`) that run independently within the dashboard layout.
- **Interconnected Panels:** SIVO map interactions are piped directly into standard dashboard components. `default_panel_position="none"` is passed so SIVO native overlays do not obscure the grid elements.
  - The **Details Panel** dynamically reflects the `html` content supplied to mapped interactive regions on the canvas.
  - The **Metrics Panel** dynamically parses and displays values from the `callback_payload` dictionary tied to interactive regions.
- **Raw HTML Blocks:** The dashboard also populates grid areas with arbitrary stringified HTML.

## Relevant Code

```python
# Create dashboard and setup the CSS Grid explicitly mapping 'grid_area' names
dashboard = SivoDashboard(title="Modular Cards Dashboard")
dashboard.set_grid_layout(
    desktop='''
        "card1 card2 card3"
        "card4 card5 card6"
    ''',
    mobile='''
        "card1"
        "card2"
        # ... stacked ...
    '''
)

# SIVO interactable with panel set to 'none' since external grid panels handle display
map_view = Sivo.from_template('dashboards/four_quadrants', default_panel_position="none")
map_view.map(
    "quadrant_1",
    html="<h3>Sector Alpha</h3>",
    callback_payload={"metric_a": "98%"}
)

# Attach SIVO blocks, details panel, and metrics panels to grid areas
dashboard.add_sivo_block("geographic_overview", map_view, grid_area="card1")
dashboard.add_metrics_panel("key_metrics", title="KPIs", metrics=["metric_a"], grid_area="card2")
dashboard.add_details_panel("detailed_analysis", title="Analysis", grid_area="card3")
```
