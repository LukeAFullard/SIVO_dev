"""
Cards Layout Dashboard Example
==============================

This example demonstrates how to use the modular `SivoDashboard` with CSS Grid
to create a responsive layout of independent dashboard components acting like "cards".
"""

import os
from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(title="Modular Cards Dashboard")

    # We define a CSS Grid layout.
    # The desktop view is a 2x3 grid, meaning 6 slots.
    # The mobile view stacks all 6 cards vertically.
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

    # Card 1: Main Map View
    # We use default_panel_position="none" so that interactivity updates the
    # dashboard's grid-based detail/metric panels rather than creating an overlay panel.
    map_view = Sivo.from_template('dashboards/four_quadrants', default_panel_position="none", layout_size="90%", lock_zoom_out=True)

    map_view.map(
        "quadrant_1",
        color="#3b82f6",
        hover_color="#2563eb",
        html="<h3>Sector Alpha</h3><p>Performance: Excellent</p>",
        callback_payload={"metric_a": "98%", "metric_b": "1.2s"}
    )
    map_view.map(
        "quadrant_4",
        color="#ef4444",
        hover_color="#dc2626",
        html="<h3>Sector Delta</h3><p>Performance: Critical</p>",
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
    small_map = Sivo.from_template('dashboards/sidebar_layout', default_panel_position="none", layout_size="90%", lock_zoom_out=True)
    small_map.map("metric_box_1", color="#f59e0b", hover_color="#d97706", html="<h3>Quick Link Action</h3><p>Clicked metric box 1.</p>")
    dashboard.add_sivo_block("quick_links", small_map, grid_area="card4")

    # Card 5: Another Sivo Block or HTML block (filling the grid)
    dashboard.add_html_block(
        "custom_html_1",
        "<div style='padding: 20px; background: white; border-radius: 8px; height: 100%; box-sizing: border-box; display: flex; align-items: center; justify-content: center; color: #64748b;'><h4>Card 5 Content</h4></div>",
        grid_area="card5"
    )

    # Card 6: Another HTML block
    dashboard.add_html_block(
        "custom_html_2",
        "<div style='padding: 20px; background: white; border-radius: 8px; height: 100%; box-sizing: border-box; display: flex; align-items: center; justify-content: center; color: #64748b;'><h4>Card 6 Content</h4></div>",
        grid_area="card6"
    )


    output_file = os.path.join(os.path.dirname(__file__), "output.html")
    print(f"Generating Cards Layout Dashboard to '{output_file}'...")
    dashboard.to_html(output_file)
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
