"""
Quad Grid Layout Example
========================

This example demonstrates how to use the `quad_grid.html` template.
The template provides a simple 2x2 grid where each card is forced to have
a square aspect ratio, perfect for showing 4 key visualizations or metrics.
"""

from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(title="KPI Overview")
    dashboard.set_grid_layout(
        desktop='''
    "tl tr"
"bl br"
        ''',
        mobile='''
    "tl"
"tr"
"bl"
"br"
        '''
    )

    # 1. Top Left - Map
    tl_map = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)
    tl_map.map("quadrant_1", color="#3b82f6", hover_color="#2563eb", tooltip="Primary Region", callback_payload={"metric_val": "$1.2M"})
    dashboard.add_sivo_block("sales_map", tl_map)

    # 2. Top Right - Metrics
    dashboard.add_metrics_panel(
        "sales_metrics",
        title="Sales KPIs",
        metrics=["metric_val"]
    )

    # 3. Bottom Left - Map
    bl_map = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)
    bl_map.map("quadrant_4", color="#ef4444", hover_color="#dc2626", tooltip="Critical Region")
    dashboard.add_sivo_block("issues_map", bl_map)

    # 4. Bottom Right - Details
    dashboard.add_details_panel(
        "analysis_details",
        title="Detailed Analysis",
        placeholder="Select a region on the map."
    )

    print("Generating Quad Grid Dashboard to 'output.html'...")
    dashboard.to_html("output.html")
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
