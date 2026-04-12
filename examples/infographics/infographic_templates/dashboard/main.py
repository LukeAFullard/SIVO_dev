from sivo import Sivo
import os

# Build the Dashboard Infographic using the new from_template method
dashboard = Sivo.from_template("3_2/dashboard", default_panel_position="none")

# --- Overlays on Dashboard ---
# Header overlay
header_html = """
<div style="text-align: center; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; box-sizing: border-box; padding: 5%; container-type: inline-size;">
    <h1 style="margin: 0; color: #333; font-family: sans-serif; font-size: clamp(10px, 3cqw, 32px);">Global Sales Overview 2024</h1>
    <p style="margin: 5px 0 0 0; color: #666; font-family: sans-serif; font-size: clamp(6px, 1.5cqw, 16px);">Interactive Business Intelligence Dashboard</p>
</div>
"""
dashboard.add_overlay("header_area", header_html)

# Key Metrics overlays
metric1_html = """
<div style="text-align: center; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; box-sizing: border-box; padding: 5%; container-type: inline-size;">
    <h3 style="margin: 0; color: #888; font-family: sans-serif; font-size: clamp(8px, 5cqw, 18px);">Total Revenue</h3>
    <p style="margin: 5px 0 0 0; color: #2ecc71; font-family: sans-serif; font-size: clamp(16px, 12cqw, 48px); font-weight: bold;">$12.5M</p>
</div>
"""
dashboard.add_overlay("metric_1", metric1_html)

metric2_html = """
<div style="text-align: center; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; box-sizing: border-box; padding: 5%; container-type: inline-size;">
    <h3 style="margin: 0; color: #888; font-family: sans-serif; font-size: clamp(8px, 5cqw, 18px);">Active Users</h3>
    <p style="margin: 5px 0 0 0; color: #3498db; font-family: sans-serif; font-size: clamp(16px, 12cqw, 48px); font-weight: bold;">84,290</p>
</div>
"""
dashboard.add_overlay("metric_2", metric2_html)

metric3_html = """
<div style="text-align: center; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; box-sizing: border-box; padding: 5%; container-type: inline-size;">
    <h3 style="margin: 0; color: #888; font-family: sans-serif; font-size: clamp(8px, 5cqw, 18px);">Growth Rate</h3>
    <p style="margin: 5px 0 0 0; color: #e74c3c; font-family: sans-serif; font-size: clamp(16px, 12cqw, 48px); font-weight: bold;">+14%</p>
</div>
"""
dashboard.add_overlay("metric_3", metric3_html)

# --- Interactive ECharts Binding to Areas ---
# Main Chart interaction
main_chart_option = {
    "title": {"text": "Monthly Sales Performance"},
    "tooltip": {"trigger": "axis"},
    "xAxis": {"type": "category", "data": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]},
    "yAxis": {"type": "value"},
    "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line", "smooth": True}]
}
dashboard.map(
    element_id="main_chart_area",
    panel_position="overlay",
    html="<h3>Monthly Sales Performance</h3><p>Click to view full sales chart</p>",
    echarts_option=main_chart_option,
    hover_color="#f1f5f9"
)

# Sidebar interaction (e.g., Pie chart)
sidebar_chart_option = {
    "title": {"text": "Sales by Region", "left": "center"},
    "tooltip": {"trigger": "item"},
    "series": [{
        "name": "Region",
        "type": "pie",
        "radius": "50%",
        "data": [
            {"value": 1048, "name": "North America"},
            {"value": 735, "name": "Europe"},
            {"value": 580, "name": "Asia"},
        ],
        "emphasis": {"itemStyle": {"shadowBlur": 10, "shadowOffsetX": 0, "shadowColor": "rgba(0, 0, 0, 0.5)"}}
    }]
}
dashboard.map(
    element_id="sidebar_area_top",
    panel_position="overlay",
    html="<h3>Sales by Region</h3><p>View regional breakdown</p>",
    echarts_option=sidebar_chart_option,
    hover_color="#f1f5f9"
)

# Another interactive widget (e.g., Markdown/Info)
dashboard.map(
    element_id="sidebar_area_bottom",
    panel_position="overlay",
    html="<h3>Recent Updates</h3><ul><li>Q3 reports published</li><li>New market entry in Japan</li><li>Updated revenue forecasts</li></ul>",
    hover_color="#f1f5f9"
)

dashboard.to_html(os.path.join(os.path.dirname(__file__), "output.html"))
print("Generated output.html")
