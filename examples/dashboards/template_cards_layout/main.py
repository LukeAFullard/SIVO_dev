"""
Cards Layout Dashboard Example
==============================

This example demonstrates how to use the `cards_layout.html` template
to create a responsive grid of independent dashboard components.
"""

from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(title="Modular Cards Dashboard")
    dashboard.set_grid_layout(
        desktop='''
    "card1 card2 card3"
"card4 card5 card6"
        ''',
        mobile='''
    "card1"
"card2"
"card3"
"card4"
"card5"
"card6"
        '''
    )

    # Card 1: Map View
    map_view = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)

    map_view.map(
        "quadrant_1",
        color="#3b82f6",
        hover_color="#2563eb",
        tooltip="<h3>Sector Alpha</h3><p>Performance: Excellent</p>",
        callback_payload={"metric_a": "98%", "metric_b": "1.2s"}
    )
    map_view.map(
        "quadrant_4",
        color="#ef4444",
        hover_color="#dc2626",
        tooltip="<h3>Sector Delta</h3><p>Performance: Critical</p>",
        callback_payload={"metric_a": "45%", "metric_b": "8.5s"}
    )

    dashboard.add_sivo_block("geographic_overview", map_view, grid_area="card1")

    # Card 2: Metrics Panel
    dashboard.add_metrics_panel(
        "key_metrics",
        title="Key Performance Indicators",
        metrics=["metric_a", "metric_b"],
        grid_area="card2"
    )

    # Card 3: Details Panel
    dashboard.add_details_panel(
        "detailed_analysis",
        title="Sector Analysis",
        placeholder="Select a sector on the map to view detailed analysis.",
        grid_area="card3"
    )

    # Card 4: Secondary Map
    small_map = Sivo.from_template('dashboards/sidebar_layout', layout_size="90%", lock_zoom_out=True)
    small_map.map("metric_box_1", color="#f59e0b", hover_color="#d97706", tooltip="Quick Link")
    dashboard.add_sivo_block("quick_links", small_map, grid_area="card4")


    print("Generating Cards Layout Dashboard to 'output.html'...")
    dashboard.to_html("output.html")
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
