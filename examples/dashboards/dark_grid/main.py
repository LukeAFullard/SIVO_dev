"""
Dark Grid Dashboard Example
===========================

This example demonstrates how to build a high-contrast, dark-mode dashboard using the `SivoDashboard`.
It creates a sleek, modern UI suitable for Operations Centers, live system monitoring, or technical readouts, using
ECharts' dark theme support and a custom CSS Grid.
"""

from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    # 1. Initialize empty dashboard
    dashboard = SivoDashboard(title="Global Server Status", columns=4)

    # 2. Define the responsive grid layout
    dashboard.set_grid_layout(
        desktop='''
    "header header header header"
    "main main side side"
    "bottom1 bottom2 side side"
        ''',
        mobile='''
    "header"
    "main"
    "side"
    "bottom1"
    "bottom2"
        '''
    )

    # 3. Add an HTML Header
    header_html = '''
    <div style="padding: 10px;">
        <h3 style="margin: 0; color: #f8fafc; font-size: 1.25rem;">Live Feed</h3>
        <p style="color: #94a3b8; margin-top: 5px; font-size: 0.875rem;">System latency updates every 5s</p>
    </div>
    '''
    dashboard.add_html_block("live_feed", header_html, grid_area="header")

    # 4. Create a primary Global Map
    world_map = Sivo.from_template('dashboards/sidebar_layout', layout_size="90%", lock_zoom_out=True, theme="dark", default_panel_position="none")

    # Add dummy data to some nodes
    world_map.map(
        "main_panel",
        color="#38bdf8",
        hover_color="#0284c7",
        tooltip="<h3>US-East Datacenter</h3><p>Status: Healthy</p>",
        callback_payload={"cpu_load": "42%", "active_connections": "12,450", "bandwidth": "850 Mbps"}
    )
    world_map.map(
        "metric_box_1",
        color="#10b981",
        hover_color="#059669",
        tooltip="<h3>EU-Central Datacenter</h3><p>Status: Excellent</p>",
        callback_payload={"cpu_load": "28%", "active_connections": "8,200", "bandwidth": "600 Mbps"}
    )
    world_map.map(
        "metric_box_2",
        color="#f59e0b",
        hover_color="#d97706",
        tooltip="<h3>AP-Northeast Datacenter</h3><p>Status: High Load</p>",
        callback_payload={"cpu_load": "85%", "active_connections": "18,900", "bandwidth": "1.2 Gbps"}
    )

    dashboard.add_sivo_block("global_network", world_map, grid_area="main")

    # 5. Add a Metrics Panel on the right
    dashboard.add_metrics_panel(
        "server_metrics",
        title="Server Telemetry",
        metrics=["cpu_load", "active_connections", "bandwidth"],
        grid_area="side"
    )

    # 6. Add Details Panel
    dashboard.add_details_panel(
        "datacenter_logs",
        title="Node Logs",
        placeholder="Select a region on the map to view live logs.",
        grid_area="bottom1"
    )

    # 7. Generate the HTML Dashboard
    print("Generating Dark Grid Dashboard to 'output.html'...")
    dashboard.to_html("output.html")
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
