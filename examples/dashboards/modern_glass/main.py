"""
Modern Glass Dashboard Example
==============================

This example demonstrates how to build a multi-block dashboard with SivoDashboard
using custom CSS grid layouts. (Note: The older HTML templates are deprecated,
so we use the modular layout builder instead to achieve similar or better structures.)
"""

from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(title="E-Commerce Analytics", columns=3)

    # Modern Glass specific stylings can be applied via panel_css or custom_js,
    # but the structure is entirely controlled by the CSS grid layout.
    dashboard.set_grid_layout(
        desktop='''
    "header header header"
    "main sidebar1 sidebar2"
        ''',
        mobile='''
    "header"
    "main"
    "sidebar1"
    "sidebar2"
        '''
    )

    header_html = '''
    <div style="text-align: center; padding: 20px; background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(10px); border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.3);">
        <h2 style="margin: 0; color: #1a202c; font-size: 2rem; font-weight: 600;">Global Sales Analytics</h2>
        <p style="color: #4a5568; margin-top: 8px; font-size: 1.1rem;">Live tracking of sales regions and revenue.</p>
    </div>
    '''
    dashboard.add_html_block("header_info", header_html, grid_area="header")

    # Primary Map
    sales_map = Sivo.from_template(
        'dashboards/sidebar_layout',
        layout_size="90%",
        lock_zoom_out=True,
        # Default panel position is 'none', so panel overlay won't trigger automatically
        default_panel_position="none"
    )

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

    dashboard.add_sivo_block("sales_regions", sales_map, grid_area="main")

    # Details Panel
    dashboard.add_details_panel(
        "region_details",
        title="Region Insights",
        placeholder="Select a region on the map to view detailed insights.",
        grid_area="sidebar1"
    )

    # Metrics Panel
    dashboard.add_metrics_panel(
        "kpi_metrics",
        title="Key Performance Indicators",
        metrics=["revenue", "growth", "active_users"],
        grid_area="sidebar2"
    )

    # We add custom glassmorphism CSS
    custom_css_js = '''
    <style>
        body {
            background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        }
        .sivo-grid-item {
            background: rgba(255, 255, 255, 0.45);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.18);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        .sivo-details-panel, .sivo-metrics-panel {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
        }
    </style>
    '''

    print("Generating Modern Glass Dashboard to 'output.html'...")
    dashboard.to_html("output.html", custom_js=custom_css_js)
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
