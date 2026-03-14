from sivo import Sivo
import os

# 1. Build the Dashboard Infographic using the new from_template method
dashboard = Sivo.from_template("dashboard")

# --- Overlays on Dashboard ---
# Header overlay
header_html = """
<div style="text-align: center; width: 1120px;">
    <h1 style="margin: 0; color: #333; font-family: sans-serif; font-size: 32px; padding-top: 20px;">Global Sales Overview 2024</h1>
    <p style="margin: 5px 0 0 0; color: #666; font-family: sans-serif; font-size: 16px;">Interactive Business Intelligence Dashboard</p>
</div>
"""
dashboard.add_overlay("header_area", header_html)

# Key Metrics overlays
metric1_html = """
<div style="text-align: center; width: 350px;">
    <h3 style="margin: 0; color: #888; font-family: sans-serif; font-size: 18px; padding-top: 30px;">Total Revenue</h3>
    <p style="margin: 10px 0 0 0; color: #2ecc71; font-family: sans-serif; font-size: 48px; font-weight: bold;">$12.5M</p>
</div>
"""
dashboard.add_overlay("metric_1", metric1_html)

metric2_html = """
<div style="text-align: center; width: 350px;">
    <h3 style="margin: 0; color: #888; font-family: sans-serif; font-size: 18px; padding-top: 30px;">Active Users</h3>
    <p style="margin: 10px 0 0 0; color: #3498db; font-family: sans-serif; font-size: 48px; font-weight: bold;">84,290</p>
</div>
"""
dashboard.add_overlay("metric_2", metric2_html)

metric3_html = """
<div style="text-align: center; width: 350px;">
    <h3 style="margin: 0; color: #888; font-family: sans-serif; font-size: 18px; padding-top: 30px;">Growth Rate</h3>
    <p style="margin: 10px 0 0 0; color: #e74c3c; font-family: sans-serif; font-size: 48px; font-weight: bold;">+14%</p>
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
    tooltip="Click to view full sales chart",
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
    tooltip="View regional breakdown",
    echarts_option=sidebar_chart_option,
    hover_color="#f1f5f9"
)

# Another interactive widget (e.g., Markdown/Info)
dashboard.map(
    element_id="sidebar_area_bottom",
    tooltip="Recent Updates",
    html="<h3>Recent Updates</h3><ul><li>Q3 reports published</li><li>New market entry in Japan</li><li>Updated revenue forecasts</li></ul>",
    hover_color="#f1f5f9"
)

dashboard.to_html(os.path.join(os.path.dirname(__file__), "dashboard_infographic.html"))
print("Generated dashboard_infographic.html")

# 2. Build the Timeline Infographic using the new from_template method
timeline = Sivo.from_template("timeline")

header_html2 = """
<div style="text-align: center; width: 900px;">
    <h1 style="margin: 0; color: #1e293b; font-family: sans-serif; font-size: 32px; padding-top: 30px;">Project Milestone History</h1>
    <p style="margin: 5px 0 0 0; color: #64748b; font-family: sans-serif; font-size: 16px;">Key events over the last two years</p>
</div>
"""
timeline.add_overlay("header_area", header_html2)

# Add text overlays to timeline nodes
for i, date in enumerate(["Q1 2023", "Q3 2023", "Q1 2024", "Q4 2024"], 1):
    html = f"""
    <div style="text-align: center; width: 350px; padding: 20px;">
        <h3 style="margin: 0; color: #3b82f6; font-family: sans-serif;">{date}</h3>
        <p style="color: #475569; font-family: sans-serif; font-size: 14px;">Milestone {i}: Project Phase {i} Launch</p>
        <button style="margin-top: 10px; padding: 5px 15px; border: none; background: #e2e8f0; border-radius: 4px; cursor: pointer;">View Details</button>
    </div>
    """
    timeline.add_overlay(f"node_{i}_card", html)

    # Map interactivity to the node dot
    timeline.map(
        element_id=f"node_{i}_dot",
        tooltip=f"Expand details for {date}",
        html=f"<h3>{date} Details</h3><p>Extensive details for milestone phase {i}...</p><p>Resources allocated: {i*50}h</p>",
        hover_color="#60a5fa",
        glow=True
    )
    # Also make the card interactive
    timeline.map(
        element_id=f"node_{i}_card",
        tooltip="Click to view",
        html=f"<h3>{date} Details</h3><p>Extensive details for milestone phase {i}...</p>",
        hover_color="#f8fafc"
    )

timeline.to_html(os.path.join(os.path.dirname(__file__), "timeline_infographic.html"))
print("Generated timeline_infographic.html")
