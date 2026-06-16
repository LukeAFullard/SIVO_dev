import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "url": "../air/index.html", "url_transition": "page-turn-enter"},
    {"label": "Land", "sublinks": [
        {"label": "Pressures", "url": "issues/index.html", "url_transition": "page-turn-enter"},
        {"label": "State", "url": "science/index.html", "url_transition": "page-turn-enter"},
        {"label": "Actions", "url": "help/index.html", "url_transition": "page-turn-enter"}
    ]},
    {"label": "Water", "url": "../water/index.html", "url_transition": "page-turn-enter"}
]

dashboard = SivoDashboard(
    title="",
    columns=2,
    background_image_url="../../assets/land/land_bg.png",
    background_image_opacity=0.15,
    background_image_size="50%",
    width="80%",
    mobile_width="100%",
    theme="transparent",
    gap="1rem",
    navigation_menu=nav_menu
)

# Read the markdown
with open(os.path.join(os.path.dirname(__file__), "welcome.md"), "r", encoding="utf-8") as f:
    md_content = f.read()

desktop_grid = """
'banner banner'
'markdown .'
'markdown issues'
'markdown science'
'markdown help'
'markdown .'
'landscape landscape'
"""

mobile_grid = """
'banner'
'markdown'
'issues'
'science'
'help'
'landscape'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../../assets/land/land_banner.png",
    col_span=2,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

dashboard.add_text_block(
    block_id="issues",
    text="Pressures | What's affecting the land? ",
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
    text="State | What does the data tell us?",
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
    text="Actions | What can we do to help?",
    url="help/index.html",
    url_transition="page-turn-enter",
    col_span=1,
    grid_area="help",
    fade_in=True,
    fade_start_time_ms=900,
    fade_duration_ms=2000
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
    block_id="landscape",
    image_url="../../assets/land/landscape.png",
    col_span=2,
    grid_area="landscape",
    object_fit="contain",
    border_radius="10px",
    fade_in=True,
    fade_start_time_ms=1200,
    fade_duration_ms=2000
)

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
