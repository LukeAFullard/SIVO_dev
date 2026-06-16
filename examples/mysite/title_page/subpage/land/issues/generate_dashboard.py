import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../..')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "url": "../../air/index.html", "url_transition": "page-turn-enter"},
    {"label": "Land", "sublinks": [
        {"label": "Pressures", "url": "index.html", "url_transition": "page-turn-enter"},
        {"label": "State", "url": "../science/index.html", "url_transition": "page-turn-enter"},
        {"label": "Actions", "url": "../help/index.html", "url_transition": "page-turn-enter"}
    ]},
    {"label": "Water", "url": "../../water/index.html", "url_transition": "page-turn-enter"}
]

dashboard = SivoDashboard(
    title="",
    columns=4,
    background_image_url="../../../assets/land/land_bg.png",
    background_image_opacity=0.15,
    background_image_size="50%",
    width="80%",
    mobile_width="100%",
    theme="transparent",
    gap="1rem",
    navigation_menu=nav_menu
)

# Read the markdown
with open(os.path.join(os.path.dirname(__file__), "md/md1.md"), "r", encoding="utf-8") as f:
    md_content1 = f.read()

with open(os.path.join(os.path.dirname(__file__), "md/md2.md"), "r", encoding="utf-8") as f:
    md_content2 = f.read()

desktop_grid = """
'banner banner banner banner'
'. markdown1 markdown1 .'
'. markdown2 markdown2 .'
'. image3 image3 .'
"""

mobile_grid = """
'banner'
'markdown1'
'markdown2'
'image3'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../../../assets/land/land_banner.png",
    col_span=4,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

dashboard.add_details_panel(
    block_id="markdown1",
    title="",
    placeholder=md_content1,
    col_span=2,
    grid_area="markdown1",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=300,
    fade_duration_ms=2000
)

dashboard.add_details_panel(
    block_id="markdown2",
    title="",
    placeholder=md_content2,
    col_span=2,
    grid_area="markdown2",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=600,
    fade_duration_ms=2000
)

dashboard.add_image_block(
    block_id="image3",
    image_url="../../../assets/land/landscape_multi.png",
    col_span=2,
    grid_area="image3",
    object_fit="contain",
    border_radius="10px",
    fade_in=True,
    fade_start_time_ms=1500,
    fade_duration_ms=2000
)


output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
