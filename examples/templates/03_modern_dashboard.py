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
    # Using add_overlay to put the chart directly on metric_2
    metric_2_stacked_bar = """
    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 2cqh; container-type: size;">
        <span style="font-family: sans-serif; font-size: 8cqh; font-weight: 700; color: #64748b; margin-bottom: 2cqh;">Energy Mix (%)</span>
        <div style="width: 80cqw; height: 15cqh; display: flex; border-radius: 4px; overflow: hidden; margin-bottom: 1cqh;">
            <div style="width: 40%; background-color: #fbbf24;" title="Solar: 40%"></div>
            <div style="width: 35%; background-color: #60a5fa;" title="Wind: 35%"></div>
            <div style="width: 25%; background-color: #94a3b8;" title="Fossil: 25%"></div>
        </div>
        <div style="display: flex; gap: 4cqw; font-family: sans-serif; font-size: 6cqh; color: #64748b;">
            <span style="display: flex; align-items: center; gap: 1cqw;"><span style="width: 2cqw; height: 2cqw; background: #fbbf24;"></span> Solar</span>
            <span style="display: flex; align-items: center; gap: 1cqw;"><span style="width: 2cqw; height: 2cqw; background: #60a5fa;"></span> Wind</span>
            <span style="display: flex; align-items: center; gap: 1cqw;"><span style="width: 2cqw; height: 2cqw; background: #94a3b8;"></span> Fossil</span>
        </div>
    </div>
    """
    app.add_overlay("metric_2", metric_2_stacked_bar)

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
            "symbolSize": 15,
            "itemStyle": {
                "color": "rgba(239, 68, 68, 0.6)",
                "shadowBlur": 10,
                "shadowColor": "rgba(239, 68, 68, 0.5)"
            },
            "tooltip": {
                "formatter": "{b}: {c}kt CO2e"
            }
        }, {
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
    # Embedded Donut Chart via SVG directly
    donut_html = """
    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; container-type: size;">
        <span style="font-family: sans-serif; font-size: 8cqh; font-weight: 700; color: #1e293b; margin-bottom: 2cqh;">Global Waste Diversion</span>
        <svg width="40cqw" height="40cqw" viewBox="0 0 32 32">
            <!-- Recycled 58% -->
            <circle r="16" cx="16" cy="16" fill="#3b82f6" stroke-width="32" stroke-dasharray="58 100" />
            <!-- Composted 14% -->
            <circle r="16" cx="16" cy="16" fill="#10b981" stroke-width="32" stroke-dasharray="14 100" stroke-dashoffset="-58" />
            <!-- Landfill 28% -->
            <circle r="16" cx="16" cy="16" fill="#94a3b8" stroke-width="32" stroke-dasharray="28 100" stroke-dashoffset="-72" />
            <!-- Inner hole for donut -->
            <circle r="8" cx="16" cy="16" fill="#ffffff" />
        </svg>
        <div style="display: flex; gap: 4cqw; font-family: sans-serif; font-size: 6cqh; color: #64748b; margin-top: 2cqh;">
            <span style="display: flex; align-items: center; gap: 1cqw;"><span style="width: 2cqw; height: 2cqw; background: #3b82f6;"></span> Recycled</span>
            <span style="display: flex; align-items: center; gap: 1cqw;"><span style="width: 2cqw; height: 2cqw; background: #10b981;"></span> Composted</span>
        </div>
    </div>
    """
    app.infographic.overlays["anchor_sidebar_top"] = {
        "html": donut_html,
        "coord": [810 + 350/2, 340 + 200/2],
        "bbox": [810, 340, 810+350, 340+200],
        "offset": [0, 0],
        "scale_with_zoom": False
    }

    # Sidebar Area Bottom: Water Usage Trend
    # Embedded Multi-series Line Chart via SVG
    line_html = """
    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 4cqh; container-type: size;">
        <span style="font-family: sans-serif; font-size: 8cqh; font-weight: 700; color: #1e293b; align-self: flex-start; margin-left: 10cqw;">Water Consumption (M Gal)</span>
        <svg width="80cqw" height="40cqh" viewBox="0 0 100 50" preserveAspectRatio="none">
            <!-- Grid lines -->
            <line x1="0" y1="25" x2="100" y2="25" stroke="#e2e8f0" stroke-width="1" />
            <line x1="0" y1="50" x2="100" y2="50" stroke="#cbd5e1" stroke-width="1" />

            <!-- 2025 (Dashed) -->
            <polyline points="0,30 25,28 50,20 75,18 100,25" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4" />
            <!-- 2026 (Solid with Area) -->
            <polyline points="0,35 25,38 50,30 75,25 100,38" fill="none" stroke="#0ea5e9" stroke-width="3" />
            <polygon points="0,35 25,38 50,30 75,25 100,38 100,50 0,50" fill="rgba(14, 165, 233, 0.2)" />
        </svg>
    </div>
    """
    app.infographic.overlays["anchor_sidebar_bottom"] = {
        "html": line_html,
        "coord": [810 + 350/2, 560 + 200/2],
        "bbox": [810, 560, 810+350, 560+200],
        "offset": [0, 0],
        "scale_with_zoom": False
    }

    output_path = os.path.join(os.path.dirname(__file__), "03_modern_dashboard.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
