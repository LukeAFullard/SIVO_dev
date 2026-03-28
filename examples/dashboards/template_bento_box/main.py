"""
Bento Box Dashboard Example
===========================

This example demonstrates how to use the modern, responsive `bento_box.html`
template to create a dashboard with multiple panels, maps, and metrics
arranged in an auto-fitting grid.
"""

from sivo import Sivo, ProjectConfig
from sivo.core.dashboard import SivoDashboard

def main():
    # 1. Initialize empty dashboard using the bento_box template
    dashboard = SivoDashboard(title="Operations Overview", columns=3)
    dashboard.set_grid_layout(
        desktop='''
    "header header header"
    "main main side1"
    "main main side2"
    "bottom1 bottom2 bottom3"
        ''',
        mobile='''
    "header"
    "main"
    "side1"
    "side2"
    "bottom1"
    "bottom2"
    "bottom3"
        '''
    )

    # 2. Add an HTML Title/Description block spanning all columns
    header_html = '''
    <div style="text-align: center; padding: 20px;">
        <h2 style="margin: 0; color: #1e293b; font-size: 1.5rem;">Global Infrastructure Status</h2>
        <p style="color: #64748b; margin-top: 10px;">Live monitoring of regional data centers and active server nodes.</p>
    </div>
    '''
    dashboard.add_html_block("header_info", header_html, grid_area="header")

    # 3. Create a primary Map for the left side
    us_map = Sivo.from_template('dashboards/sidebar_layout', layout_size="90%", lock_zoom_out=True)

    # Add some dummy interactions to the map
    us_map.map(
        "main_panel",
        color="#3b82f6",
        hover_color="#2563eb",
        tooltip="<h3>Main Panel Hub</h3><p>Status: Healthy<br>Nodes: 1,245</p>",
        callback_payload={"active_nodes": "1,245", "latency": "12ms", "uptime": "99.99%"}
    )
    us_map.map(
        "metric_box_1",
        color="#f59e0b",
        hover_color="#d97706",
        tooltip="<h3>Metric Box 1 Hub</h3><p>Status: Warning<br>Nodes: 850</p>",
        callback_payload={"active_nodes": "850", "latency": "45ms", "uptime": "98.5%"}
    )
    us_map.map(
        "metric_box_2",
        color="#3b82f6",
        hover_color="#2563eb",
        tooltip="<h3>Metric Box 2 Hub</h3><p>Status: Healthy<br>Nodes: 920</p>",
        callback_payload={"active_nodes": "920", "latency": "18ms", "uptime": "99.9%"}
    )

    # Add the primary map to the dashboard, taking up 2 columns
    dashboard.add_sivo_block("regional_map", us_map, grid_area="main")

    # 4. Create a Secondary Map (e.g., a specific floorplan or detailed area)
    floorplan = Sivo.from_template('dashboards/sidebar_layout', layout_size="80%", lock_scroll_bounds=False)
    floorplan.map("main_panel", color="#10b981", tooltip="London DC: Online")

    # Add the secondary map, taking up 1 column
    dashboard.add_sivo_block("eu_operations", floorplan, grid_area="side1")

    # 5. Add a Details Panel that updates on map clicks
    dashboard.add_details_panel(
        "hub_details",
        title="Node Details",
        placeholder="Click a state on the map to view regional hub details.",
        grid_area="bottom1"
    )

    # 6. Add a Metrics Panel that updates automatically via the `payload` dictionary
    dashboard.add_metrics_panel(
        "performance_metrics",
        title="Live Metrics",
        metrics=["active_nodes", "latency", "uptime"],
        grid_area="side2"
    )

    # 7. Generate the HTML Dashboard
    print("Generating Bento Box Dashboard to 'output.html'...")
    dashboard.to_html("output.html")
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
