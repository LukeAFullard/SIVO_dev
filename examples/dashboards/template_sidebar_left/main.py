import os
from sivo import Sivo, SivoDashboard

def main():
    # --- 1. Main Content Block: Global Map ---
    map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
        <rect id="bg" width="1000" height="600" fill="#f8fafc" />
        <circle id="node_na" cx="250" cy="200" r="60" fill="#3b82f6" />
        <circle id="node_eu" cx="600" cy="180" r="50" fill="#f59e0b" />
        <circle id="node_as" cx="800" cy="250" r="70" fill="#10b981" />

        <text x="250" y="290" font-family="sans-serif" font-size="18" fill="#333" pointer-events="none" text-anchor="middle">North America</text>
        <text x="600" y="260" font-family="sans-serif" font-size="18" fill="#333" pointer-events="none" text-anchor="middle">Europe</text>
        <text x="800" y="350" font-family="sans-serif" font-size="18" fill="#333" pointer-events="none" text-anchor="middle">Asia</text>
    </svg>"""
    # Pass `layout_size` to control exactly how much of the card the SVG fills.
    sivo_map = Sivo.from_string(map_svg, theme="light", title="Global Active Nodes", layout_size="100%")
    sivo_map.map("node_na", hover_color="#2563eb", tooltip="NA Region Details", callback_payload={"status": "Healthy", "latency": "24ms"})
    sivo_map.map("node_eu", hover_color="#d97706", tooltip="EU Region Details", callback_payload={"status": "Degraded", "latency": "180ms"})
    sivo_map.map("node_as", hover_color="#059669", tooltip="AS Region Details", callback_payload={"status": "Healthy", "latency": "45ms"})

    # --- 2. Assemble the Dashboard using 'sidebar_left' template ---
    # By specifying `template="sidebar_left"`, SivoDashboard loads the custom layout template
    dashboard = SivoDashboard(title="Sidebar Layout HTML Template Example", template="sidebar_left", columns=1)

    # Assign the map to the 'main' content slot
    dashboard.add_sivo_block("global_map", sivo_map, slot="main")

    # Assign interaction panels to the 'sidebar' slot
    dashboard.add_metrics_panel("metrics", title="Node Metrics", metrics=["status", "latency"], slot="sidebar")
    dashboard.add_details_panel("details", title="Node Details", slot="sidebar")

    # Export
    output_file = os.path.join(os.path.dirname(__file__), "output.html")
    dashboard.to_html(output_file)
    print(f"Successfully generated dashboard from HTML template: {output_file}")


if __name__ == "__main__":
    main()
