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
        {"label": "Issues", "url": "../issues/index.html", "url_transition": "page-turn-enter"},
        {"label": "Science", "url": "../science/index.html", "url_transition": "page-turn-enter"},
        {"label": "How to help", "url": "index.html", "url_transition": "page-turn-enter"}
    ]}
]

dashboard = SivoDashboard(
    title="",
    columns=3,
    background_image_url="../water_bg.png",
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
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)


with open(os.path.join(os.path.dirname(__file__), 'text.md'), 'r') as f:
    intro_markdown = f.read()

dashboard.add_details_panel(
    block_id="intro_text",
    title="",
    placeholder=intro_markdown,
    col_span=3,
    grid_area="intro_text",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    fade_in=True,
    fade_start_time_ms=300,
    fade_duration_ms=2000
)

dashboard.add_image_block(

    block_id="banner",
    image_url="../water_banner.png",
    col_span=3,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

# Helper function to create a Sivo instance with a card
def create_card_sivo(id_str, title, value, body, bg_color):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
      <rect id="{id_str}" x="0" y="0" width="100" height="100" fill="none" />
    </svg>'''
    s = Sivo.from_string(svg, layout_size="100%", mobile_layout_size="100%", lock_canvas=True, disable_zoom_controls=True, disable_resizer=True, lock_scroll_bounds=True, lock_zoom_out=True)
    s.add_card(element_id=id_str, title=title, value=value, body=body, left="0%", top="0%", width="100%", height="100%", shape="ellipse", bg_color=bg_color, border_color=bg_color, title_color="#ffffff", value_color="#ffffff", body_color="#ffffff")
    return s

dashboard.add_sivo_block("card1", create_card_sivo("c1", "Volunteer", "Join us", "Sign up for weekend cleanups.", "#007DA3"), col_span=1, grid_area="card1", min_height="250px")
dashboard.add_sivo_block("card2", create_card_sivo("c2", "Donate", "$50", "Your donation helps us plant more trees.", "#00A79E"), col_span=1, grid_area="card2", min_height="250px")
dashboard.add_sivo_block("card3", create_card_sivo("c3", "Report", "1-800", "Report illegal dumping in waterways.", "#459461"), col_span=1, grid_area="card3", min_height="250px")
dashboard.add_sivo_block("card4", create_card_sivo("c4", "Educate", "Learn", "Read our guides on water conservation.", "#283244"), col_span=1, grid_area="card4", min_height="250px")
dashboard.add_sivo_block("card5", create_card_sivo("c5", "Reduce", "Save", "Tips on reducing daily water usage.", "#772981"), col_span=1, grid_area="card5", min_height="250px")
dashboard.add_sivo_block("card6", create_card_sivo("c6", "Advocate", "Speak up", "Contact your local representatives.", "#007DA3"), col_span=1, grid_area="card6", min_height="250px")

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.to_html(output_path=output_file)
print(f"Help Dashboard generated at {output_file}")
