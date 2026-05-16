import os
import sys

# Ensure SIVO core can be imported from the repo root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    # 1. Define a simple static SVG map
    svg_content = """
    <svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
        <rect id="region_a" x="10" y="10" width="180" height="180" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
        <text x="100" y="100" text-anchor="middle" font-family="sans-serif" font-size="20" pointer-events="none">Region A</text>

        <rect id="region_b" x="210" y="10" width="180" height="180" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
        <text x="300" y="100" text-anchor="middle" font-family="sans-serif" font-size="20" pointer-events="none">Region B</text>
    </svg>
    """

    # 2. Initialize SIVO and map interactions
    sivo_app = Sivo.from_string(svg_content)

    # Define payload updates for the chart depending on which region is clicked.
    # Notice we pass a full ECharts `series` option dict to dynamically replace the data.
    sivo_app.map(
        "region_a",
        hover_color="#bae6fd",
        callback_payload={
            "my_chart_update": {
                "series": [{
                    "data": [120, 200, 150, 80, 70, 110, 130],
                    "type": 'bar',
                    "itemStyle": {"color": "#38bdf8"}
                }]
            }
        }
    )

    sivo_app.map(
        "region_b",
        hover_color="#fca5a5",
        callback_payload={
            "my_chart_update": {
                "series": [{
                    "data": [300, 45, 90, 210, 140, 60, 20],
                    "type": 'bar',
                    "itemStyle": {"color": "#f87171"}
                }]
            }
        }
    )

    # 3. Create a Responsive SivoDashboard Layout
    dashboard = SivoDashboard(title="Native Chart Blocks Example")

    # Define a 2-column grid layout where the map and chart sit side-by-side
    dashboard.set_grid_layout(
        desktop="""
        'title title'
        'map chart'
        """,
        mobile="""
        'title'
        'map'
        'chart'
        """
    )

    # Add a title block
    dashboard.add_html_block(
        "title",
        "<h2 style='text-align: center; font-family: sans-serif; color: #334155;'>Click a region to update the chart dynamically</h2>",
        grid_area="title"
    )

    # Add the SIVO graphic
    dashboard.add_sivo_block("map", sivo_app, grid_area="map")

    # 4. Add a Native Chart Block
    # We provide an initial base ECharts configuration dictionary.
    initial_chart_option = {
        "title": {
            "text": 'Weekly Sales'
        },
        "tooltip": {},
        "xAxis": {
            "type": 'category',
            "data": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [
            {
                "data": [0, 0, 0, 0, 0, 0, 0],
                "type": 'bar'
            }
        ]
    }

    # We bind the chart to the "my_chart_update" payload key.
    # Whenever a map element is clicked that contains this key in its callback_payload,
    # the chart will automatically update via `myChart.setOption(payload)`.
    dashboard.add_chart_block(
        "chart",
        option=initial_chart_option,
        payload_key="my_chart_update",
        grid_area="chart",
        min_height="400px"
    )

    # 5. Export to HTML
    output_filename = "native_chart_blocks.html"
    dashboard.to_html(output_filename)

    print(f"✅ Generated {output_filename}")
    print(f"Open it in your browser to see the interactive cross-filtering.")

if __name__ == "__main__":
    main()
