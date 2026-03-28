"""
Quad Grid Zooming Example
=========================

This example demonstrates how to use the `quad_grid.html` template
with interactive zoom features. Clicking an element within a square
zooms the map into another area within the same square using the
`zoom_to` and `zoom_to_size` features.
"""

from sivo import Sivo
from sivo.core.dashboard import SivoDashboard
import os

def main():
    dashboard = SivoDashboard(title="Interactive Zoom Quad Grid")
    dashboard.set_grid_layout(
        desktop='''
    "tl tr"
"bl br"
        ''',
        mobile='''
    "tl"
"tr"
"bl"
"br"
        '''
    )

    # Reusable SVG string for each quadrant block
    # Each quadrant has a background square and two inner areas to click and zoom between
    quad_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
        <rect id="bg" x="0" y="0" width="400" height="400" fill="#f8fafc" rx="16" />

        <!-- Main Area -->
        <circle id="main_area" cx="200" cy="200" r="150" fill="#cbd5e1" />
        <text x="200" y="100" font-family="sans-serif" font-size="20" fill="#475569" text-anchor="middle" pointer-events="none">Main Area</text>

        <!-- Detail Area -->
        <circle id="detail_area" cx="200" cy="200" r="30" fill="#3b82f6" />
        <text x="200" y="204" font-family="sans-serif" font-size="10" fill="#ffffff" text-anchor="middle" pointer-events="none">Zoom</text>
    </svg>"""

    # We will create 4 Sivo blocks, one for each quadrant
    for i in range(1, 5):
        block = Sivo.from_string(quad_svg, title=f"Quadrant {i}", layout_size="90%")

        # When clicking the detail area, zoom into it
        block.map(
            "detail_area",
            hover_color="#2563eb",
            zoom_to="detail_area",
            zoom_to_size="80%"
        )

        # When clicking the main area, zoom out to show the whole main area
        block.map(
            "main_area",
            hover_color="#94a3b8",
            zoom_to="main_area",
            zoom_to_size="90%"
        )

        # Add the block to the dashboard grid
        dashboard.add_sivo_block(f"quadrant_{i}", block)

    # Export
    output_file = os.path.join(os.path.dirname(__file__), "output.html")
    print(f"Generating Quad Grid Zoom Dashboard to '{output_file}'...")
    dashboard.to_html(output_file)
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    main()
