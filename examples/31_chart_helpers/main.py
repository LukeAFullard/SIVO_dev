import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    # Initialize Sivo from SVG
    sivo_app = Sivo.from_svg(svg_path)

    # 1. Bar Chart
    sivo_app.map_bar_chart(
        element_id="TX",
        title="Texas Regional Sales",
        data=[5000, 20000, 36000, 10000],
        categories=["Austin", "Dallas", "Houston", "San Antonio"],
        color="#43a2ca",
        tooltip="View Regional Data (Bar)"
    )

    # 2. Line Chart
    sivo_app.map_line_chart(
        element_id="CA",
        title="California Growth Trend",
        data=[150, 230, 224, 218],
        categories=["Q1", "Q2", "Q3", "Q4"],
        color="#ff7f50",
        tooltip="View Growth Trend (Line)"
    )

    # 3. Pie Chart
    sivo_app.map_pie_chart(
        element_id="NY",
        title="NY Demographics",
        data=[
            {"value": 1048, "name": "Search Engine"},
            {"value": 735, "name": "Direct"},
            {"value": 580, "name": "Email"}
        ],
        tooltip="View Demographics (Pie)"
    )

    # 4. Gauge Chart
    sivo_app.map_gauge_chart(
        element_id="WY",
        title="Wyoming Energy Output",
        value=82,
        max_value=100,
        tooltip="View Energy Output (Gauge)"
    )

    # Export to HTML
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported Interactive Chart Helpers HTML to {output_path}")

if __name__ == "__main__":
    main()
