"""
Modern Glass Dashboard Example
==============================

This example demonstrates how to recreate a "Modern Glass" dashboard layout
using SivoDashboard's CSS Grid and custom JS injection. By explicitly passing
CSS via `custom_js` and applying it to the SIVO block elements, you can achieve
glassmorphism aesthetics without relying on deprecated HTML layout templates.
"""

from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(title="E-Commerce Analytics", columns=3)

    # We use a 3-column setup where "header" spans across 3 columns, "main" takes up 2, and sidebars take up 1
    dashboard.set_grid_layout(
        desktop='''
    "header header header"
    "main main sidebar1"
    "main main sidebar2"
        ''',
        mobile='''
    "header"
    "main"
    "sidebar1"
    "sidebar2"
        '''
    )

    header_html = '''
    <div style="text-align: center; padding: 10px; color: white;">
        <h2 style="margin: 0; font-size: 1.5rem;">Global Sales Analytics</h2>
        <p style="margin-top: 5px; opacity: 0.8;">Live tracking of sales regions and revenue.</p>
    </div>
    '''
    dashboard.add_html_block("header_info", header_html, grid_area="header")

    # Primary Map
    sales_map = Sivo.from_template('dashboards/sidebar_layout', layout_size="90%", lock_zoom_out=True)

    sales_map.map(
        "main_panel",
        color="#4299e1",
        hover_color="#3182ce",
        html="<h3>North America</h3><p>Status: Excellent<br>Revenue: $2.4M</p>",
        callback_payload={"revenue": "$2.4M", "growth": "+12%", "active_users": "145K"}
    )
    sales_map.map(
        "metric_box_1",
        color="#9f7aea",
        hover_color="#805ad5",
        html="<h3>Europe</h3><p>Status: Good<br>Revenue: $1.8M</p>",
        callback_payload={"revenue": "$1.8M", "growth": "+8%", "active_users": "112K"}
    )
    sales_map.map(
        "metric_box_2",
        color="#ed8936",
        hover_color="#dd6b20",
        html="<h3>Asia Pacific</h3><p>Status: Emerging<br>Revenue: $850K</p>",
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

    custom_js = '''
    <style>
        /* Base background for the page to show off glassmorphism */
        body {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #ffffff;
            font-family: sans-serif;
            margin: 0;
            padding: 20px;
        }

        /* Target all sivo dashboard blocks to apply glass effect */
        .sivo-grid-block {
            background: rgba(255, 255, 255, 0.1) !important;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 16px !important;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1) !important;
            color: white !important;
        }

        /* Adjust panel internal typography to match dark mode */
        .sivo-grid-block h2, .sivo-grid-block h3, .sivo-grid-block p, .sivo-grid-block div {
            color: #f8fafc !important;
        }

        .metric-value {
            color: #38bdf8 !important;
        }

        /* Set grid gap */
        .sivo-dashboard-container {
            gap: 20px !important;
        }
    </style>
    '''

    import os
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    print(f"Generating Modern Glass Dashboard to '{output_path}'...")
    dashboard.to_html(output_path, custom_js=custom_js)
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
