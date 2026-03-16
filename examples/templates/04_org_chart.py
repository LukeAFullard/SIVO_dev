from sivo import Sivo
import os
import lxml.etree as etree

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "pyramid_hierarchy_template.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="light",
        ambient_effect="snow"
    )

    # Narrative: Enterprise Cloud Architecture Layers
    app.fill_template_zone("text_hierarchy_details", "Enterprise Data Fabric Architecture", font_size="100%", font_weight="900", color="#0f172a")

    # Tier 1 - Application Layer (Top)
    app.add_scalable_text("poly-tier-1", "APP LAYER", font_size="12%", color="#0f172a", font_weight="900", align="center", top="40%")
    app.add_scalable_text("poly-tier-1", "SaaS, BI, ML", font_size="8%", color="#1e293b", font_weight="600", align="center", top="65%")
    app.map("poly-tier-1", hover_color="#fca5a5", tooltip="<b>Application Layer</b><br>Provides APIs and visualization tools for end-users to consume insights.")

    # Tier 2 - Compute & Analytics
    app.add_scalable_text("poly-tier-2", "COMPUTE ENGINE", font_size="15%", color="#0f172a", font_weight="800", align="center", top="40%")

    # Custom HTML Overlay for a Sparkline directly embedded on Tier 2
    tier_2_sparkline = """
    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 2cqh; container-type: size;">
        <svg width="40cqw" height="15cqh" viewBox="0 0 100 30" preserveAspectRatio="none">
            <polyline points="0,30 20,20 40,25 60,10 80,15 100,0" fill="none" stroke="#d97706" stroke-width="3" />
            <polygon points="0,30 0,30 20,20 40,25 60,10 80,15 100,0 100,30" fill="rgba(217, 119, 6, 0.2)" />
        </svg>
    </div>
    """
    app.add_overlay("poly-tier-2", tier_2_sparkline)
    app.map("poly-tier-2", hover_color="#fde047", tooltip="<b>Compute Layer</b><br>Scalable distributed processing for batch and streaming data.")

    # Tier 3 - Storage & Lakehouse
    app.add_scalable_text("poly-tier-3", "LAKEHOUSE STORAGE", font_size="12%", color="#0f172a", font_weight="800", align="center", top="40%")

    # Custom HTML Overlay for a Sparkline directly embedded on Tier 3
    tier_3_sparkline = """
    <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 2cqh; container-type: size;">
        <svg width="50cqw" height="20cqh" viewBox="0 0 100 30" preserveAspectRatio="none">
            <polyline points="0,30 25,25 50,15 75,10 100,5" fill="none" stroke="#047857" stroke-width="3" />
            <polygon points="0,30 0,30 25,25 50,15 75,10 100,5 100,30" fill="rgba(4, 120, 87, 0.2)" />
        </svg>
    </div>
    """
    app.add_overlay("poly-tier-3", tier_3_sparkline)
    app.map("poly-tier-3", hover_color="#6ee7b7", tooltip="<b>Storage Layer</b><br>Cost-effective, scalable object storage with ACID transaction guarantees.")

    # Tier 4 - Ingestion & Sources (Bottom)
    app.add_scalable_text("poly-tier-4", "INGESTION PIPELINES", font_size="10%", color="#0f172a", font_weight="800", align="center", top="40%")

    # Custom HTML Overlay for a Bar Chart directly embedded on Tier 4
    tier_4_bars = """
    <div style="width: 100%; height: 100%; display: flex; align-items: flex-end; justify-content: center; gap: 2cqw; padding-bottom: 2cqh; container-type: size;">
        <div style="width: 4cqw; height: 10cqh; background-color: #1d4ed8; border-radius: 2px 2px 0 0;"></div>
        <div style="width: 4cqw; height: 15cqh; background-color: #1d4ed8; border-radius: 2px 2px 0 0;"></div>
        <div style="width: 4cqw; height: 8cqh; background-color: #1d4ed8; border-radius: 2px 2px 0 0;"></div>
        <div style="width: 4cqw; height: 20cqh; background-color: #1d4ed8; border-radius: 2px 2px 0 0;"></div>
        <div style="width: 4cqw; height: 12cqh; background-color: #1d4ed8; border-radius: 2px 2px 0 0;"></div>
        <div style="width: 4cqw; height: 25cqh; background-color: #1d4ed8; border-radius: 2px 2px 0 0;"></div>
    </div>
    """
    app.add_overlay("poly-tier-4", tier_4_bars)
    app.map("poly-tier-4", hover_color="#93c5fd", tooltip="<b>Ingestion Layer</b><br>Extract and Load (EL) capabilities capturing data from transactional systems.")

    # Info Panel Side Content - System Architecture Health & Load
    app.add_scalable_text("info-panel-data", "System Load & Latency Metrics", left="0%", top="0%", width="100%", height="10%", font_size="20%", font_weight="800", color="#1e293b")

    # Side panel chart mapping
    app.map_bar_chart(
        element_id="info-panel-data",
        title="",
        categories=["Ingest", "Storage", "Compute", "App"],
        data=[
            {"name": "Throughput (GB/s)", "type": "bar", "data": [12.5, 8.2, 45.0, 2.1], "itemStyle": {"color": "#3b82f6", "borderRadius": [4, 4, 0, 0]}},
            {"name": "P99 Latency (ms)", "type": "bar", "data": [45, 120, 85, 200], "itemStyle": {"color": "#f43f5e", "borderRadius": [4, 4, 0, 0]}}
        ],
        extra_options={
            "grid": {"top": 80, "bottom": 30, "left": 40, "right": 20},
            "legend": {"show": True, "top": 30, "textStyle": {"fontSize": 12, "color": "#475569"}},
            "backgroundColor": "transparent",
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}}
        }
    )

    output_path = os.path.join(os.path.dirname(__file__), "04_org_chart.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
