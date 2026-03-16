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

    # Custom HTML Overlay for a Funnel directly on Node 1
    node_1_funnel = """
    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 2cqh; gap: 2px; container-type: size;">
        <div style="width: 15cqw; height: 3cqh; background-color: #93c5fd; border-radius: 2px;"></div>
        <div style="width: 12cqw; height: 3cqh; background-color: #60a5fa; border-radius: 2px;"></div>
        <div style="width: 8cqw; height: 3cqh; background-color: #3b82f6; border-radius: 2px;"></div>
        <div style="width: 4cqw; height: 3cqh; background-color: #1d4ed8; border-radius: 2px;"></div>
    </div>
    """
    app.add_overlay("node-1-card", node_1_funnel)
    app.map("node-1-card", tooltip="<b>Phase 1:</b> Initial lead generation and qualification through automated marketing channels.", glow=True, hover_color="#f8fafc")

    # Node 2: Qualification
    app.fill_template_zone("node-2-step-placeholder", "2. Qualification", font_size="100%", font_weight="800", color="#1e293b", align="left")
    app.fill_template_zone("node-2-desc-1-placeholder", "Sales Accepted Leads (SAL)", font_size="100%", font_weight="600", color="#64748b", align="left")
    app.fill_template_zone("node-2-desc-2-placeholder", "Conversion Rate: 12%", font_size="100%", font_weight="700", color="#f59e0b", align="left")

    # Custom HTML Overlay for a Gauge Chart directly on Node 2
    node_2_gauge = """
    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 2cqh; container-type: size;">
        <svg width="20cqw" height="10cqw" viewBox="0 0 100 50">
            <!-- Background Arc -->
            <path d="M 10 50 A 40 40 0 0 1 90 50" fill="none" stroke="#e2e8f0" stroke-width="15" stroke-linecap="round" />
            <!-- Foreground Arc (Value) -->
            <path d="M 10 50 A 40 40 0 0 1 70 20" fill="none" stroke="#f59e0b" stroke-width="15" stroke-linecap="round" />
            <text x="50" y="45" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1e293b" text-anchor="middle">78</text>
        </svg>
    </div>
    """
    app.add_overlay("node-2-card", node_2_gauge)
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

    # Note: For node-4, we can't easily overlay onto step-placeholder because it's tiny. We'll map the tooltip only.
    app.map("node-4-step-placeholder", tooltip="<b>Phase 4:</b> Customer Success drives upsells and cross-sells, increasing customer lifetime value.", hover_color="#f8fafc")


    # Node 5: Renewals
    app.fill_template_zone("node-5-step-placeholder", "5. Renewals", font_size="100%", font_weight="800", color="#1e293b", align="left")
    app.fill_template_zone("node-5-desc-1-placeholder", "Gross Retention Rate", font_size="100%", font_weight="600", color="#64748b", align="left")
    app.fill_template_zone("node-5-desc-2-placeholder", "Q4 Cohort", font_size="100%", font_weight="800", color="#10b981", align="left")

    # Map side panel action just for demonstration of both approaches
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
    app.map("node-5-step-placeholder", tooltip="<b>Phase 5:</b> Renewal rates are strong. At-risk accounts are actively managed by the CS team.<br/><i>(Click to view details in panel)</i>", hover_color="#f8fafc")

    output_path = os.path.join(os.path.dirname(__file__), "01_minimalist_journey.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
