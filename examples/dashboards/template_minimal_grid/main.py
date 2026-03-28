"""
Minimal Grid Dashboard Example
==============================

This example demonstrates how to use the `minimal_grid.html` template
to create a highly legible, high-contrast dashboard suitable for data-heavy applications.
"""

from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(title="System Operations", columns=4)
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

    # Metrics Panel
    dashboard.add_metrics_panel(
        "system_metrics",
        title="Live Telemetry",
        metrics=["cpu_load", "memory_usage", "network_io", "active_connections"],
        grid_area="metrics"
    )

    # Primary Map
    cluster_map = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)

    cluster_map.map(
        "quadrant_1",
        color="#10b981",
        hover_color="#059669",
        tooltip="<h3>Cluster Alpha</h3><p>Status: Healthy<br>Nodes: 120</p>",
        callback_payload={"cpu_load": "45%", "memory_usage": "62%", "network_io": "1.2 GB/s", "active_connections": "4,502"}
    )
    cluster_map.map(
        "quadrant_2",
        color="#f59e0b",
        hover_color="#d97706",
        tooltip="<h3>Cluster Beta</h3><p>Status: Warning<br>Nodes: 95</p>",
        callback_payload={"cpu_load": "88%", "memory_usage": "75%", "network_io": "2.1 GB/s", "active_connections": "6,100"}
    )
    cluster_map.map(
        "quadrant_3",
        color="#10b981",
        hover_color="#059669",
        tooltip="<h3>Cluster Gamma</h3><p>Status: Healthy<br>Nodes: 150</p>",
        callback_payload={"cpu_load": "32%", "memory_usage": "41%", "network_io": "0.8 GB/s", "active_connections": "2,150"}
    )
    cluster_map.map(
        "quadrant_4",
        color="#ef4444",
        hover_color="#dc2626",
        tooltip="<h3>Cluster Delta</h3><p>Status: Critical<br>Nodes: 5</p>",
        callback_payload={"cpu_load": "99%", "memory_usage": "98%", "network_io": "0.1 GB/s", "active_connections": "52"}
    )

    dashboard.add_sivo_block("cluster_topology", cluster_map, grid_area="map")

    # Details Panel
    dashboard.add_details_panel(
        "node_details",
        title="Cluster Logs",
        placeholder="Select a cluster quadrant to view active logs and status.",
        grid_area="details"
    )


    print("Generating Minimal Grid Dashboard to 'output.html'...")
    dashboard.to_html("output.html")
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
