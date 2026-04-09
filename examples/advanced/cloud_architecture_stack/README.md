# Cloud Architecture Stack

## Description
Header Layer 3 (Bottom) - Data Tier Layer 2 (Middle) - Logic Tier Layer 1 (Top) - Presentation Map Treemap to Data Tier Map Network Graph to Logic Tier

## Relevant Code
```python
    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=True,
        lock_canvas=True,
        theme="dark"
    )
    app.apply_template_style("cyberpunk")
    app.fill_template_zone("header-subtitle-placeholder", "SYSTEM TOPOLOGY", font_size=14, font_weight="600", color="#ff00ff")
    app.fill_template_zone("header-title-placeholder", "Neo-Cloud Architecture", font_size=36, font_weight="800", color="#ffffff")
    app.fill_template_zone("layer-3-label-placeholder", "DATA TIER", font_size=20, font_weight="700", color="#00ffcc", align="right")
    app.fill_template_zone("layer-3-desc-1-placeholder", "Distributed Object Storage", font_size=14, font_weight="400", color="#cbd5e1", align="right")
    app.fill_template_zone("layer-3-desc-2-placeholder", "and NoSQL databases.", font_size=14, font_weight="400", color="#cbd5e1", align="right")
    app.fill_template_zone("layer-2-label-placeholder", "SERVICE MESH", font_size=20, font_weight="700", color="#00ffcc", align="left")
    app.fill_template_zone("layer-2-desc-1-placeholder", "Containerized microservices", font_size=14, font_weight="400", color="#cbd5e1", align="left")
    app.fill_template_zone("layer-2-desc-2-placeholder", "and API gateways.", font_size=14, font_weight="400", color="#cbd5e1", align="left")
    app.fill_template_zone("layer-1-label-placeholder", "EDGE UI", font_size=20, font_weight="700", color="#ff00ff", align="right")
    app.fill_template_zone("layer-1-desc-1-placeholder", "Client-side rendering layer", font_size=14, font_weight="400", color="#cbd5e1", align="right")
    app.fill_template_zone("layer-1-desc-2-placeholder", "via CDN edge nodes.", font_size=14, font_weight="400", color="#cbd5e1", align="right")
    app.map_treemap_chart(
        element_id="layer-3-data",
        title="Data Tier Resource Allocation (GB)",
        data=data_tier_treemap,
        color=["#00ffcc", "#00b38f", "#008066", "#004d3d"],
        tooltip="View detailed storage volume distributions.",
        panel_position="right"
    )
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
    app.to_html(output_path)
```
