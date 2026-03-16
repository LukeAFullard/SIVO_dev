from sivo import Sivo
import os
import lxml.etree as etree

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "bento_grid_dashboard_2026.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="dark", # Premium dark mode
        ambient_effect="stars"
    )

    # Change background to dark manually if theme doesn't hit everything
    # Map to classes isn't standard, we'll assume the theme="dark" is enough, or map to nothing
    app.map("card-main", color="#1e293b", border_color="#334155", border_width=1)
    app.map("rect-users", color="#1e293b", border_color="#334155", border_width=1)
    app.map("rect-conversion", color="#1e293b", border_color="#334155", border_width=1)
    app.map("card-engagement", color="#1e293b", border_color="#334155", border_width=1)
    app.map("card-bounce", color="#1e293b", border_color="#334155", border_width=1)
    app.map("card-satisfaction", color="#1e293b", border_color="#334155", border_width=1)

    # Header
    app.fill_template_zone("text_performance_overview", "Global Supply Chain Command Center", font_size="100%", font_weight="900", color="#f8fafc")
    app.fill_template_zone("text_q3_2026_analytics_dashboard", "Real-time Fleet Tracking & Logistics Intelligence • LIVE", font_size="100%", color="#94a3b8")

    # Card Main: Global Map - High Fidelity Map
    app.map_nested_map_chart(
        element_id="card-main",
        title="Active Maritime Cargo Routes & Congestion",
        map_name="world",
        map_data="world",
        data=[
            {"name": "United States", "value": 1500},
            {"name": "China", "value": 3400},
            {"name": "Germany", "value": 1100},
            {"name": "Brazil", "value": 800},
            {"name": "Australia", "value": 1400},
            {"name": "South Africa", "value": 600},
            {"name": "India", "value": 2100}
        ],
        min_val=0,
        max_val=4000,
        title_size=18,
        title_color="#f8fafc",
        color=["#0ea5e9", "#2563eb", "#3b82f6", "#1d4ed8", "#1e40af", "#1e3a8a"], # Deep sea blues
        extra_options={
            "backgroundColor": "transparent",
            "geo": {
                "itemStyle": {
                    "areaColor": "#334155",
                    "borderColor": "#475569"
                },
                "emphasis": {
                    "itemStyle": {
                        "areaColor": "#64748b"
                    }
                }
            }
        }
    )

    # Card Users: Fleet Efficiency (Radar Chart)
    app.add_scalable_text("rect-users", "FLEET PERFORMANCE MATRIX", left="8%", top="10%", width="80%", height="15%", font_size="12%", font_weight="700", color="#94a3b8")

    app.map_radar_chart(
        element_id="rect-users",
        title="",
        indicators=[
            {"name": "On-Time", "max": 100},
            {"name": "Fuel Eff", "max": 100},
            {"name": "Maint", "max": 100},
            {"name": "Safety", "max": 100},
            {"name": "Capacity", "max": 100}
        ],
        data=[
            {"value": [94, 85, 90, 98, 88], "name": "Current Fleet Avg"}
        ],
        color="#10b981",
        extra_options={
            "radar": {
                "center": ["50%", "60%"],
                "radius": "65%",
                "axisName": {"color": "#cbd5e1", "fontSize": 10},
                "splitLine": {"lineStyle": {"color": "#334155"}},
                "splitArea": {"show": False},
                "axisLine": {"lineStyle": {"color": "#334155"}}
            },
            "series": [{"areaStyle": {"opacity": 0.3}}],
            "backgroundColor": "transparent"
        }
    )

    # Card Conversion: Critical Alert System
    app.add_scalable_text("rect-conversion", "PORT CONGESTION ALERT", left="10%", top="15%", width="50%", height="15%", font_size="12%", font_weight="800", color="#ef4444")
    app.add_scalable_text("rect-conversion", "Severe delays at Port of Long Beach. Average wait time increased to 8.4 days. AI rerouting protocols active.", left="10%", top="35%", width="50%", height="40%", font_size="10%", font_weight="600", color="#e2e8f0", auto_shrink=True)

    # Custom HTML Overlay for a glowing alert status
    alert_html = """
    <div style='width: 100%; height: 100%; display: flex; align-items: center; justify-content: flex-end; padding-right: 10%; box-sizing: border-box; container-type: size;'>
        <div style='display: flex; flex-direction: column; align-items: center;'>
            <div style='width: 15cqh; height: 15cqh; background-color: #ef4444; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 20px rgba(239, 68, 68, 0.6); animation: pulse 2s infinite;'>
                <span style='color: white; font-family: sans-serif; font-size: 8cqh; font-weight: bold;'>!</span>
            </div>
            <span style='color: #ef4444; font-family: sans-serif; font-size: 5cqh; font-weight: bold; margin-top: 1cqh; letter-spacing: 1px;'>CRITICAL</span>
            <style>
                @keyframes pulse {
                    0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
                    70% { transform: scale(1.1); box-shadow: 0 0 0 10px rgba(239, 68, 68, 0); }
                    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
                }
            </style>
        </div>
    </div>
    """
    app.add_overlay("rect-conversion", alert_html)


    # Bottom Cards
    # Card 1: Revenue / Freight Value
    app.add_scalable_text("card-engagement", "IN-TRANSIT VALUE", left="10%", top="20%", width="80%", height="15%", font_size="12%", font_weight="700", color="#94a3b8")
    app.add_scalable_text("card-engagement", "$4.2B", left="10%", top="40%", width="80%", height="35%", font_size="40%", font_weight="900", color="#3b82f6")
    app.add_scalable_text("card-engagement", "▲ +3.2% vs last week", left="10%", top="75%", width="80%", height="10%", font_size="8%", font_weight="600", color="#10b981")

    # Card 2: Shipments Trend (Area Chart)
    app.add_scalable_text("card-bounce", "WEEKLY CARGO VOL", left="10%", top="10%", width="80%", height="15%", font_size="12%", font_weight="700", color="#94a3b8")

    app.map_line_chart(
        element_id="card-bounce",
        title="",
        categories=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        data=[1200, 1350, 1100, 1500, 1800, 900, 800],
        color="#8b5cf6",
        smooth=True,
        extra_options={
            "grid": {"top": 40, "bottom": 30, "left": 40, "right": 20},
            "backgroundColor": "transparent",
            "xAxis": {"axisLine": {"lineStyle": {"color": "#475569"}}, "axisLabel": {"color": "#cbd5e1"}},
            "yAxis": {"splitLine": {"lineStyle": {"color": "#334155"}}, "axisLabel": {"color": "#cbd5e1"}},
            "series": [{"areaStyle": {
                "color": {
                    "type": "linear", "x": 0, "y": 0, "x2": 0, "y2": 1,
                    "colorStops": [{"offset": 0, "color": "rgba(139, 92, 246, 0.8)"}, {"offset": 1, "color": "rgba(139, 92, 246, 0.1)"}]
                }
            }}]
        }
    )

    # Card 3: Emissions Tracker (Gauge)
    app.add_scalable_text("card-satisfaction", "CARBON TARGET (MTD)", left="10%", top="10%", width="80%", height="15%", font_size="12%", font_weight="700", color="#94a3b8")

    app.map_gauge_chart(
        element_id="card-satisfaction",
        title="Quota Used",
        value=68,
        color="#10b981",
        extra_options={
            "series": [{
                "center": ["50%", "65%"], "radius": "80%",
                "startAngle": 180, "endAngle": 0,
                "axisLine": {"lineStyle": {"width": 15, "color": [[0.7, "#10b981"], [0.9, "#f59e0b"], [1, "#ef4444"]]}},
                "pointer": {"itemStyle": {"color": "#cbd5e1"}},
                "detail": {"fontSize": 20, "fontWeight": "bold", "color": "#f8fafc", "formatter": "{value}%", "offsetCenter": [0, "-20%"]}
            }],
            "backgroundColor": "transparent"
        }
    )

    output_path = os.path.join(os.path.dirname(__file__), "02_bento_grid.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
