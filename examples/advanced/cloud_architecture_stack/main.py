from sivo import Sivo
import os

def build_architecture_stack():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "premium_layer_stack_2026.svg"
    )
    output_dir = os.path.dirname(__file__)

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=True,
        lock_canvas=True,
        theme="dark"
    )

    app.apply_template_style("cyberpunk")

    # Header
    app.fill_template_zone("header-subtitle-placeholder", "SYSTEM TOPOLOGY", font_size=14, font_weight="600", color="#ff00ff")
    app.fill_template_zone("header-title-placeholder", "Neo-Cloud Architecture", font_size=36, font_weight="800", color="#ffffff")

    # Layer 3 (Bottom) - Data Tier
    app.fill_template_zone("layer-3-label-placeholder", "DATA TIER", font_size=20, font_weight="700", color="#00ffcc", align="right")
    app.fill_template_zone("layer-3-desc-1-placeholder", "Distributed Object Storage", font_size=14, font_weight="400", color="#cbd5e1", align="right")
    app.fill_template_zone("layer-3-desc-2-placeholder", "and NoSQL databases.", font_size=14, font_weight="400", color="#cbd5e1", align="right")

    # Layer 2 (Middle) - Logic Tier
    app.fill_template_zone("layer-2-label-placeholder", "SERVICE MESH", font_size=20, font_weight="700", color="#00ffcc", align="left")
    app.fill_template_zone("layer-2-desc-1-placeholder", "Containerized microservices", font_size=14, font_weight="400", color="#cbd5e1", align="left")
    app.fill_template_zone("layer-2-desc-2-placeholder", "and API gateways.", font_size=14, font_weight="400", color="#cbd5e1", align="left")

    # Layer 1 (Top) - Presentation
    app.fill_template_zone("layer-1-label-placeholder", "EDGE UI", font_size=20, font_weight="700", color="#ff00ff", align="right")
    app.fill_template_zone("layer-1-desc-1-placeholder", "Client-side rendering layer", font_size=14, font_weight="400", color="#cbd5e1", align="right")
    app.fill_template_zone("layer-1-desc-2-placeholder", "via CDN edge nodes.", font_size=14, font_weight="400", color="#cbd5e1", align="right")

    # Map Treemap to Data Tier
    data_tier_treemap = [
        {"name": "PostgreSQL Primary", "value": 1500},
        {"name": "Read Replicas", "value": 3000, "children": [
            {"name": "Replica US", "value": 1000},
            {"name": "Replica EU", "value": 1000},
            {"name": "Replica ASIA", "value": 1000}
        ]},
        {"name": "Redis Cache", "value": 800},
        {"name": "S3 Storage", "value": 5000}
    ]
    app.map_treemap_chart(
        element_id="layer-3-data",
        title="Data Tier Resource Allocation (GB)",
        data=data_tier_treemap,
        color=["#00ffcc", "#00b38f", "#008066", "#004d3d"],
        tooltip="View detailed storage volume distributions.",
        panel_position="right"
    )

    # Map Network Graph to Logic Tier
    nodes = [
        {"name": "Gateway", "symbolSize": 30},
        {"name": "Auth Service", "symbolSize": 20},
        {"name": "User Service", "symbolSize": 20},
        {"name": "Billing Service", "symbolSize": 20},
        {"name": "Analytics Service", "symbolSize": 25}
    ]
    links = [
        {"source": "Gateway", "target": "Auth Service"},
        {"source": "Gateway", "target": "User Service"},
        {"source": "Gateway", "target": "Billing Service"},
        {"source": "User Service", "target": "Analytics Service"},
        {"source": "Billing Service", "target": "Analytics Service"}
    ]
    app.map_graph_chart(
        element_id="layer-2-logic",
        title="Microservice Topology",
        nodes=nodes,
        links=links,
        layout="force",
        color="#ff00ff",
        tooltip="Click to trace API dependencies.",
        panel_position="right"
    )

    output_path = os.path.join(output_dir, "cloud_architecture.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    build_architecture_stack()