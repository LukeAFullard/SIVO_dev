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

    # The tiers in the SVG are brightly colored:
    # tier-1 (red): #f87171, tier-2 (yellow): #fbbf24, tier-3 (green): #34d399, tier-4 (blue): #60a5fa
    # Dark text (#0f172a or #1e293b) works best for contrast.

    # Tier 1 - Application Layer (Top)
    app.add_scalable_text("poly-tier-1", "APP LAYER", font_size="12%", color="#0f172a", font_weight="900", align="center", top="40%")
    app.add_scalable_text("poly-tier-1", "SaaS, BI, ML", font_size="8%", color="#1e293b", font_weight="600", align="center", top="65%")
    app.map("poly-tier-1", hover_color="#fca5a5", tooltip="<b>Application Layer</b><br>Provides APIs and visualization tools for end-users to consume insights.")

    # Tier 2 - Compute & Analytics
    app.add_scalable_text("poly-tier-2", "COMPUTE ENGINE", font_size="15%", color="#0f172a", font_weight="800", align="center", top="45%")
    # Let's add a small sparkline chart directly inside the tier-2 polygon
    app.map_line_chart(
        element_id="poly-tier-2",
        title="",
        categories=["M1", "M2", "M3", "M4"],
        data=[12, 18, 25, 40],
        color="#d97706", # darker orange/yellow for contrast
        smooth=True,
        extra_options={
            "grid": {"top": "70%", "bottom": "10%", "left": "30%", "right": "30%"},
            "xAxis": {"show": False},
            "yAxis": {"show": False},
            "series": [{"areaStyle": {"opacity": 0.2}, "lineStyle": {"width": 2}}],
            "backgroundColor": "transparent"
        }
    )
    app.map("poly-tier-2", hover_color="#fde047", tooltip="<b>Compute Layer</b><br>Scalable distributed processing for batch and streaming data.")

    # Tier 3 - Storage & Lakehouse
    app.add_scalable_text("poly-tier-3", "LAKEHOUSE STORAGE", font_size="12%", color="#0f172a", font_weight="800", align="center", top="45%")
    # Sparkline chart in tier-3
    app.map_line_chart(
        element_id="poly-tier-3",
        title="",
        categories=["M1", "M2", "M3", "M4"],
        data=[100, 150, 250, 400],
        color="#047857", # darker green
        smooth=True,
        extra_options={
            "grid": {"top": "70%", "bottom": "10%", "left": "25%", "right": "25%"},
            "xAxis": {"show": False},
            "yAxis": {"show": False},
            "series": [{"areaStyle": {"opacity": 0.2}, "lineStyle": {"width": 2}}],
            "backgroundColor": "transparent"
        }
    )
    app.map("poly-tier-3", hover_color="#6ee7b7", tooltip="<b>Storage Layer</b><br>Cost-effective, scalable object storage with ACID transaction guarantees.")

    # Tier 4 - Ingestion & Sources (Bottom)
    app.add_scalable_text("poly-tier-4", "INGESTION PIPELINES", font_size="10%", color="#0f172a", font_weight="800", align="center", top="40%")
    # Bar chart in tier-4
    app.map_bar_chart(
        element_id="poly-tier-4",
        title="",
        categories=["S1", "S2", "S3", "S4", "S5", "S6"],
        data=[40, 60, 30, 80, 50, 90],
        color="#1d4ed8", # darker blue
        extra_options={
            "grid": {"top": "60%", "bottom": "20%", "left": "20%", "right": "20%"},
            "xAxis": {"show": False},
            "yAxis": {"show": False},
            "backgroundColor": "transparent"
        }
    )
    app.map("poly-tier-4", hover_color="#93c5fd", tooltip="<b>Ingestion Layer</b><br>Extract and Load (EL) capabilities capturing data from transactional systems.")

    # Info Panel Side Content - System Architecture Health & Load
    app.add_scalable_text("info-panel-data", "System Load & Latency Metrics", left="0%", top="0%", width="100%", height="10%", font_size="20%", font_weight="800", color="#1e293b")

    # Adding a grouped bar chart to represent read/write load per layer
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
