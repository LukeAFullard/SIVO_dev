import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../src')))

from sivo.core.dashboard import SivoDashboard
from sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../index.html"},
    {"label": "Air", "url": "../../air/index.html"},
    {"label": "Land", "sublinks": [
        {"label": "Overview", "url": "../index.html"},
        {"label": "Pressures", "url": "../issues/index.html"},
        {"label": "State", "url": "../science/index.html"},
        {"label": "Actions", "url": "index.html"}
    ]},
    {"label": "Water", "url": "../../water/index.html"}
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
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
      <rect id="{id_str}" x="0" y="0" width="100" height="100" fill="none" />
    </svg>'''
    s = Sivo.from_string(svg, layout_size="100%", mobile_layout_size="100%", lock_canvas=True, disable_zoom_controls=True, disable_resizer=True, lock_scroll_bounds=True, lock_zoom_out=True, theme="transparent", render_mode="svg")
    s.map(id_str, color="transparent")
    s.add_card(element_id=id_str, title=title, subtitle="", value=value, body=body, left="0%", top="0%", width="100%", height="100%", shape="ellipse", bg_color=color, url=url, title_color="#ffffff", subtitle_color="#ffffff", body_color="#ffffff", html_body=True)
    return s

dashboard.add_sivo_block("card1", create_card_sivo("c1", "Reduce erosion", "", 'Chat to Horizons’ <a href="https://www.horizons.govt.nz/managing-natural-resources/land#:~:text=Get%20in%20touch%20with%20your%20LMA,LAND%20MANAGEMENT%20TEAMS%20MAP" target="_blank" style="color:white; text-decoration:underline;">Land Management Advisors</a> for advice on erosion-prone land use.', "#007DA3"), col_span=1, grid_area="card1", min_height="250px")
dashboard.add_sivo_block("card2", create_card_sivo("c2", "Enhance biodiversity", "", 'Protect and restore local biodiversity by fencing bush remnants, planting native vegetation, and joining <a href="https://enm.org.nz/" target="_blank" style="color:white; text-decoration:underline;">community conservation efforts</a>.', "#00A79E"), col_span=1, grid_area="card2", min_height="250px")
dashboard.add_sivo_block("card3", create_card_sivo("c3", "Manage nutrients wisely", "", 'Reach out to Horizons’ <a href="https://www.horizons.govt.nz/managing-natural-resources/rural-advice" target="_blank" style="color:white; text-decoration:underline;">Rural Advice team</a> for advice on improving on-farm nutrient management.', "#459461"), col_span=1, grid_area="card3", min_height="250px")
dashboard.add_sivo_block("card4", create_card_sivo("c4", "Strengthen biosecurity", "", 'Report pest plants and animals to Horizons’ <a href="https://www.horizons.govt.nz/managing-natural-resources/plant-animal-pests" target="_blank" style="color:white; text-decoration:underline;">Pest Management teams</a> and work with neighbours on coordinated pest control.', "#283244"), col_span=1, grid_area="card4", min_height="250px")
dashboard.add_sivo_block("card5", create_card_sivo("c5", "Apply for a grant", "", 'You might be eligible for funding through Horizons initiatives such as the <a href="https://www.horizons.govt.nz/managing-natural-resources/biodiversity-and-totara-reserve/priority-habitats-programme" target="_blank" style="color:white; text-decoration:underline;">Priority Habitats Programme</a> or <a href="https://www.horizons.govt.nz/managing-natural-resources/land#:~:text=TEAM%20UPDATE%20%232-,Sustainable%20Land%20Use%20Initiative%20(SLUI),FUNDING%20HANDOUT%20SHEET,-Get%20in%20touch" target="_blank" style="color:white; text-decoration:underline;">SLUI</a>, or through a <a href="https://www.horizons.govt.nz/about-our-region-and-council/grants-and-sponsorship/biodiversity-grants" target="_blank" style="color:white; text-decoration:underline;">community grant</a>.', "#772981"), col_span=1, grid_area="card5", min_height="250px")
dashboard.add_sivo_block("card6", create_card_sivo("c6", "Learn more", "", 'Explore the state of the region’s environment in more detail in the report: <a href="https://www.horizons.govt.nz/HRC/media/Media/State-of-the-Environment-Horizons-Region-2025.pdf" target="_blank" style="color:white; text-decoration:underline;">Te Oranga o te Taiao | State of the Environment – Horizons Region 2025</a>.', "#007DA3"), col_span=1, grid_area="card6", min_height="250px")

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
