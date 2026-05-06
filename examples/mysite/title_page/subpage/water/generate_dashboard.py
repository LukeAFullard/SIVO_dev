import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "url": "../air/index.html", "url_transition": "page-turn-enter"},
    {"label": "Land", "url": "../land/index.html", "url_transition": "page-turn-enter"},
    {"label": "Water", "sublinks": [
        {"label": "Issues", "url": "issues/index.html", "url_transition": "page-turn-enter"},
        {"label": "Science", "url": "science/index.html", "url_transition": "page-turn-enter"},
        {"label": "How to help", "url": "help/index.html", "url_transition": "page-turn-enter"}
    ]}
]

dashboard = SivoDashboard(
    title="",
    columns=1,
    background_image_url="water_bg.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    theme="transparent",
    gap="1rem",
    navigation_menu=nav_menu
)

desktop_grid = """
'banner'
'issues'
'science'
'help'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=desktop_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="water_banner.png",
    col_span=1,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

dashboard.add_text_block(
    block_id="issues",
    text="What are the issues?",
    url="issues/index.html",
    url_transition="page-turn-enter",
    col_span=1,
    grid_area="issues",
    fade_in=True,
    fade_start_time_ms=300,
    fade_duration_ms=2000
)

dashboard.add_text_block(
    block_id="science",
    text="What does the science say?",
    url="science/index.html",
    url_transition="page-turn-enter",
    col_span=1,
    grid_area="science",
    fade_in=True,
    fade_start_time_ms=600,
    fade_duration_ms=2000
)

dashboard.add_text_block(
    block_id="help",
    text="What can we do to help?",
    url="help/index.html",
    url_transition="page-turn-enter",
    col_span=1,
    grid_area="help",
    fade_in=True,
    fade_start_time_ms=900,
    fade_duration_ms=2000
)

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
