import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    # Initialize Sivo from SVG
    sivo_app = Sivo.from_svg(svg_path, theme="dark")

    # 1. Bar Chart with styling
    sivo_app.map_bar_chart(
        element_id="TX",
        title="Texas Regional Sales",
        data=[5000, 20000, 36000, 10000],
        categories=["Austin", "Dallas", "Houston", "San Antonio"],
        color="#38bdf8",
        tooltip="View Regional Data (Bar)",
        title_color="#facc15",
        title_size=20,
        axis_color="#9ca3af",
        tooltip_bg_color="rgba(0, 0, 0, 0.8)",
        grid_margin=[60, 20, 40, 60]
    )

    # 2. Line Chart with morphing transition enabled
    # Clicking CA will show a line chart. If you were viewing TX first,
    # the ECharts universal transition will attempt to morph the bar chart into the line chart.
    sivo_app.map_line_chart(
        element_id="CA",
        title="California Growth Trend",
        data=[150, 230, 224, 218],
        categories=["Q1", "Q2", "Q3", "Q4"],
        color="#a78bfa",
        smooth=True,
        tooltip="View Growth Trend (Line)",
        title_color="#cbd5e1",
        universal_transition=True,
        extra_options={"series": [{"areaStyle": {"opacity": 0.2}}]} # Example of injecting raw echarts options
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
        tooltip="View Demographics (Pie)",
        title_color="#fff"
    )

    # Export to HTML
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported Interactive Chart Helpers HTML to {output_path}")

if __name__ == "__main__":
    main()
