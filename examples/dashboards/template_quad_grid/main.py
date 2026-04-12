"""
Quad Grid Layout Example
========================

This example demonstrates how to use the `SivoDashboard` with a CSS grid layout
to create a 2x2 grid. Each card is positioned inside a responsive grid area,
perfect for showing 4 key visualizations or metrics.
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
    tl_map.map(
        "quadrant_1",
        color="#3b82f6",
        hover_color="#2563eb",
        html="<h3>Primary Region</h3><p>This is the main area of interest.</p>",
        callback_payload={"metric_val": "$1.2M"}
    )
    dashboard.add_sivo_block("sales_map", tl_map, grid_area="tl")

    # 2. Top Right - Metrics
    dashboard.add_metrics_panel(
        "sales_metrics",
        title="Sales KPIs",
        metrics=["metric_val"],
        grid_area="tr"
    )

    # 3. Bottom Left - Map
    bl_map = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)
    bl_map.map(
        "quadrant_4",
        color="#ef4444",
        hover_color="#dc2626",
        html="<h3>Critical Region</h3><p>This area requires immediate attention.</p>",
        callback_payload={"metric_val": "$340K"}
    )
    dashboard.add_sivo_block("issues_map", bl_map, grid_area="bl")

    # 4. Bottom Right - Details
    dashboard.add_details_panel(
        "analysis_details",
        title="Detailed Analysis",
        placeholder="Select a region on the map.",
        grid_area="br"
    )

    import os
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    print(f"Generating Quad Grid Dashboard to '{output_path}'...")
    dashboard.to_html(output_path)
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
