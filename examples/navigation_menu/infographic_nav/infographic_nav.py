import os
import sys

# Ensure SIVO is in the path for the example to run correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src')))

from sivo.core.project import SivoProject
from sivo.core.sivo import Sivo

# Paths
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "infographic_nav.html")

# Create the main view
main_app = Sivo.from_string(
    '<svg width="100%" height="100%" viewBox="0 0 100 100"><rect width="100" height="100" fill="#f8fafc"/><text x="50" y="50" font-family="Arial" font-size="10" text-anchor="middle" dominant-baseline="middle" fill="#334155">Main View</text></svg>',
    navigation_menu=[
        {"label": "SIVO Homepage", "url": "https://sivo.dev"},
        {
            "label": "GitHub Resources",
            "sublinks": [
                {"label": "Examples", "url": "https://github.com/LukeAFullard/sivo/tree/main/examples"},
                {"label": "Documentation", "url": "https://github.com/LukeAFullard/sivo/blob/main/README.md"},
                {"label": "Code", "url": "https://github.com/LukeAFullard/sivo/tree/main/src/sivo"}
            ]
        },
        {"label": "Go to Detail View", "view_id": "detail_view"}
    ],
    navigation_menu_position="top-left"
)

# Create a detail view to navigate to
detail_app = Sivo.from_string(
    '<svg width="100%" height="100%" viewBox="0 0 100 100"><rect width="100" height="100" fill="#e2e8f0"/><text x="50" y="50" font-family="Arial" font-size="10" text-anchor="middle" dominant-baseline="middle" fill="#0f172a">Detail View</text></svg>',
    navigation_menu=[
        {"label": "Back to Main", "view_id": "main_view"}
    ],
    navigation_menu_position="top-left"
)

# Use SivoProject to bundle them together so internal view_id navigation works
project = SivoProject(initial_view_id="main_view")
project.add_view("main_view", main_app)
project.add_view("detail_view", detail_app)

project.to_html(OUTPUT_FILE)
print(f"Generated successfully: {OUTPUT_FILE}")
