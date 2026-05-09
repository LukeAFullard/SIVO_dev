import sys
import os
import textwrap

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../..')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

fmus = [
    "Puketoi ki Tai",
    "Manawatū",
    "Rangitīkei-Turakina",
    "Waiopehu",
    "Kai Iwi",
    "Whangaehu",
    "Whanganui"
]

app = Sivo.from_svg(
    os.path.join(os.path.dirname(__file__), "sivo_template.svg"),
    enable_geocoder=True,
    geocode_provider="nominatim",
    geocode_country_codes="nz",
    geocoder_position="top-left",
    disable_zoom_controls=True,
    lock_canvas=True,
    disable_resizer=True,
    lock_zoom_out=True,
    lock_scroll_bounds=True,
    transparent_template_lines=True
)

app.add_svg_background_image(
    "nz_comms_map_04_zoomed_detailed.png",
    insert_after="background"
)

app.bind_geocoder_intersection(
    geojson_url="https://services1.arcgis.com/VuN78wcRdq1Oj69W/arcgis/rest/services/FMU_20210122/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=geojson",
    display_element_id="null", # Output handled by overlay, we just put null
    property_name="Name",
    no_result_text="Address not found in any FMU zone."
)

# Read the markdown
with open(os.path.join(os.path.dirname(__file__), "placeholder.md"), "r", encoding="utf-8") as f:
    md_content = f.read()

for fmu in fmus:
    slug = fmu.lower().replace(" ", "-").replace("ā", "a").replace("ī", "i")
    element_id = fmu.replace(" ", "_")
    app.map(
        element_id=element_id,
        url=f"fmu/{slug}/index.html",
        url_target="_self",
        url_transition="page-turn-enter",
        hover_color="lightgray",
        tooltip=fmu,
        glow=True,
        markdown=md_content
    )

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "url": "../../air/index.html", "url_transition": "page-turn-enter"},
    {"label": "Land", "url": "../../land/index.html", "url_transition": "page-turn-enter"},
    {"label": "Water", "sublinks": [
        {"label": "Issues", "url": "../issues/index.html", "url_transition": "page-turn-enter"},
        {"label": "Science", "url": "index.html", "url_transition": "page-turn-enter"},
        {"label": "How to help", "url": "../help/index.html", "url_transition": "page-turn-enter"}
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
'search map map'
'markdown map map'
"""

mobile_grid = """
'banner'
'search'
'markdown'
'map'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../water_banner.png",
    col_span=3,
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
    show_element_name=False
)

dashboard.add_geocoder_block(
    block_id="search",
    col_span=1,
    grid_area="search",
    min_height="50px",
    overflow_visible=True
)

dashboard.add_sivo_block("map", app, col_span=2, grid_area="map", min_height="500px")

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.to_html(output_path=output_file)
print(f"Science Dashboard generated at {output_file}")
