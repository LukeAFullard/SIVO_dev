from sivo import Sivo
import os
import lxml.etree as etree

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "dashboard_template.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="light",
        ambient_effect="snow" # Gentle particle effect for sustainability theme
    )

    # Header
    app.add_scalable_text("header_area", "Corporate Sustainability & ESG Reporting", left="2%", top="20%", width="96%", height="40%", font_size="35%", font_weight="900", color="#0f172a", align="left")
    app.add_scalable_text("header_area", "Scope 1, 2, & 3 Emissions and Renewable Energy Transitions • FY2026 Q3", left="2%", top="60%", width="96%", height="20%", font_size="15%", font_weight="600", color="#64748b", align="left")

    # Metric 1: Carbon Offset
    app.add_scalable_text("metric_1", "TOTAL CO2 OFFSET", left="10%", top="20%", width="80%", height="15%", font_size="12%", font_weight="700", color="#64748b")
    app.add_scalable_text("metric_1", "2.4M", left="10%", top="40%", width="80%", height="35%", font_size="40%", font_weight="900", color="#10b981")
    app.add_scalable_text("metric_1", "Metric Tons (YTD)", left="10%", top="75%", width="80%", height="10%", font_size="10%", font_weight="600", color="#94a3b8")

    # Metric 2: Renewables Mix (Stacked Bar)
    app.map_bar_chart(
        element_id="metric_2",
        title="Energy Mix by Region (%)",
        categories=["NA", "EMEA", "APAC", "LATAM"],
        data=[
            {"name": "Solar", "type": "bar", "stack": "total", "data": [40, 50, 30, 60], "itemStyle": {"color": "#fbbf24"}, "emphasis": {"focus": "series"}},
            {"name": "Wind", "type": "bar", "stack": "total", "data": [35, 40, 20, 25], "itemStyle": {"color": "#60a5fa"}, "emphasis": {"focus": "series"}},
            {"name": "Fossil", "type": "bar", "stack": "total", "data": [25, 10, 50, 15], "itemStyle": {"color": "#94a3b8"}, "emphasis": {"focus": "series"}}
        ],
        extra_options={
            "grid": {"top": 40, "bottom": 30, "left": 40, "right": 20},
            "legend": {"show": True, "bottom": 0, "textStyle": {"fontSize": 10}},
            "backgroundColor": "transparent",
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}}
        }
    )

    # Metric 3: ESG Score
    app.add_scalable_text("metric_3", "MSCI ESG RATING", left="10%", top="20%", width="80%", height="15%", font_size="12%", font_weight="700", color="#64748b")
    app.add_scalable_text("metric_3", "AA", left="10%", top="40%", width="80%", height="35%", font_size="45%", font_weight="900", color="#8b5cf6")

    app.add_scalable_text("metric_3", "INDUSTRY PERCENTILE", left="10%", top="75%", width="50%", height="10%", font_size="8%", font_weight="700", color="#64748b")
    app.add_scalable_progress_bar("metric_3", progress="88%", left="55%", top="75%", width="35%", height="5%", rx="4", bg_color="#e2e8f0", fill_color="#8b5cf6")

    # Main Chart Area: Dot Density Map
    app.map_nested_map_chart(
        element_id="main_chart_area",
        title="Global Facility Carbon Emissions (Dot Density)",
        map_name="world",
        map_data="world",
        data=[], # Empty base choropleth data
        extra_options={
            "backgroundColor": "transparent",
            "geo": {"itemStyle": {"areaColor": "#e2e8f0", "borderColor": "#cbd5e1"}, "roam": False},
            "title": {"textStyle": {"fontSize": 16, "color": "#1e293b", "fontWeight": "600"}}
        }
    )

    # We use a custom dictionary to map values to coordinates for the dot density
    # (Since these countries aren't distinct SVG regions in this dashboard template's base SVG,
    #  but rather handled via ECharts nested geo, we'll configure a scatter series directly).
    # It requires lat/lon coords.

    cities = [
        {"name": "New York", "value": [ -74, 40.7, 120]},
        {"name": "London", "value": [ -0.1, 51.5, 80]},
        {"name": "Beijing", "value": [ 116.4, 39.9, 250]},
        {"name": "Mumbai", "value": [ 72.8, 19.0, 180]},
        {"name": "Sao Paulo", "value": [ -46.6, -23.5, 60]},
        {"name": "Sydney", "value": [ 151.2, -33.8, 90]}
    ]

    # Apply the scatter to the existing nested map options
    app.map("main_chart_area", echarts_option={
        "series": [{
            "name": "Emissions",
            "type": "scatter",
            "coordinateSystem": "geo",
            "data": cities,
            "symbolSize": 15, # Would ideally use a function (val[2]/10), but static is safer here
            "itemStyle": {
                "color": "rgba(239, 68, 68, 0.6)",
                "shadowBlur": 10,
                "shadowColor": "rgba(239, 68, 68, 0.5)"
            },
            "tooltip": {
                "formatter": "{b}: {c}kt CO2e"
            }
        }, {
            # Adding an effect scatter for the highest emitters
            "name": "High Emissions",
            "type": "effectScatter",
            "coordinateSystem": "geo",
            "data": [cities[2], cities[3]], # Beijing and Mumbai
            "symbolSize": 20,
            "showEffectOn": "render",
            "rippleEffect": {"brushType": "stroke"},
            "itemStyle": {"color": "#ef4444"}
        }]
    })

    # Sidebar Area Top: Waste Diversion Rate
    app.map_pie_chart(
        element_id="sidebar_area_top",
        title="Global Waste Diversion",
        data=[
            {"name": "Recycled", "value": 58},
            {"name": "Composted", "value": 14},
            {"name": "Landfill", "value": 28}
        ],
        extra_options={
            "series": [{
                "radius": ["50%", "70%"],
                "avoidLabelOverlap": False,
                "itemStyle": {"borderRadius": 5, "borderColor": "#fff", "borderWidth": 2},
                "label": {"show": False, "position": "center"},
                "emphasis": {
                    "label": {"show": True, "fontSize": 14, "fontWeight": "bold"}
                }
            }],
            "color": ["#3b82f6", "#10b981", "#94a3b8"],
            "title": {"textStyle": {"fontSize": 16, "color": "#334155"}},
            "backgroundColor": "transparent",
            "legend": {"show": True, "orient": "vertical", "left": "left"}
        }
    )

    # Sidebar Area Bottom: Water Usage Trend
    app.map_line_chart(
        element_id="sidebar_area_bottom",
        title="Water Consumption (M Gallons)",
        categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"],
        data=[
            {"name": "2025", "type": "line", "data": [45, 42, 48, 50, 55, 60, 62, 58, 50], "itemStyle": {"color": "#94a3b8"}, "lineStyle": {"type": "dashed", "width": 2}},
            {"name": "2026", "type": "line", "data": [40, 38, 42, 45, 48, 52, 50, 48, 42], "itemStyle": {"color": "#0ea5e9"}, "areaStyle": {"opacity": 0.2}, "lineStyle": {"width": 3}}
        ],
        color="#0ea5e9",
        smooth=True,
        title_size=16,
        title_color="#1e293b",
        extra_options={
            "grid": {"top": 50, "bottom": 30, "left": 40, "right": 20},
            "backgroundColor": "transparent",
            "legend": {"show": True, "top": 20, "right": 0, "textStyle": {"fontSize": 10}},
            "tooltip": {"trigger": "axis"}
        }
    )

    output_path = os.path.join(os.path.dirname(__file__), "03_modern_dashboard.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
