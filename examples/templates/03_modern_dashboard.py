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
        theme="light"
    )

    # Header
    app.add_scalable_text("header_area", "Corporate Sustainability & ESG Dashboard", left="2%", top="20%", width="96%", height="40%", font_size="35%", font_weight="900", color="#0f172a", align="left")
    app.add_scalable_text("header_area", "Global Energy Consumption, Emissions, & Policy Targets • FY2026", left="2%", top="60%", width="96%", height="20%", font_size="15%", font_weight="600", color="#64748b", align="left")

    # Metric 1: Key Metric (Total Reduction)
    app.add_scalable_text("metric_1", "CARBON OFFSET", left="10%", top="20%", width="80%", height="15%", font_size="12%", font_weight="700", color="#64748b")
    app.add_scalable_text("metric_1", "1.2M", left="10%", top="45%", width="80%", height="35%", font_size="35%", font_weight="900", color="#10b981")
    app.add_scalable_text("metric_1", "Tons CO2e Offset YTD", left="10%", top="80%", width="80%", height="10%", font_size="8%", font_weight="600", color="#94a3b8")

    # Metric 2: Renewables Share
    app.map_bar_chart(
        element_id="metric_2",
        title="Renewables Share",
        categories=["Solar", "Wind", "Hydro", "Nuclear", "Other"],
        data=[45, 30, 15, 8, 2],
        color="#3b82f6",
        title_size=16,
        title_color="#334155",
        extra_options={"grid": {"top": 40, "bottom": 30, "left": 40, "right": 20}, "backgroundColor": "transparent"}
    )

    # Metric 3: ESG Score
    app.add_scalable_text("metric_3", "ESG RATING (MSCI)", left="10%", top="20%", width="80%", height="15%", font_size="12%", font_weight="700", color="#64748b")
    app.add_scalable_text("metric_3", "AAA", left="10%", top="45%", width="80%", height="35%", font_size="35%", font_weight="900", color="#8b5cf6")
    app.add_scalable_progress_bar("metric_3", progress="95%", left="10%", top="85%", width="80%", height="5%", rx="4", bg_color="#e2e8f0", fill_color="#8b5cf6")

    # Main Chart Area: Main Center Map
    app.map_nested_map_chart(
        element_id="main_chart_area",
        title="Global CO2 Emissions (Metric Tons per Capita)",
        map_name="world",
        map_data="world",
        data=[
            {"name": "United States", "value": 14.5},
            {"name": "China", "value": 8.1},
            {"name": "Germany", "value": 7.8},
            {"name": "India", "value": 1.9},
            {"name": "Brazil", "value": 2.2},
            {"name": "United Kingdom", "value": 5.2}
        ],
        min_val=0,
        max_val=15,
        title_size=20,
        title_color="#1e293b",
        color=["#f87171", "#fb923c", "#fcd34d", "#34d399", "#10b981"], # Gradient from high (red) to low (green) emissions
        extra_options={"backgroundColor": "transparent"}
    )

    # Sidebar Area Top: Policy Compliance
    app.map_pie_chart(
        element_id="sidebar_area_top",
        title="Facility Compliance",
        data=[
            {"name": "Compliant", "value": 82},
            {"name": "In Review", "value": 12},
            {"name": "At Risk", "value": 6}
        ],
        extra_options={
            "series": [{"radius": ["40%", "70%"]}],
            "color": ["#10b981", "#f59e0b", "#ef4444"],
            "title": {"textStyle": {"fontSize": 16, "color": "#334155"}},
            "backgroundColor": "transparent"
        }
    )

    # Sidebar Area Bottom: Energy Consumption Trend
    app.map_line_chart(
        element_id="sidebar_area_bottom",
        title="Energy vs. Pathway",
        categories=["2021", "2022", "2023", "2024", "2025", "2026"],
        data=[4500, 4300, 4100, 3950, 3800, 3650],
        color="#f59e0b",
        smooth=True,
        title_size=18,
        title_color="#1e293b",
        extra_options={
            "grid": {"top": 50, "bottom": 30, "left": 50, "right": 30},
            "backgroundColor": "transparent"
        }
    )

    output_path = os.path.join(os.path.dirname(__file__), "03_modern_dashboard.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
