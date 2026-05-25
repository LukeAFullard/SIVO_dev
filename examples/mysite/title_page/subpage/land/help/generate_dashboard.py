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
        {"label": "Issues", "url": "../issues/index.html", "url_transition": "page-turn-enter"},
        {"label": "What we are doing", "url": "../science/index.html", "url_transition": "page-turn-enter"},
        {"label": "How to help", "url": "index.html", "url_transition": "page-turn-enter"}
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
with open(os.path.join(os.path.dirname(__file__), "md/help.md"), "r", encoding="utf-8") as f:
    md_content = f.read()

with open(os.path.join(os.path.dirname(__file__), "md/new_panel.md"), "r", encoding="utf-8") as f:
    new_panel_md_content = f.read()

desktop_grid = """
'banner banner banner banner'
'co_benefit co_benefit new_panel new_panel'
'. markdown markdown .'
'. sustainable sustainable .'
'birds birds birds birds'
"""

mobile_grid = """
'banner'
'markdown'
'co_benefit'
'new_panel'
'sustainable'
'birds'
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

dashboard.add_html_block(
    block_id="co_benefit",
    html_content='<div style="display:flex; justify-content:center; align-items:center; width:100%; height:100%;"><img src="../../../assets/land/soil_co_benefit.png" style="width:100%; height:100%; object-fit:contain; border-radius:0px;" /></div>',
    col_span=2,
    grid_area="co_benefit"
)

dashboard.add_details_panel(
    block_id="new_panel",
    title="",
    placeholder=new_panel_md_content,
    col_span=2,
    grid_area="new_panel",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=600,
    fade_duration_ms=2000
)

dashboard.add_details_panel(
    block_id="markdown",
    title="",
    placeholder=md_content,
    col_span=2,
    grid_area="markdown",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=300,
    fade_duration_ms=2000
)

dashboard.add_html_block(
    block_id="sustainable",
    html_content='<div style="display:flex; justify-content:center; align-items:center; width:100%; height:100%;"><img src="../../../assets/land/sustainable.png" style="width:100%; height:100%; object-fit:contain; border-radius:10px;" /></div>',
    col_span=2,
    grid_area="sustainable"
)

dashboard.add_html_block(
    block_id="birds",
    html_content='<div style="display:flex; justify-content:center; align-items:center; width:100%; height:100%;"><img src="../../../assets/land/birds.png" style="width:100%; height:100%; object-fit:contain; border-radius:10px;" /></div>',
    col_span=4,
    grid_area="birds"
)

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
