import os
import sys

# Add the src directory to the sys path so we can import sivo locally
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from sivo import ProjectConfig, Sivo

def create_trendline_infographic():
    # 1. Initialize configuration with the SVG file path
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")
    config = ProjectConfig(
        title="Trendline Variations",
        svg_file=svg_path,
        enable_minimap=False,
        theme="light"
    )

    # 2. Create the Sivo app
    app = Sivo.from_config(config)

    # Simulated Data
    linear_data = [[1, 2], [2, 4], [3, 5], [4, 4.5], [5, 6], [6, 8], [7, 7.5], [8, 10]]
    exp_data = [[1, 1], [2, 2.5], [3, 4], [4, 8], [5, 12], [6, 25], [7, 30], [8, 60]]
    log_data = [[1, 10], [2, 25], [3, 30], [4, 38], [5, 42], [6, 45], [7, 48], [8, 50]]
    poly_data = [[1, 5], [2, 12], [3, 8], [4, 3], [5, 4], [6, 15], [7, 25], [8, 10]]

    # Map Linear Trendline
    app.map_trendline_chart(
        element_id="chart_linear",
        title="Sales (Linear Trend)",
        data=linear_data,
        trendline_type="linear",
        trendline_color="#3b82f6", # Blue
        trendline_width=3,
        trendline_arrow=True,
        color="#93c5fd" # Light Blue
    )

    # Map Exponential Trendline
    app.map_trendline_chart(
        element_id="chart_exponential",
        title="User Growth (Exponential)",
        data=exp_data,
        trendline_type="exponential",
        trendline_color="#ef4444", # Red
        trendline_width=2,
        trendline_arrow=False,
        color="#fca5a5" # Light Red
    )

    # Map Logarithmic Trendline
    app.map_trendline_chart(
        element_id="chart_logarithmic",
        title="Engagement (Logarithmic)",
        data=log_data,
        trendline_type="logarithmic",
        trendline_color="#10b981", # Green
        trendline_width=4,
        trendline_arrow=True,
        color="#6ee7b7" # Light Green
    )

    # Map Polynomial Trendline
    app.map_trendline_chart(
        element_id="chart_polynomial",
        title="Stock Price (Polynomial)",
        data=poly_data,
        trendline_type="polynomial",
        trendline_color="#8b5cf6", # Purple
        trendline_width=2,
        trendline_arrow=False,
        color="#c4b5fd" # Light Purple
    )

    # Export to HTML
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    app.to_html(output_path)
    print(f"Exported Trendlines Example to {output_path}")

if __name__ == "__main__":
    create_trendline_infographic()
