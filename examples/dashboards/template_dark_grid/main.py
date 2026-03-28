"""
Dark Grid Dashboard Example
===========================

This example demonstrates how to use the modern, dark-themed `dark_grid.html`
template to create a dashboard with a high-contrast layout, perfect for NOCs
(Network Operations Centers) or live monitoring views.
"""

from sivo import Sivo, ProjectConfig
from sivo.core.dashboard import SivoDashboard

def main():
    # 1. Initialize empty dashboard using the dark_grid template
    dashboard = SivoDashboard(title="Global Server Status", columns=4)
    dashboard.set_grid_layout(
        desktop='''
    "main main side"
"bottom1 bottom2 side"
        ''',
        mobile='''
    "main"
"side"
"bottom1"
"bottom2"
        '''
    )

    # 2. Add an HTML Header
    header_html = '''
    <div style="padding: 10px;">
        <h3 style="margin: 0; color: #f8fafc; font-size: 1.25rem;">Live Feed</h3>
        <p style="color: #94a3b8; margin-top: 5px; font-size: 0.875rem;">System latency updates every 5s</p>
    </div>
    '''
    dashboard.add_html_block("live_feed", header_html)

    # 3. Create a primary Global Map spanning 3 columns
    world_map = Sivo.from_template('dashboards/sidebar_layout', layout_size="90%", lock_zoom_out=True)

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

    dashboard.add_sivo_block("global_network", world_map)

    # 4. Add a Metrics Panel on the right (1 column)
    dashboard.add_metrics_panel(
        "server_metrics",
        title="Server Telemetry",
        metrics=["cpu_load", "active_connections", "bandwidth"]
    )

    # 5. Add Details Panel
    dashboard.add_details_panel(
        "datacenter_logs",
        title="Node Logs",
        placeholder="Select a region on the map to view live logs."
    )

    # 6. Generate the HTML Dashboard
    print("Generating Dark Grid Dashboard to 'output.html'...")
    dashboard.to_html("output.html")
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
