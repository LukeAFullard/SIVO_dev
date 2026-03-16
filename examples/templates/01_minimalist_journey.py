from sivo import Sivo
import os

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "minimalist_journey_flow_2026.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="light"
    )

    # Make sure text is visible (dark text on light background)

    # Header
    app.fill_template_zone("header-subtitle-placeholder", "E-Commerce Funnel Optimization", font_size="100%", color="#3b82f6", font_weight="700")
    app.fill_template_zone("header-title-placeholder", "Customer Lifecycle Journey", font_size="100%", font_weight="900", color="#0f172a")

    # Node 1: Discovery (Completed Phase)
    app.fill_template_zone("node-1-step-placeholder", "1. Discovery", font_size="100%", font_weight="800", color="#1e293b", align="left")
    app.fill_template_zone("node-1-desc-1-placeholder", "SEO & Social Campaigns", font_size="100%", font_weight="600", color="#64748b", align="left")
    app.fill_template_zone("node-1-desc-2-placeholder", "1.2M Impressions", font_size="100%", font_weight="800", color="#10b981", align="left")

    # Node 2: Engagement (Active Phase)
    app.fill_template_zone("node-2-step-placeholder", "2. Engagement", font_size="100%", font_weight="800", color="#1e293b", align="left")
    app.fill_template_zone("node-2-desc-1-placeholder", "Traffic Sources", font_size="100%", font_weight="600", color="#64748b", align="left")
    app.fill_template_zone("node-2-desc-2-placeholder", "Bounce Rate: 42%", font_size="100%", font_weight="700", color="#f59e0b", align="left")

    # Native ECharts Bar Chart mapped to the interaction box
    app.map_bar_chart(
        element_id="node-2-card",
        title="",
        categories=["Organic", "Paid", "Referral", "Direct"],
        data=[450, 320, 150, 80],
        color="#3b82f6",
        axis_color="#64748b",
        extra_options={"grid": {"top": 10, "bottom": 30, "left": 40, "right": 20}, "backgroundColor": "transparent"}
    )

    # Node 3: Conversion (Active Phase)
    app.fill_template_zone("node-3-step-placeholder", "3. Conversion", font_size="100%", font_weight="800", color="#1e293b", align="left")
    app.fill_template_zone("node-3-desc-1-placeholder", "Checkout Completion", font_size="100%", font_weight="600", color="#64748b", align="left")
    app.fill_template_zone("node-3-desc-2-placeholder", "Target: 5.0%", font_size="100%", font_weight="700", color="#94a3b8", align="left")

    app.add_scalable_text("node-3-card", "CONVERSION RATE", left="0%", top="30%", width="100%", height="15%", font_size="12%", font_weight="700", color="#64748b", align="center")
    app.add_scalable_text("node-3-card", "4.8%", left="0%", top="45%", width="100%", height="30%", font_size="35%", font_weight="900", color="#10b981", align="center")
    app.add_scalable_progress_bar("node-3-card", progress="96%", left="10%", top="85%", width="80%", height="5%", rx="4", bg_color="#e2e8f0", fill_color="#10b981")


    # Node 4: Retention (Upcoming Phase)
    app.fill_template_zone("node-4-step-placeholder", "4. Retention", font_size="100%", font_weight="800", color="#1e293b", align="left")
    app.fill_template_zone("node-4-desc-1-placeholder", "Monthly Active Users", font_size="100%", font_weight="600", color="#64748b", align="left")
    app.fill_template_zone("node-4-desc-2-placeholder", "10,240 DAU", font_size="100%", font_weight="800", color="#3b82f6", align="left")

    app.add_scalable_text("node-4-step-placeholder", "RENEWAL RATE", left="0%", top="200%", width="100%", height="100%", font_size="80%", font_weight="700", color="#94a3b8", align="left")
    app.add_scalable_text("node-4-step-placeholder", "88.4%", left="0%", top="300%", width="100%", height="200%", font_size="180%", font_weight="900", color="#8b5cf6", align="left")

    # Node 5: Advocacy (Future Phase)
    app.fill_template_zone("node-5-step-placeholder", "5. Advocacy", font_size="100%", font_weight="800", color="#1e293b", align="left")
    app.fill_template_zone("node-5-desc-1-placeholder", "Net Promoter Score", font_size="100%", font_weight="600", color="#64748b", align="left")
    app.fill_template_zone("node-5-desc-2-placeholder", "Score: +64", font_size="100%", font_weight="800", color="#10b981", align="left")

    # Add a donut chart to Node 5 card area
    # The SVG doesn't have node-5-card explicitly named, but we can map it near the placeholders
    app.map_pie_chart(
        element_id="node-5-step-placeholder",
        title="",
        data=[
            {"name": "Promoters", "value": 75},
            {"name": "Passives", "value": 15},
            {"name": "Detractors", "value": 10}
        ],
        extra_options={
            "series": [{"radius": ["50%", "80%"], "center": ["50%", "450%"]}],
            "color": ["#10b981", "#fbbf24", "#ef4444"],
            "backgroundColor": "transparent"
        }
    )

    output_path = os.path.join(os.path.dirname(__file__), "01_minimalist_journey.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
