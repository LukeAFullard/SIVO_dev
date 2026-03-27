import os
from sivo import Sivo, SivoDashboard

def main():
    # --- 1. Top Block: Global Map (Hero Slot) ---
    map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300">
        <rect id="bg" width="1000" height="300" fill="#e2e8f0" />
        <rect id="node_na" x="150" y="100" width="200" height="100" fill="#3b82f6" />
        <rect id="node_eu" x="450" y="100" width="200" height="100" fill="#f59e0b" />
        <rect id="node_as" x="750" y="100" width="200" height="100" fill="#10b981" />
        <text x="250" y="150" font-family="sans-serif" font-size="18" fill="#fff" pointer-events="none" text-anchor="middle">NA Data Center</text>
        <text x="550" y="150" font-family="sans-serif" font-size="18" fill="#fff" pointer-events="none" text-anchor="middle">EU Data Center</text>
        <text x="850" y="150" font-family="sans-serif" font-size="18" fill="#fff" pointer-events="none" text-anchor="middle">AS Data Center</text>
    </svg>"""
    # Explicitly configure `layout_size` so the SVG fills 100% of the Hero container bounds
    sivo_map = Sivo.from_string(map_svg, theme="light", title="Global Fleet Status", layout_size="100%")

    sivo_map.map("node_na", hover_color="#2563eb", tooltip="Click for NA logs")
    sivo_map.map("node_eu", hover_color="#d97706", tooltip="Click for EU logs")
    sivo_map.map("node_as", hover_color="#059669", tooltip="Click for AS logs")

    # --- 2. Secondary Blocks ---
    chart_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
        <rect width="400" height="400" fill="#ffffff" />
        <circle cx="200" cy="200" r="100" fill="#3b82f6" />
        <text x="200" y="200" font-family="sans-serif" font-size="24" fill="#fff" text-anchor="middle">99.9% Uptime</text>
    </svg>"""
    # You can change `layout_size` independently for each block to create margins or focus area
    sivo_chart = Sivo.from_string(chart_svg, theme="light", layout_size="80%")


    # --- 3. Assemble the Dashboard using 'hero_top' template ---
    # By specifying `template="hero_top"`, SivoDashboard loads a custom HTML layout template
    # that exposes a full-width 'hero' slot and a multi-column 'main' slot below it.
    dashboard = SivoDashboard(title="Hero Top HTML Template Example", template="hero_top", columns=2)

    # Assign the map to the 'hero' slot to span the full width at the top
    dashboard.add_sivo_block("fleet_map", sivo_map, slot="hero")

    # Assign secondary blocks to the 'main' grid below the hero slot
    dashboard.add_sivo_block("chart_1", sivo_chart, slot="main", col_span=1)
    dashboard.add_sivo_block("chart_2", sivo_chart, slot="main", col_span=1)

    # Export
    output_file = os.path.join(os.path.dirname(__file__), "output.html")
    dashboard.to_html(output_file)
    print(f"Successfully generated dashboard from HTML template: {output_file}")


if __name__ == "__main__":
    main()
