import os
from sivo import Sivo

def main():
    # Define a simple SVG representing a network or map
    # Use standard shapes with explicit coordinates so bounding boxes calculate easily
    svg_string = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
        <rect id="background" width="1000" height="600" fill="#f8fafc" rx="15" />

        <!-- Server Nodes -->
        <circle id="node_database" cx="200" cy="300" r="60" fill="#3b82f6" />
        <text x="200" y="305" font-family="sans-serif" font-size="16" fill="white" text-anchor="middle" dominant-baseline="middle" pointer-events="none">Database</text>

        <circle id="node_api" cx="500" cy="150" r="60" fill="#10b981" />
        <text x="500" y="155" font-family="sans-serif" font-size="16" fill="white" text-anchor="middle" dominant-baseline="middle" pointer-events="none">API</text>

        <circle id="node_client" cx="800" cy="300" r="60" fill="#8b5cf6" />
        <text x="800" y="305" font-family="sans-serif" font-size="16" fill="white" text-anchor="middle" dominant-baseline="middle" pointer-events="none">Client</text>
    </svg>"""

    # 1. Initialize Sivo with the new drawing tools enabled
    sivo_app = Sivo.from_string(
        svg_string,
        title="Network Architecture & Annotations",
        subtitle="Test the new Dynamic Flow Arrows and Drawing Tools.",
        enable_drawing_tools=True,  # Enables the top-right drawing toolbar
        theme="light",
        disable_panel=True          # Focus entirely on the canvas features
    )

    # 2. Add Dynamic Flow Arrows between nodes
    # Data flow from Database to API
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

    # Data flow from API to Client
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

    # Map hover interactions to ensure standard interactivity works simultaneously
    sivo_app.map("node_database", tooltip="Primary SQL Database Cluster", hover_color="#2563eb", glow=True)
    sivo_app.map("node_api", tooltip="GraphQL API Gateway", hover_color="#059669", glow=True)
    sivo_app.map("node_client", tooltip="Web / Mobile Client Apps", hover_color="#7c3aed", glow=True)

    # 3. Export to HTML
    output_file = os.path.join(os.path.dirname(__file__), 'output.html')
    sivo_app.to_html(output_file)
    print(f"Generated example at {output_file}")

if __name__ == "__main__":
    main()
