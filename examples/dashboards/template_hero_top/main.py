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
    # Set default_panel_position="none" to ensure no side panel is shown by default
    sivo_map = Sivo.from_string(map_svg, theme="light", title="Global Fleet Status", layout_size="100%", default_panel_position="none")

    # Add click interactivity so clicking regions updates a details panel in the dashboard grid
    na_html = """
    <div style="font-family: sans-serif;">
        <h4 style="color: #3b82f6; margin-top: 0;">NA Data Center</h4>
        <p>Status: All systems operational.</p>
        <p>Recent Logs: [INFO] Daily backup completed successfully.</p>
    </div>
    """

    eu_html = """
    <div style="font-family: sans-serif;">
        <h4 style="color: #f59e0b; margin-top: 0;">EU Data Center</h4>
        <p>Status: Maintenance ongoing.</p>
        <p>Recent Logs: [WARN] Node 3 latency spike detected.</p>
    </div>
    """

    as_html = """
    <div style="font-family: sans-serif;">
        <h4 style="color: #10b981; margin-top: 0;">AS Data Center</h4>
        <p>Status: Optimal.</p>
        <p>Recent Logs: [INFO] New deployment rolled out to production.</p>
    </div>
    """

    sivo_map.map("node_na", hover_color="#2563eb", tooltip="Click for NA logs", html=na_html)
    sivo_map.map("node_eu", hover_color="#d97706", tooltip="Click for EU logs", html=eu_html)
    sivo_map.map("node_as", hover_color="#059669", tooltip="Click for AS logs", html=as_html)

    # --- 2. Secondary Blocks ---
    chart_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
        <rect width="400" height="400" fill="#ffffff" />
        <circle cx="200" cy="200" r="100" fill="#3b82f6" />
        <text x="200" y="200" font-family="sans-serif" font-size="24" fill="#fff" text-anchor="middle">99.9% Uptime</text>
    </svg>"""
    # You can change `layout_size` independently for each block to create margins or focus area
    sivo_chart = Sivo.from_string(chart_svg, theme="light", layout_size="80%", default_panel_position="none")


    # --- 3. Assemble the Dashboard using 'hero_top' template ---
    # By specifying the CSS Grid layout, SivoDashboard builds a responsive top-hero view.
    dashboard = SivoDashboard(title="Hero Top HTML Template Example")
    dashboard.set_grid_layout(
        desktop='''
    "hero hero hero"
    "col1 col2 col3"
        ''',
        mobile='''
    "hero"
    "col1"
    "col2"
    "col3"
        '''
    )

    # Assign the map to the 'hero' slot to span the full width at the top
    dashboard.add_sivo_block("fleet_map", sivo_map, grid_area="hero")

    # Add a Details Panel to 'col3' which automatically renders `html` from mapped Sivo blocks
    dashboard.add_details_panel("log_details", title="Data Center Logs", placeholder="Select a region to view its logs.", grid_area="col3")

    # Assign secondary blocks to the remaining grid areas
    dashboard.add_sivo_block("chart_1", sivo_chart, grid_area="col1")
    dashboard.add_sivo_block("chart_2", sivo_chart, grid_area="col2")

    # Export
    output_file = os.path.join(os.path.dirname(__file__), "output.html")
    dashboard.to_html(output_file)
    print(f"Successfully generated dashboard from HTML template: {output_file}")


if __name__ == "__main__":
    main()
