import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # 1. Bar Chart Option (TX)
    bar_chart_option = {
        "title": {"text": "Texas Regional Sales"},
        "tooltip": {},
        "xAxis": {"data": ["Austin", "Dallas", "Houston", "San Antonio"]},
        "yAxis": {},
        "series": [{
            "name": "Sales",
            "type": "bar",
            "data": [5000, 20000, 36000, 10000],
            "itemStyle": {"color": "#43a2ca"}
        }]
    }

    # 2. Line Chart Option (CA)
    line_chart_option = {
        "title": {"text": "California Growth Trend"},
        "tooltip": {"trigger": "axis"},
        "xAxis": {"type": "category", "data": ["Q1", "Q2", "Q3", "Q4"]},
        "yAxis": {"type": "value"},
        "series": [{
            "data": [150, 230, 224, 218],
            "type": "line",
            "smooth": True,
            "itemStyle": {"color": "#ff7f50"}
        }]
    }

    # 3. Pie Chart Option (NY)
    pie_chart_option = {
        "title": {"text": "NY Demographics", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical", "left": "left"},
        "series": [{
            "name": "Access From",
            "type": "pie",
            "radius": "50%",
            "data": [
                {"value": 1048, "name": "Search Engine"},
                {"value": 735, "name": "Direct"},
                {"value": 580, "name": "Email"},
                {"value": 484, "name": "Union Ads"},
                {"value": 300, "name": "Video Ads"}
            ],
            "emphasis": {
                "itemStyle": {
                    "shadowBlur": 10,
                    "shadowOffsetX": 0,
                    "shadowColor": "rgba(0, 0, 0, 0.5)"
                }
            }
        }]
    }

    # 4. Gauge Chart Option (WY)
    gauge_chart_option = {
        "title": {"text": "Wyoming Energy Output", "left": "center"},
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [{
            "name": "Pressure",
            "type": "gauge",
            "detail": {"formatter": "{value}%"},
            "data": [{"value": 82, "name": "SCORE"}]
        }]
    }

    # Map the elements
    sivo_app.map(element_id="TX", tooltip="View Regional Data (Bar)", html="<h3>Bar Chart</h3>", echarts_option=bar_chart_option)
    sivo_app.map(element_id="CA", tooltip="View Growth Trend (Line)", html="<h3>Line Chart</h3>", echarts_option=line_chart_option)
    sivo_app.map(element_id="NY", tooltip="View Demographics (Pie)", html="<h3>Pie Chart</h3>", echarts_option=pie_chart_option)
    sivo_app.map(element_id="WY", tooltip="View Energy Output (Gauge)", html="<h3>Gauge Chart</h3>", echarts_option=gauge_chart_option)

    # Export to HTML
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported Multiple ECharts Actions HTML to {output_path}")

if __name__ == "__main__":
    main()
