# Drawing And Flow

## Description
Define a simple SVG representing a network or map Use standard shapes with explicit coordinates so bounding boxes calculate easily 1. Initialize Sivo with the new drawing tools enabled 2. Add Dynamic Flow Arrows between nodes Data flow from Database to API Data flow from API to Client Map hover interactions to ensure standard interactivity works simultaneously 3. Export to HTML

## Relevant Code
```python
    sivo_app = Sivo.from_string(
        svg_string,
        title="Network Architecture & Annotations",
        subtitle="Test the new Dynamic Flow Arrows and Drawing Tools.",
        enable_drawing_tools=True,  # Enables the top-right drawing toolbar
        theme="light",
        disable_panel=True          # Focus entirely on the canvas features
    )
    sivo_app.add_connection(
        source_id="node_database",
        target_id="node_api",
        label="Data Fetch",
        color="#3b82f6",
        width=3,
        animation_speed=4,
        type="dashed",
        flow_effect=True,
        effect_symbol="arrow",
        effect_size=12
    )
    sivo_app.add_connection(
        source_id="node_api",
        target_id="node_client",
        label="Response",
        color="#10b981",
        width=3,
        animation_speed=3,
        type="solid",
        flow_effect=True,
        effect_symbol="circle", # Different effect style
        effect_size=8
    )
    sivo_app.map("node_database", tooltip="Primary SQL Database Cluster", hover_color="#2563eb", glow=True)
    sivo_app.map("node_api", tooltip="GraphQL API Gateway", hover_color="#059669", glow=True)
    sivo_app.map("node_client", tooltip="Web / Mobile Client Apps", hover_color="#7c3aed", glow=True)
    sivo_app.to_html(output_file)
```
