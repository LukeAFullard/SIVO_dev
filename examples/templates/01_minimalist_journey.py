from sivo import Sivo
import os
import lxml.etree as etree

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "minimalist_journey_flow_2026.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="light",
        ambient_effect="stars" # Premium touch
    )

    # Header - Advanced Typography
    app.fill_template_zone("header-subtitle-placeholder", "Enterprise SaaS Revenue Operations", font_size="100%", color="#6366f1", font_weight="800")
    app.fill_template_zone("header-title-placeholder", "B2B Customer Acquisition & LTV Funnel", font_size="100%", font_weight="900", color="#0f172a")

    # Node 1: Lead Gen
    app.fill_template_zone("node-1-step-placeholder", "1. MQL Generation", font_size="100%", font_weight="800", color="#1e293b", align="left")
    app.fill_template_zone("node-1-desc-1-placeholder", "Inbound & Outbound Sourced", font_size="100%", font_weight="600", color="#64748b", align="left")
    app.fill_template_zone("node-1-desc-2-placeholder", "Volume: 45,000", font_size="100%", font_weight="800", color="#10b981", align="left")

    # Advanced ECharts: Custom Funnel mapped to interaction box
    app.map_funnel_chart(
        element_id="node-1-card",
        title="Pipeline Velocity",
        data=[
            {"name": "Awareness", "value": 100},
            {"name": "Interest", "value": 60},
            {"name": "Consideration", "value": 30},
            {"name": "Intent", "value": 10}
        ],
        extra_options={
            "series": [{
                "left": "10%", "top": "25%", "bottom": "10%", "width": "80%",
                "label": {"show": True, "position": "inside", "color": "#fff", "fontWeight": "bold"},
                "itemStyle": {"borderColor": "#fff", "borderWidth": 2},
                "emphasis": {"label": {"fontSize": 14}}
            }],
            "color": ["#93c5fd", "#60a5fa", "#3b82f6", "#1d4ed8"],
            "title": {"textStyle": {"fontSize": 12, "color": "#64748b", "fontWeight": "600"}},
            "backgroundColor": "transparent"
        }
    )
    app.map("node-1-card", tooltip="<b>Phase 1:</b> Initial lead generation and qualification through automated marketing channels.", glow=True, hover_color="#f8fafc")

    # Node 2: Qualification
    app.fill_template_zone("node-2-step-placeholder", "2. Qualification", font_size="100%", font_weight="800", color="#1e293b", align="left")
    app.fill_template_zone("node-2-desc-1-placeholder", "Sales Accepted Leads (SAL)", font_size="100%", font_weight="600", color="#64748b", align="left")
    app.fill_template_zone("node-2-desc-2-placeholder", "Conversion Rate: 12%", font_size="100%", font_weight="700", color="#f59e0b", align="left")

    # Advanced ECharts: Gauge Chart
    app.map_gauge_chart(
        element_id="node-2-card",
        title="Lead Quality Score",
        value=78,
        color="#f59e0b",
        extra_options={
            "series": [{
                "center": ["50%", "50%"], "radius": "80%",
                "axisLine": {"lineStyle": {"width": 10, "color": [[0.3, "#ef4444"], [0.7, "#f59e0b"], [1, "#10b981"]]}},
                "pointer": {"itemStyle": {"color": "#1e293b"}},
                "detail": {"fontSize": 16, "fontWeight": "bold", "color": "#1e293b", "formatter": "{value}/100"}
            }],
            "backgroundColor": "transparent"
        }
    )
    app.map("node-2-card", tooltip="<b>Phase 2:</b> BDRs qualify leads based on BANT criteria. Current average score is strong.", hover_color="#f8fafc")


    # Node 3: Conversion
    app.fill_template_zone("node-3-step-placeholder", "3. Closed Won", font_size="100%", font_weight="800", color="#1e293b", align="left")
    app.fill_template_zone("node-3-desc-1-placeholder", "New Enterprise Logos", font_size="100%", font_weight="600", color="#64748b", align="left")
    app.fill_template_zone("node-3-desc-2-placeholder", "Target: $12M ARR", font_size="100%", font_weight="700", color="#94a3b8", align="left")

    app.add_scalable_text("node-3-card", "WIN RATE (Q3)", left="0%", top="20%", width="100%", height="15%", font_size="12%", font_weight="700", color="#64748b", align="center")
    app.add_scalable_text("node-3-card", "24.5%", left="0%", top="35%", width="100%", height="30%", font_size="35%", font_weight="900", color="#10b981", align="center")

    # Custom HTML Overlay for a sleek progress bar inside the card
    progress_html = """
    <div style='width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; padding: 0 10%; box-sizing: border-box; container-type: size;'>
        <div style='display: flex; justify-content: space-between; margin-bottom: 2cqh; font-family: sans-serif;'>
            <span style='font-size: 8cqh; font-weight: 700; color: #64748b;'>$11.5M ARR</span>
            <span style='font-size: 8cqh; font-weight: 700; color: #10b981;'>96% to Target</span>
        </div>
        <div style='width: 100%; height: 6cqh; background-color: #e2e8f0; border-radius: 4px; overflow: hidden;'>
            <div style='width: 96%; height: 100%; background: linear-gradient(90deg, #34d399, #10b981); border-radius: 4px;'></div>
        </div>
    </div>
    """
    app.add_overlay("node-3-card", progress_html, offset_y=30)
    app.map("node-3-card", tooltip="<b>Phase 3:</b> Account Executives close deals. We are currently 96% to our Q3 target.", confetti={"particle_count": 100, "spread": 70}, hover_color="#f8fafc")


    # Node 4: Expansion
    app.fill_template_zone("node-4-step-placeholder", "4. Expansion", font_size="100%", font_weight="800", color="#1e293b", align="left")
    app.fill_template_zone("node-4-desc-1-placeholder", "Net Revenue Retention", font_size="100%", font_weight="600", color="#64748b", align="left")
    app.fill_template_zone("node-4-desc-2-placeholder", "Target: 120%", font_size="100%", font_weight="800", color="#3b82f6", align="left")

    app.add_scalable_text("node-4-step-placeholder", "CURRENT NRR", left="0%", top="200%", width="100%", height="100%", font_size="80%", font_weight="700", color="#94a3b8", align="left")
    app.add_scalable_text("node-4-step-placeholder", "118.2%", left="0%", top="300%", width="100%", height="200%", font_size="180%", font_weight="900", color="#8b5cf6", align="left")

    # Add a line chart showing NRR trend
    app.map_line_chart(
        element_id="node-4-step-placeholder",
        title="",
        categories=["Q1", "Q2", "Q3", "Q4"],
        data=[112, 115, 118, 122],
        color="#8b5cf6",
        smooth=True,
        extra_options={
            "grid": {"top": 150, "bottom": -50, "left": -10, "right": -10}, # Push it down below the text
            "xAxis": {"show": False},
            "yAxis": {"show": False, "min": 100, "max": 130},
            "series": [{"areaStyle": {"opacity": 0.1}}],
            "backgroundColor": "transparent"
        }
    )
    app.map("node-4-step-placeholder", tooltip="<b>Phase 4:</b> Customer Success drives upsells and cross-sells, increasing customer lifetime value.", hover_color="#f8fafc")


    # Node 5: Renewals
    app.fill_template_zone("node-5-step-placeholder", "5. Renewals", font_size="100%", font_weight="800", color="#1e293b", align="left")
    app.fill_template_zone("node-5-desc-1-placeholder", "Gross Retention Rate", font_size="100%", font_weight="600", color="#64748b", align="left")
    app.fill_template_zone("node-5-desc-2-placeholder", "Q4 Cohort", font_size="100%", font_weight="800", color="#10b981", align="left")

    app.map_pie_chart(
        element_id="node-5-step-placeholder",
        title="Account Status",
        data=[
            {"name": "Renewed", "value": 85},
            {"name": "At Risk", "value": 10},
            {"name": "Churn", "value": 5}
        ],
        extra_options={
            "series": [{
                "radius": ["40%", "60%"],
                "center": ["50%", "300%"],
                "label": {"show": True, "position": "outside", "formatter": "{b}\n{d}%", "fontSize": 8}
            }],
            "color": ["#10b981", "#fbbf24", "#ef4444"],
            "title": {"textStyle": {"fontSize": 10, "color": "#64748b", "fontWeight": "700"}, "top": 40},
            "backgroundColor": "transparent"
        }
    )
    app.map("node-5-step-placeholder", tooltip="<b>Phase 5:</b> Renewal rates are strong. At-risk accounts are actively managed by the CS team.", hover_color="#f8fafc")

    output_path = os.path.join(os.path.dirname(__file__), "01_minimalist_journey.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
