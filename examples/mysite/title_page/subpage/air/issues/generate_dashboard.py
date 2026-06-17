import sys
import os
import subprocess

# Run the sub-dashboard generator first
sub_dashboard_script = os.path.join(os.path.dirname(__file__), "generate_sub_dashboard.py")
subprocess.run([sys.executable, sub_dashboard_script], check=True)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "sublinks": [
        {"label": "Overview", "url": "../index.html", "url_transition": "page-turn-enter"},
        {"label": "Pressures", "url": "index.html", "url_transition": "page-turn-enter"},
        {"label": "State", "url": "../science/index.html", "url_transition": "page-turn-enter"},
        {"label": "Actions", "url": "../help/index.html", "url_transition": "page-turn-enter"}
    ]},
    {"label": "Land", "url": "../../land/index.html", "url_transition": "page-turn-enter"},
    {"label": "Water", "url": "../../water/index.html", "url_transition": "page-turn-enter"}
]

dashboard = SivoDashboard(
    title="",
    columns=6,
    background_image_url="../../../assets/air/air_bg.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    width="80%",
    mobile_width="90%",
    theme="transparent",
    gap="tight",
    navigation_menu=nav_menu
)

def read_md(name):
    with open(os.path.join(os.path.dirname(__file__), "md", name + ".md"), "r", encoding="utf-8") as f:
        return f.read()

pm_md = read_md("pm")
importance_md = read_md("importance")
influences_md = read_md("influences")

desktop_grid = """
'. banner banner banner banner .'
'. pm pm pm pm .'
'. importance importance importance importance .'
'. influences influences influences influences .'
"""

mobile_grid = """
'banner'
'pm'
'importance'
'influences'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../../../assets/air/air_banner.png",
    col_span=4,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

dashboard.add_details_panel(
    block_id="pm",
    title="",
    placeholder=pm_md,
    col_span=4,
    grid_area="pm",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=300,
    fade_duration_ms=2000
)

dashboard.add_details_panel(
    block_id="importance",
    title="",
    placeholder=importance_md,
    col_span=4,
    grid_area="importance",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=600,
    fade_duration_ms=2000
)

dashboard.add_details_panel(
    block_id="influences",
    title="",
    placeholder=influences_md,
    col_span=4,
    grid_area="influences",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=900,
    fade_duration_ms=2000
)

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
