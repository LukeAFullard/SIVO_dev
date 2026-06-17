import sys
import os
import textwrap

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../src')))

from sivo.core.dashboard import SivoDashboard
from sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "url": "../../air/index.html", "url_transition": "page-turn-enter"},
    {"label": "Land", "sublinks": [
        {"label": "Pressures", "url": "../issues/index.html", "url_transition": "page-turn-enter"},
        {"label": "State", "url": "../science/index.html", "url_transition": "page-turn-enter"},
        {"label": "Actions", "url": "index.html", "url_transition": "page-turn-enter"}
    ]},
    {"label": "Water", "url": "../../water/index.html", "url_transition": "page-turn-enter"}
]

dashboard = SivoDashboard(
    title="",
    columns=3,
    background_image_url="../../../assets/land/land_bg.png",
    background_image_opacity=0.15,
    background_image_size="50%",
    width="80%",
    mobile_width="90%",
    theme="transparent",
    gap="1rem",
    navigation_menu=nav_menu
)

desktop_grid = """
'banner banner banner'
'intro_text intro_text intro_text'
'card1 card2 card3'
'card4 card5 card6'
'birds birds birds'
"""

mobile_grid = """
'banner'
'intro_text'
'card1'
'card2'
'card3'
'card4'
'card5'
'card6'
'birds'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../../../assets/land/land_banner.png",
    col_span=3,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

intro_md_path = os.path.join(os.path.dirname(__file__), "md/help.md")
with open(intro_md_path, "r", encoding="utf-8") as f:
    intro_md = f.read()

dashboard.add_details_panel(
    block_id="intro_text",
    title="",
    placeholder=intro_md,
    col_span=3,
    grid_area="intro_text",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    fade_in=True,
    fade_start_time_ms=300,
    fade_duration_ms=2000,
    update_on_click=False
)

# Helper function to create a Sivo instance with a card
def create_card_sivo(id_str, title, value, body, color, url=None):
    wrapped_title = textwrap.wrap(title, width=18)
    display_title = wrapped_title[0] if wrapped_title else ""
    display_subtitle = wrapped_title[1] if len(wrapped_title) > 1 else ""

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
      <rect id="{id_str}" x="0" y="0" width="100" height="100" fill="none" />
    </svg>'''
    s = Sivo.from_string(svg, layout_size="100%", mobile_layout_size="100%", lock_canvas=True, disable_zoom_controls=True, disable_resizer=True, lock_scroll_bounds=True, lock_zoom_out=True, theme="transparent", render_mode="svg")
    s.map(id_str, color="transparent")
    s.add_card(element_id=id_str, title=display_title, subtitle=display_subtitle, value=value, body=body, left="0%", top="0%", width="100%", height="100%", shape="ellipse", bg_color=color, url=url, title_color="#ffffff", subtitle_color="#ffffff", body_color="#ffffff")
    return s

dashboard.add_sivo_block("card1", create_card_sivo("c1", "Reduce erosion", "", "Chat to Horizons’ Land Management Advisors for advice on erosion-prone land use. Consider retiring marginal land or planting poplar trees. Fence off and plant riparian margins to reduce soil loss into waterways.", "#007DA3", url="https://google.com"), col_span=1, grid_area="card1", min_height="250px")
dashboard.add_sivo_block("card2", create_card_sivo("c2", "Enhance biodiversity", "", "Fence off bush remnants to protect ecosystems from grazing stock. Plant native vegetation in riparian margins, gardens, or shelterbelts to attract native birds, lizards, and insects. Join community conservation groups or local habitat restoration efforts.", "#00A79E", url="https://google.com"), col_span=1, grid_area="card2", min_height="250px")
dashboard.add_sivo_block("card3", create_card_sivo("c3", "Manage nutrients wisely", "", "Establish buffer strips, cover crops, or constructed wetlands to treat excess nutrients. Use slow-release fertilisers and test soil nitrogen levels before applying fertilisers. Line effluent ponds, and irrigate pasture only when conditions are optimal.", "#459461", url="https://google.com"), col_span=1, grid_area="card3", min_height="250px")
dashboard.add_sivo_block("card4", create_card_sivo("c4", "Strengthen biosecurity", "", "Report pest plants and animals to Horizons’ Pest Management team. Clean boats and other equipment thoroughly to prevent the spread of freshwater pests. Team up with neighbours or local environmental groups for coordinated pest control efforts.", "#283244", url="https://google.com"), col_span=1, grid_area="card4", min_height="250px")
dashboard.add_sivo_block("card5", create_card_sivo("c5", "Reach out", "", "to Horizons Visit horizons.govt.nz or call 0508 800 800 to explore how Horizons can support your land management goals. You might be eligible for funding through initiatives like the Priority Habitats Programme or SLUI. We also offer community grants for environmental projects, such as the Kanorau Koiora Taketake Indigenous Biodiversity Grant.", "#772981", url="https://google.com"), col_span=1, grid_area="card5", min_height="250px")
dashboard.add_sivo_block("card6", create_card_sivo("c6", "Check out", "", "our State of\nEnvironment Report", "#007DA3", url="https://www.horizons.govt.nz/HRC/media/Media/State-of-the-Environment-Horizons-Region-2025-Print.pdf"), col_span=1, grid_area="card6", min_height="250px")

dashboard.add_html_block(
    block_id="birds",
    html_content='<div style="display:flex; justify-content:center; align-items:center; width:100%; height:100%;"><img src="../../../assets/land/birds.png" style="width:100%; height:100%; object-fit:contain; border-radius:10px;" /></div>',
    col_span=3,
    grid_area="birds"
)

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
