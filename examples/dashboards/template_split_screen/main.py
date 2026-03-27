"""
Split Screen Dashboard Example
==============================

This example demonstrates how to use the `split_screen.html` template
to create a dual-pane layout suitable for comparing two primary components side-by-side.
"""

from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    dashboard = SivoDashboard(title="Comparison Dashboard", columns=2, template="split_screen")

    # Left Map
    left_map = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)

    left_map.map(
        "quadrant_1",
        color="#3b82f6",
        hover_color="#2563eb",
        tooltip="<h3>Region A1</h3><p>Status: Active</p>",
        callback_payload={"left_metric_1": "120", "left_metric_2": "45%"}
    )

    dashboard.add_sivo_block("left_view", left_map, slot="left")

    # Left Details
    dashboard.add_details_panel(
        "left_details",
        title="Left View Details",
        placeholder="Select a region on the left to view details.",
        slot="left"
    )

    # Right Map
    right_map = Sivo.from_template('dashboards/four_quadrants', layout_size="90%", lock_zoom_out=True)

    right_map.map(
        "quadrant_2",
        color="#10b981",
        hover_color="#059669",
        tooltip="<h3>Region B2</h3><p>Status: Stable</p>",
        callback_payload={"right_metric_1": "85", "right_metric_2": "90%"}
    )

    dashboard.add_sivo_block("right_view", right_map, slot="right")

    # Right Details
    dashboard.add_details_panel(
        "right_details",
        title="Right View Details",
        placeholder="Select a region on the right to view details.",
        slot="right"
    )

    print("Generating Split Screen Dashboard to 'output.html'...")
    dashboard.to_html("output.html")
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
