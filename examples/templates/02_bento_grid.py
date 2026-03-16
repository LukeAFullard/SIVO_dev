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
    # map_nested_map_chart actually renders ON the SVG element (card-main) because it configures the base geo
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

    # Custom HTML Overlay for Radar/Spider graph on rect-users
    radar_html = """
    <div style="width: 100%; height: 100%; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 2cqh; container-type: size;">
        <svg width="25cqw" height="25cqw" viewBox="0 0 100 100">
            <!-- Grid -->
            <polygon points="50,10 90,40 75,90 25,90 10,40" fill="none" stroke="#334155" stroke-width="1"/>
            <polygon points="50,30 70,45 62,70 38,70 30,45" fill="none" stroke="#334155" stroke-width="1"/>
            <polygon points="50,50 50,50 50,50 50,50 50,50" fill="none" stroke="#334155" stroke-width="1"/>
            <!-- Data -->
            <polygon points="50,15 85,45 70,85 30,80 15,35" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="2"/>
        </svg>
    </div>
    """
    app.add_overlay("rect-users", radar_html)

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

    # Directly embed the area chart via SVG inside add_overlay
    area_html = """
    <div style="width: 100%; height: 100%; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 2cqh; container-type: size;">
        <svg width="80cqw" height="40cqh" viewBox="0 0 100 50" preserveAspectRatio="none">
            <!-- Grid lines -->
            <line x1="0" y1="25" x2="100" y2="25" stroke="#334155" stroke-width="1" stroke-dasharray="2" />
            <line x1="0" y1="50" x2="100" y2="50" stroke="#475569" stroke-width="1" />

            <polyline points="0,40 16,30 33,45 50,20 66,10 83,45 100,40" fill="none" stroke="#8b5cf6" stroke-width="2" />
            <polygon points="0,40 16,30 33,45 50,20 66,10 83,45 100,40 100,50 0,50" fill="rgba(139, 92, 246, 0.2)" />
        </svg>
    </div>
    """
    app.add_overlay("card-bounce", area_html)

    # Card 3: Emissions Tracker (Gauge)
    app.add_scalable_text("card-satisfaction", "CARBON TARGET (MTD)", left="10%", top="10%", width="80%", height="15%", font_size="12%", font_weight="700", color="#94a3b8")

    # Directly embed a gauge chart via SVG
    gauge_html = """
    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 4cqh; container-type: size;">
        <svg width="35cqw" height="17.5cqw" viewBox="0 0 100 50">
            <!-- Background Arc -->
            <path d="M 10 50 A 40 40 0 0 1 90 50" fill="none" stroke="#334155" stroke-width="15" stroke-linecap="round" />
            <!-- Foreground Arc (Value) -->
            <path d="M 10 50 A 40 40 0 0 1 65 15" fill="none" stroke="#10b981" stroke-width="15" stroke-linecap="round" />
            <text x="50" y="45" font-family="sans-serif" font-size="20" font-weight="bold" fill="#f8fafc" text-anchor="middle">68%</text>
        </svg>
    </div>
    """
    app.add_overlay("card-satisfaction", gauge_html)

    output_path = os.path.join(os.path.dirname(__file__), "02_bento_grid.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
