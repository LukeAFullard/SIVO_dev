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
    {"label": "Land", "url": "../../land/index.html", "url_transition": "page-turn-enter"},
    {"label": "Water", "sublinks": [
        {"label": "Pressures", "url": "../issues/index.html", "url_transition": "page-turn-enter"},
        {"label": "State", "url": "../science/index.html", "url_transition": "page-turn-enter"},
        {"label": "Actions", "url": "index.html", "url_transition": "page-turn-enter"}
    ]}
]

dashboard = SivoDashboard(
    title="",
    columns=3,
    background_image_url="../../../assets/water/water_bg.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    width="80%",
    mobile_width="100%",
    theme="transparent",
    gap="1rem",
    navigation_menu=nav_menu
)

desktop_grid = """
'banner banner banner'
'intro_text intro_text intro_text'
'card1 card2 card3'
'card4 card5 card6'
'footer_image footer_image footer_image'
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
'footer_image'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../../../assets/water/water_banner.png",
    col_span=3,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

intro_md_path = os.path.join(os.path.dirname(__file__), "intro.md")
with open(intro_md_path, "r") as f:
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

dashboard.add_sivo_block("card1", create_card_sivo("c1", "Take action on-farm", "", "Seek guidance from Horizons to reduce\ncontaminants entering waterways. Learn\nmore about on-farm mitigations at\nlandscapedna.org.", "#007DA3", url="https://ourlandandwater.nz/fep-actions/"), col_span=1, grid_area="card1", min_height="250px")
dashboard.add_sivo_block("card2", create_card_sivo("c2", "Get involved", "", "Join a local Catchment Care\nGroup to support community\nled efforts to improve\nwater quality.", "#00A79E", url="https://www.cca.nz/"), col_span=1, grid_area="card2", min_height="250px")
dashboard.add_sivo_block("card3", create_card_sivo("c3", "Help track fish passage barriers", "", "Download the NIWA Fish\nPassage Assessment\nTool app to log barriers\nnationwide, and explore\nassessed structures in the\ntool’s database.", "#459461", url="https://niwa.co.nz/freshwater/fish-passage/fish-passage-assessment-tool"), col_span=1, grid_area="card3", min_height="250px")
dashboard.add_sivo_block("card4", create_card_sivo("c4", "Conserve water", "", "check your pipes for damage or leaks to avoid wasting water\n. Using water efficiently helps keep our river at healthy levels, which is essential for aquatic life to survive", "#283244"), col_span=1, grid_area="card4", min_height="250px")
dashboard.add_sivo_block("card5", create_card_sivo("c5", "Maintain Septic Systems", "", "If you are not on a town sewage system, ensure your septic tank is well-maintained and not leaking. Leaky septic systems are a common source of excess nitrogen in our waterways", "#772981"), col_span=1, grid_area="card5", min_height="250px")
dashboard.add_sivo_block("card6", create_card_sivo("c6", "Check out", "", "our State of\nEnvironment Report", "#007DA3", url="https://www.horizons.govt.nz/HRC/media/Media/State-of-the-Environment-Horizons-Region-2025-Print.pdf"), col_span=1, grid_area="card6", min_height="250px")

dashboard.add_image_block(
    block_id="footer_image",
    image_url="../../../assets/water/fishbanner.png",
    col_span=3,
    grid_area="footer_image",
    object_fit="contain",
    border_radius="0px"
)

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file)
print(f"Help Dashboard generated at {output_file}")
