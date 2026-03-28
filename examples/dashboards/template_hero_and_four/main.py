"""
Hero and Four Layout Example
============================

This example demonstrates how to use the `hero_and_four.html` template.
The template provides a 2-column layout where the left column is a single
large hero component (square aspect ratio) and the right column contains a 2x2 grid
of smaller components.
"""

from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(title="Executive Summary")
    dashboard.set_grid_layout(
        desktop='''
    "hero hero"
"box1 box2"
"box3 box4"
        ''',
        mobile='''
    "hero"
"box1"
"box2"
"box3"
"box4"
        '''
    )

    # The Hero component
    main_map = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)
    main_map.map("quadrant_1", color="#3b82f6", hover_color="#2563eb", tooltip="<h3>Primary Region</h3><p>Focus Area</p>")
    dashboard.add_sivo_block("primary_focus", main_map, grid_area="hero")

    # The four quad components
    # 1. Top Left Metric
    dashboard.add_metrics_panel(
        "q1_metrics",
        title="Revenue",
        metrics=["revenue", "growth"],
        grid_area="box1"
    )

    # 2. Top Right Map
    tr_map = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)
    tr_map.map("quadrant_2", color="#10b981", hover_color="#059669")
    dashboard.add_sivo_block("secondary_focus", tr_map, grid_area="box2")

    # 3. Bottom Left Map
    bl_map = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)
    bl_map.map("quadrant_3", color="#f59e0b", hover_color="#d97706")
    dashboard.add_sivo_block("tertiary_focus", bl_map, grid_area="box3")

    # 4. Bottom Right Details
    dashboard.add_details_panel(
        "q4_details",
        title="Quick Analysis",
        placeholder="Select a region to view analysis.",
        grid_area="box4"
    )


    print("Generating Hero and Four Dashboard to 'output.html'...")
    dashboard.to_html("output.html")
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
