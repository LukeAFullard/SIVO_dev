import os
from sivo import Sivo, SivoDashboard

def main():
    # --- 1. Top Left Block: Global Map ---
    map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
        <rect id="bg" width="1000" height="600" fill="#f8fafc" />
        <circle id="node_na" cx="250" cy="200" r="60" fill="#3b82f6" />
        <circle id="node_eu" cx="600" cy="180" r="50" fill="#f59e0b" />
        <circle id="node_as" cx="800" cy="250" r="70" fill="#10b981" />

        <text x="250" y="290" font-family="sans-serif" font-size="18" fill="#333" pointer-events="none" text-anchor="middle">North America</text>
        <text x="600" y="260" font-family="sans-serif" font-size="18" fill="#333" pointer-events="none" text-anchor="middle">Europe</text>
        <text x="800" y="350" font-family="sans-serif" font-size="18" fill="#333" pointer-events="none" text-anchor="middle">Asia</text>
    </svg>"""
    sivo_map = Sivo.from_string(map_svg, theme="light", title="Global Active Nodes")
    sivo_map.map("node_na", hover_color="#2563eb", tooltip="Status: Healthy")
    sivo_map.map("node_eu", hover_color="#d97706", tooltip="Status: Degradation")
    sivo_map.map("node_as", hover_color="#059669", tooltip="Status: Healthy")


    # --- 2. Top Right Block: Infrastructure Topology ---
    topo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600">
        <rect id="bg" width="600" height="600" fill="#ffffff" />
        <line x1="300" y1="200" x2="150" y2="400" stroke="#cbd5e1" stroke-width="4"/>
        <line x1="300" y1="200" x2="450" y2="400" stroke="#cbd5e1" stroke-width="4"/>

        <circle id="gateway" cx="300" cy="200" r="40" fill="#64748b" />
        <rect id="db_primary" x="110" y="380" width="80" height="60" rx="8" fill="#3b82f6" />
        <rect id="db_replica" x="410" y="380" width="80" height="60" rx="8" fill="#94a3b8" />

        <text x="300" y="260" font-family="sans-serif" font-size="16" fill="#333" pointer-events="none" text-anchor="middle">API Gateway</text>
        <text x="150" y="460" font-family="sans-serif" font-size="16" fill="#333" pointer-events="none" text-anchor="middle">Primary DB</text>
        <text x="450" y="460" font-family="sans-serif" font-size="16" fill="#333" pointer-events="none" text-anchor="middle">Replica DB</text>
    </svg>"""
    sivo_topo = Sivo.from_string(topo_svg, theme="light", title="US-East Topology")
    sivo_topo.map("gateway", hover_color="#475569", tooltip="Throughput: 15k req/s")
    sivo_topo.map("db_primary", hover_color="#2563eb", tooltip="CPU: 85% | Write-Heavy")
    sivo_topo.map("db_replica", hover_color="#64748b", tooltip="CPU: 12% | Read-Only")


    # --- 3. Bottom Block: Timeline / Metrics ---
    metrics_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300">
        <rect id="bg" width="1000" height="300" fill="#f8fafc" />
        <polyline points="100,250 300,200 500,100 700,150 900,50" fill="none" stroke="#3b82f6" stroke-width="4"/>

        <circle id="point1" cx="300" cy="200" r="10" fill="#3b82f6" />
        <circle id="point2" cx="500" cy="100" r="10" fill="#3b82f6" />
        <circle id="point3" cx="700" cy="150" r="10" fill="#3b82f6" />
        <circle id="point4" cx="900" cy="50" r="10" fill="#3b82f6" />
    </svg>"""
    sivo_metrics = Sivo.from_string(metrics_svg, theme="light", title="Latency Trend (7d)")
    sivo_metrics.map("point1", tooltip="24ms")
    sivo_metrics.map("point2", tooltip="18ms")
    sivo_metrics.map("point3", tooltip="35ms (Spike)")
    sivo_metrics.map("point4", tooltip="12ms")


    # --- 4. Assemble the Dashboard ---
    # We combine all three SIVO SVGs into a single responsive layout.
    # We will use raw HTML blocks to add structure or separators if desired,
    # but primarily focus on the SVG blocks.

    dashboard = SivoDashboard(title="Systems Command Center")

    # Add blocks in the order we want them to flow in the grid.
    # The default CSS Grid template will handle placing them side-by-side on desktop
    # and stacking them vertically on mobile.
    dashboard.add_sivo_block("global_map", sivo_map)
    dashboard.add_sivo_block("topology", sivo_topo)
    dashboard.add_sivo_block("latency_metrics", sivo_metrics)

    # Export
    output_file = os.path.join(os.path.dirname(__file__), "output.html")
    dashboard.to_html(output_file)
    print(f"Successfully generated multi-SIVO block dashboard: {output_file}")


if __name__ == "__main__":
    main()
