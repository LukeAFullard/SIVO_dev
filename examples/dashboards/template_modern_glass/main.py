"""
Modern Glass Dashboard Example
==============================

This example demonstrates how to use the `modern_glass.html` template
to create a beautiful, translucent glassmorphism styled dashboard.
"""

from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(title="E-Commerce Analytics", columns=3)
    dashboard.set_grid_layout(
        desktop='''
    "header header"
"main sidebar"
        ''',
        mobile='''
    "header"
"main"
"sidebar"
        '''
    )

    header_html = '''
    <div style="text-align: center; padding: 10px;">
        <h2 style="margin: 0; color: #1a202c; font-size: 1.5rem;">Global Sales Analytics</h2>
        <p style="color: #718096; margin-top: 5px;">Live tracking of sales regions and revenue.</p>
    </div>
    '''
    dashboard.add_html_block("header_info", header_html)

    # Primary Map
    sales_map = Sivo.from_template('dashboards/sidebar_layout', layout_size="90%", lock_zoom_out=True)

    sales_map.map(
        "main_panel",
        color="#4299e1",
        hover_color="#3182ce",
        tooltip="<h3>North America</h3><p>Status: Excellent<br>Revenue: $2.4M</p>",
        callback_payload={"revenue": "$2.4M", "growth": "+12%", "active_users": "145K"}
    )
    sales_map.map(
        "metric_box_1",
        color="#9f7aea",
        hover_color="#805ad5",
        tooltip="<h3>Europe</h3><p>Status: Good<br>Revenue: $1.8M</p>",
        callback_payload={"revenue": "$1.8M", "growth": "+8%", "active_users": "112K"}
    )
    sales_map.map(
        "metric_box_2",
        color="#ed8936",
        hover_color="#dd6b20",
        tooltip="<h3>Asia Pacific</h3><p>Status: Emerging<br>Revenue: $850K</p>",
        callback_payload={"revenue": "$850K", "growth": "+24%", "active_users": "85K"}
    )

    dashboard.add_sivo_block("sales_regions", sales_map)

    # Details Panel
    dashboard.add_details_panel(
        "region_details",
        title="Region Insights",
        placeholder="Select a region on the map to view detailed insights."
    )

    # Metrics Panel
    dashboard.add_metrics_panel(
        "kpi_metrics",
        title="Key Performance Indicators",
        metrics=["revenue", "growth", "active_users"]
    )

    print("Generating Modern Glass Dashboard to 'output.html'...")
    dashboard.to_html("output.html")
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
