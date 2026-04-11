"""
Large Square with Two Vertically Stacked Squares
================================================

This example demonstrates how to build a responsive dashboard with a custom grid layout.
The left column contains a single large square, and the right column contains two vertically
stacked components (e.g., details and metrics panels).
"""

import os
from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(title="System Overview", columns=2)

    # Define the responsive grid layout
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

    # 1. The Large Square (Left)
    # We set default_panel_position="none" because we are using a custom dashboard layout
    # and don't need SIVO's internal side panel.
    large_map = Sivo.from_template(
        'dashboards/four_quadrants',
        default_panel_position="none",
        layout_size="90%",
        lock_zoom_out=True
    )

    large_map.map(
        "quadrant_1",
        color="#3b82f6",
        hover_color="#2563eb",
        tooltip="<h3>Primary Server</h3><p>Status: Online</p>",
        callback_payload={"server": "Primary", "uptime": "99.99%", "load": "45%"}
    )
    large_map.map(
        "quadrant_2",
        color="#10b981",
        hover_color="#059669",
        tooltip="<h3>Secondary Server</h3><p>Status: Online</p>",
        callback_payload={"server": "Secondary", "uptime": "99.95%", "load": "32%"}
    )
    large_map.map(
        "quadrant_3",
        color="#f59e0b",
        hover_color="#d97706",
        tooltip="<h3>Database</h3><p>Status: Warning</p>",
        callback_payload={"server": "Database", "uptime": "99.90%", "load": "85%"}
    )

    dashboard.add_sivo_block("primary_view", large_map, grid_area="large")

    # 2. Top Right Stacked Component (Details Panel)
    dashboard.add_details_panel(
        "server_details",
        title="Server Information",
        placeholder="Select a server node to view its detailed information.",
        grid_area="right1"
    )

    # 3. Bottom Right Stacked Component (Metrics Panel)
    dashboard.add_metrics_panel(
        "server_metrics",
        title="Performance Metrics",
        metrics=["server", "uptime", "load"],
        grid_area="right2"
    )

    # Export
    output_file = os.path.join(os.path.dirname(__file__), "output.html")
    print(f"Generating Dashboard to '{output_file}'...")
    dashboard.to_html(output_file)
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
