from sivo import Sivo
import os

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
        "src", "sivo", "templates", "16_10", "layered_pyramid_2026.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="digital_first_glassmorphism",
        ambient_effect="particles"
    )

    # Title overrides
    app.fill_template_zone("main-title", "Sales Funnel Architecture", font_size="120%", font_weight="800", color="#f8fafc")
    app.fill_template_zone("sub-title", "Q4 2026 Conversion Metrics", font_size="100%", color="#adb5bd")

    # Map interactions and data to Pyramid Tiers
    app.map("tier-1",
            color="rgba(157, 78, 221, 0.4)",
            border_color="#9d4edd",
            border_width=2,
            tooltip="Awareness Stage",
            panel_position="right",
            markdown="### Top of Funnel: Awareness\n\n- Total Reach: 1.2M\n- Ad Spend: $50k\n- CTR: 3.2%\n\nOur initial touchpoints focus on broad market education and brand visibility."
    )
    app.fill_template_zone("text-tier-1", "Awareness (1.2M)", color="#f8fafc", font_weight="bold")

    app.map("tier-2",
            color="rgba(57, 255, 20, 0.4)",
            border_color="#39ff14",
            border_width=2,
            tooltip="Consideration Stage",
            panel_position="right",
            markdown="### Consideration\n\n- Engaged Users: 450k\n- Webinar Signups: 12k\n- Resource Downloads: 85k"
    )
    app.fill_template_zone("text-tier-2", "Consideration (450k)", color="#f8fafc", font_weight="bold")

    app.map("tier-3",
            color="rgba(14, 165, 233, 0.4)",
            border_color="#0ea5e9",
            border_width=2,
            tooltip="Intent Stage",
            panel_position="right",
            markdown="### Intent & Evaluation\n\n- Demo Requests: 5k\n- Sales Calls: 1.2k\n- Proposal Sent: 800"
    )
    app.fill_template_zone("text-tier-3", "Intent (5k)", color="#f8fafc", font_weight="bold")

    app.map("tier-4",
            color="rgba(239, 68, 68, 0.4)",
            border_color="#ef4444",
            border_width=2,
            tooltip="Conversion Stage",
            panel_position="right",
            markdown="### Conversion (Closed Won)\n\n- New Logos: 150\n- Total ACV: $4.5M\n- Win Rate: 18.75%"
    )
    app.fill_template_zone("text-tier-4", "Conversion (150)", color="#f8fafc", font_weight="bold")

    # Map data and charts to Bento Boxes

    # Bento 1: Traffic Sources (Donut Chart)
    app.add_scalable_text("bento-1", "TRAFFIC SOURCES", left="10%", top="10%", width="80%", height="15%", font_size="10%", font_weight="700", color="#adb5bd")
    app.map_pie_chart("bento-1",
                      title="",
                      data=[
                          {"name": "Organic Search", "value": 45},
                          {"name": "Paid Ads", "value": 30},
                          {"name": "Social", "value": 15},
                          {"name": "Referral", "value": 10}
                      ],
                      color=["#9d4edd", "#39ff14", "#0ea5e9", "#ef4444"],
                      extra_options={
                          "backgroundColor": "transparent",
                          "series": [{"radius": ["50%", "70%"], "center": ["50%", "60%"]}]
                      })

    # Bento 2: Conversion Rate Trend (Line Chart)
    app.add_scalable_text("bento-2", "CONVERSION RATE", left="10%", top="10%", width="80%", height="15%", font_size="10%", font_weight="700", color="#adb5bd")
    app.map_line_chart("bento-2",
                       title="",
                       categories=["Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                       data=[2.1, 2.3, 2.8, 3.2, 3.5, 4.1],
                       color=["#39ff14"],
                       extra_options={
                           "backgroundColor": "transparent",
                           "grid": {"top": "30%", "bottom": "15%", "left": "15%", "right": "10%"},
                           "series": [{"areaStyle": {}}]
                       })

    # Bento 3: Key Metric Overlay
    app.add_scalable_text("bento-3", "CAC", left="10%", top="15%", width="80%", height="15%", font_size="12%", font_weight="700", color="#adb5bd")
    app.add_scalable_text("bento-3", "$850", left="10%", top="35%", width="80%", height="35%", font_size="35%", font_weight="900", color="#9d4edd")
    app.add_scalable_text("bento-3", "▼ -12% vs last quarter", left="10%", top="75%", width="80%", height="10%", font_size="8%", font_weight="600", color="#39ff14")

    # Bento 4: MQL to SQL Conversion Gauge
    app.add_scalable_text("bento-4", "MQL to SQL", left="10%", top="10%", width="80%", height="15%", font_size="12%", font_weight="700", color="#adb5bd")
    gauge_html = """
    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 5cqh; container-type: size;">
        <svg width="40cqw" height="20cqw" viewBox="0 0 100 50">
            <path d="M 10 50 A 40 40 0 0 1 90 50" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="12" stroke-linecap="round" />
            <path d="M 10 50 A 40 40 0 0 1 70 15" fill="none" stroke="#0ea5e9" stroke-width="12" stroke-linecap="round" />
            <text x="50" y="45" font-family="sans-serif" font-size="20" font-weight="bold" fill="#f8fafc" text-anchor="middle">42%</text>
        </svg>
    </div>
    """
    app.add_overlay("bento-4", gauge_html)

    output_path = os.path.join(os.path.dirname(__file__), "layered_pyramid.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
