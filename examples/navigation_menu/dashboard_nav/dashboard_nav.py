import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src')))

from sivo.core.sivo import Sivo
from sivo.core.dashboard import SivoDashboard

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "dashboard_nav.html")

# Create some basic blocks
block1 = Sivo.from_string('<svg viewBox="0 0 100 100"><rect width="100" height="100" fill="#fecaca"/><text x="50" y="50" text-anchor="middle" font-family="Arial" fill="#991b1b">Block 1</text></svg>')
block2 = Sivo.from_string('<svg viewBox="0 0 100 100"><rect width="100" height="100" fill="#bfdbfe"/><text x="50" y="50" text-anchor="middle" font-family="Arial" fill="#1e40af">Block 2</text></svg>')

# Initialize the dashboard with a navigation menu
dashboard = SivoDashboard(
    title="Navigation Dashboard Example",
    columns=2,
    navigation_menu=[
        {"label": "Documentation", "url": "https://sivo.dev/docs"},
        {
            "label": "GitHub",
            "url": "https://github.com/LukeAFullard/sivo",
            "sublinks": [
                {"label": "Examples", "url": "https://github.com/LukeAFullard/sivo/tree/main/examples"},
                {"label": "Documentation", "url": "https://github.com/LukeAFullard/sivo/blob/main/README.md"},
                {"label": "Code", "url": "https://github.com/LukeAFullard/sivo/tree/main/src/sivo"}
            ]
        }
    ],
    navigation_menu_position="top-right"
)

# Add the blocks
dashboard.add_sivo_block("view1", block1, col_span=1)
dashboard.add_sivo_block("view2", block2, col_span=1)

dashboard.set_grid_layout(
    desktop='"view1 view2"',
    mobile='"view1"\n"view2"'
)

dashboard.to_html(OUTPUT_FILE)
print(f"Generated successfully: {OUTPUT_FILE}")
