import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "sublinks": [
        {"label": "Issues", "url": "issues/index.html", "url_transition": "page-turn-enter"},
        {"label": "Science", "url": "science/index.html", "url_transition": "page-turn-enter"},
        {"label": "How to help", "url": "help/index.html", "url_transition": "page-turn-enter"}
    ]},
    {"label": "Land", "url": "../land/index.html", "url_transition": "page-turn-enter"},
    {"label": "Water", "url": "../water/index.html", "url_transition": "page-turn-enter"}
]

dashboard = SivoDashboard(
    title="",
    columns=2,
    background_image_url="../../assets/air/air_bg.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    width="80%",
    mobile_width="100%",
    theme="transparent",
    gap="tight",
    navigation_menu=nav_menu
)

# Read the markdown
with open(os.path.join(os.path.dirname(__file__), "welcome.md"), "r", encoding="utf-8") as f:
    md_content = f.read()

desktop_grid = """
'banner banner'
'markdown leaves'
'issues leaves'
'science leaves'
'help leaves'
"""

mobile_grid = """
'banner'
'markdown'
'issues'
'science'
'help'
'leaves'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../../assets/air/air_banner.png",
    col_span=2,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

dashboard.add_details_panel(
    block_id="markdown",
    title="",
    placeholder=md_content,
    col_span=1,
    grid_area="markdown",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=300,
    fade_duration_ms=2000
)

dashboard.add_image_block(
    block_id="leaves",
    image_url="../../assets/air/leaves.png",
    col_span=1,
    grid_area="leaves",
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
