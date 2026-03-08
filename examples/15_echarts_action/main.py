import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # 1. Define an ECharts option dict
    bar_chart_option = {
        "title": {
            "text": "Texas Regional Sales"
        },
        "tooltip": {},
        "xAxis": {
            "data": ["Austin", "Dallas", "Houston", "San Antonio"]
        },
        "yAxis": {},
        "series": [
            {
                "name": "Sales",
                "type": "bar",
                "data": [5000, 20000, 36000, 10000],
                "itemStyle": {
                    "color": "#43a2ca"
                }
            }
        ]
    }

    # 2. Map the element to trigger the chart
    sivo_app.map(
        element_id="TX",
        tooltip="View Regional Data",
        html="<h3>Detailed Overview</h3><p>Clicking this element triggered a nested ECharts visualization.</p>",
        echarts_option=bar_chart_option
    )

    # 3. Export to HTML
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported ECharts Action HTML to {output_path}")

if __name__ == "__main__":
    main()
