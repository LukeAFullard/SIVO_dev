from sivo import Sivo
import os

def build_saas_dashboard():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "sleek_bento_stats_2026.svg"
    )
    output_dir = os.path.dirname(__file__)

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=True,
        lock_canvas=True,
        theme="dark"
    )

    app.apply_template_style("dark_mode")

    # Header
    app.fill_template_zone("header-subtitle-placeholder", "Q4 METRICS", font_size=14, font_weight="600", color="#94a3b8")
    app.fill_template_zone("header-title-placeholder", "SaaS Growth Dashboard", font_size=40, font_weight="800", color="#f8fafc")

    # Hero Card
    app.fill_template_zone("hero-label-placeholder", "Annual Recurring Revenue", font_size=18, font_weight="700", color="#cbd5e1")
    app.fill_template_zone("hero-value-placeholder", "$12.4M", font_size=64, font_weight="800", color="#f8fafc")
    app.fill_template_zone("hero-trend-text-placeholder", "+22.5%", font_size=14, font_weight="700", color="#16a34a", align="center")

    # Top Right Card
    app.fill_template_zone("top-right-label-placeholder", "Active Subscriptions", font_size=16, font_weight="700", color="#cbd5e1")
    app.fill_template_zone("top-right-value-placeholder", "42,800", font_size=48, font_weight="800", color="#f8fafc")

    # Middle Right Card
    app.fill_template_zone("mid-right-label-placeholder", "Trial Conversion", font_size=16, font_weight="700", color="#cbd5e1")
    app.fill_template_zone("mid-right-value-placeholder", "14.2%", font_size=48, font_weight="800", color="#f8fafc")
    app.fill_template_zone("mid-trend-text-placeholder", "+3.1%", font_size=14, font_weight="700", color="#16a34a", align="center")

    # Bottom Cards
    app.fill_template_zone("bottom-left-label-placeholder", "Churn Rate", font_size=16, font_weight="600", color="#94a3b8")
    app.fill_template_zone("bottom-left-value-placeholder", "2.1%", font_size=36, font_weight="800", color="#f8fafc")

    app.fill_template_zone("bottom-center-label-placeholder", "Avg Revenue Per User", font_size=16, font_weight="600", color="#94a3b8")
    app.fill_template_zone("bottom-center-value-placeholder", "$240/mo", font_size=36, font_weight="800", color="#f8fafc")

    app.fill_template_zone("bottom-right-label-placeholder", "NPS Score", font_size=16, font_weight="600", color="#94a3b8")
    app.fill_template_zone("bottom-right-value-placeholder", "76", font_size=36, font_weight="800", color="#f8fafc")

    # Interactive Maps
    app.map_bar_chart(
        element_id="bento-hero",
        title="ARR Growth by Quarter",
        categories=["Q1", "Q2", "Q3", "Q4"],
        data=[8.2, 9.5, 11.1, 12.4],
        color="#3b82f6",
        tooltip="Click to view quarterly ARR growth ($M)",
        panel_position="right"
    )

    app.map_pie_chart(
        element_id="bento-top-right",
        title="Subscriptions by Plan",
        data=[
            {"name": "Starter", "value": 18500},
            {"name": "Pro", "value": 15200},
            {"name": "Enterprise", "value": 9100}
        ],
        color=["#94a3b8", "#3b82f6", "#8b5cf6"],
        tooltip="Click to view subscription plan breakdown",
        panel_position="right"
    )

    app.map_gauge_chart(
        element_id="bento-bottom-right",
        title="Net Promoter Score",
        value=76,
        max_value=100,
        color="#10b981",
        tooltip="Click to see customer satisfaction metrics",
        panel_position="left"
    )

    output_path = os.path.join(output_dir, "saas_dashboard.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    build_saas_dashboard()