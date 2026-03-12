import os
import sys

# Add the src directory to the sys path so we can import sivo locally
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from sivo import ProjectConfig, Sivo

def analyze_trend(data):
    """Simple calculation to determine trend direction."""
    if not data or len(data) < 2:
        return "Flat"

    first_y = data[0][1]
    last_y = data[-1][1]
    diff = last_y - first_y

    # We add a small threshold to determine "Flat"
    if diff > 1.5:
        return "Increasing"
    elif diff < -1.5:
        return "Reducing"
    else:
        return "Flat"

def create_exaggerated_trendline_infographic():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")
    config = ProjectConfig(
        title="Exaggerated Trendlines",
        svg_file=svg_path,
        enable_minimap=False,
        theme="light"
    )

    app = Sivo.from_config(config)

    # Simulated Data
    data_increasing = [[1, 2], [2, 3], [3, 2.5], [4, 5], [5, 4.5], [6, 7], [7, 6], [8, 9]]
    data_reducing = [[1, 9], [2, 7.5], [3, 8], [4, 5], [5, 6], [6, 3], [7, 4], [8, 1]]
    data_flat = [[1, 5], [2, 5.5], [3, 4.5], [4, 5.2], [5, 4.8], [6, 5], [7, 4.9], [8, 5.1]]

    # 1. Increasing Trendline
    label_increasing = analyze_trend(data_increasing)
    app.map_trendline_chart(
        element_id="chart_increasing",
        title="Sales (Increasing)",
        data=data_increasing,
        trendline_type="linear",
        trendline_color="#10b981", # Green
        trendline_width=10,        # Exaggerated width
        trendline_arrow=True,
        trendline_arrow_size=30,   # Exaggerated arrow size
        trendline_label=label_increasing, # Dynamic label
        color="#a7f3d0",           # Light Green
        grid_margin=[60, 100, 40, 40] # Add right margin so label isn't cut off
    )

    # 2. Reducing Trendline
    label_reducing = analyze_trend(data_reducing)
    app.map_trendline_chart(
        element_id="chart_reducing",
        title="Costs (Reducing)",
        data=data_reducing,
        trendline_type="linear",
        trendline_color="#ef4444", # Red
        trendline_width=10,
        trendline_arrow=True,
        trendline_arrow_size=30,
        trendline_label=label_reducing,
        color="#fca5a5",
        grid_margin=[60, 100, 40, 40]
    )

    # 3. Flat Trendline
    label_flat = analyze_trend(data_flat)
    app.map_trendline_chart(
        element_id="chart_flat",
        title="Engagement (Flat)",
        data=data_flat,
        trendline_type="linear",
        trendline_color="#f59e0b", # Orange
        trendline_width=10,
        trendline_arrow=True,
        trendline_arrow_size=30,
        trendline_label=label_flat,
        color="#fde68a",
        grid_margin=[60, 100, 40, 40]
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    app.to_html(output_path)
    print(f"Exported Exaggerated Trendlines Example to {output_path}")

if __name__ == "__main__":
    create_exaggerated_trendline_infographic()
