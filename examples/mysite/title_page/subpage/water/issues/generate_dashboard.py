import sys
import os

# fix sys path to include root src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../..')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "url": "../../air/index.html", "url_transition": "page-turn-enter"},
    {"label": "Land", "url": "../../land/index.html", "url_transition": "page-turn-enter"},
    {"label": "Water", "sublinks": [
        {"label": "Issues", "url": "index.html", "url_transition": "page-turn-enter"},
        {"label": "Science", "url": "../science/index.html", "url_transition": "page-turn-enter"},
        {"label": "How to help", "url": "../help/index.html", "url_transition": "page-turn-enter"}
    ]}
]

dashboard = SivoDashboard(
    title="",
    columns=6,
    background_image_url="../water_bg.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    theme="transparent",
    gap="1rem",
    navigation_menu=nav_menu
)

desktop_grid = """
'banner banner banner banner banner banner'
'subtitle subtitle subtitle subtitle subtitle subtitle'
'icon1 icon2 icon3 icon4 icon5 icon6'
'details details details image image image'
"""

mobile_grid = """
'banner banner'
'subtitle subtitle'
'icon1 icon2'
'icon3 icon4'
'icon5 icon6'
'details details'
'image image'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../water_banner.png",
    col_span=6,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

dashboard.add_text_block(
    block_id="subtitle",
    text="Issues with Water Quality in the region",
    col_span=6,
    grid_area="subtitle",
    font_size="24px"
)

# Define icons and their tooltips/markdown content
icons = [
    {"id": "icon1", "img": "20221123_OrangaWai_IconEcoli.png", "hover": "E. <i>coli</i>", "md": "## E. coli\n\nPlaceholder text about E. coli issues."},
    {"id": "icon2", "img": "20221123_OrangaWai_IconSuspendedSediment.png", "hover": "Suspended sediment", "md": "## Suspended sediment\n\nPlaceholder text about suspended sediment issues."},
    {"id": "icon3", "img": "20221123_OrangaWai_IconN.png", "hover": "Nitrogen", "md": "## Nitrogen\n\nPlaceholder text about nitrogen issues."},
    {"id": "icon4", "img": "20221123_OrangaWai_IconP.png", "hover": "Phosphorus", "md": "## Phosphorus\n\nPlaceholder text about phosphorus issues."},
    {"id": "icon5", "img": "20221123_OrangaWai_IconChlA.png", "hover": "Algae", "md": "## Algae\n\nPlaceholder text about algae issues."},
    {"id": "icon6", "img": "20221123_OrangaWai_IconAquaticLife.png", "hover": "Invertebrates", "md": "## Invertebrates\n\nPlaceholder text about aquatic life issues."}
]

for icon in icons:
    # We will create a tiny Sivo app for each icon
    sivo_app = Sivo.from_string(
        '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"></svg>',
        lock_canvas=True,
        disable_resizer=True,
        disable_zoom_controls=True,
        lock_zoom_out=True,
        lock_scroll_bounds=True
    )
    sivo_app.add_image_rect(
        element_id="img",
        image_url=icon["img"],
        width="100",
        height="100",
        preserve_aspect_ratio="xMidYMid meet"
    )
    sivo_app.map("img", tooltip=icon["hover"], markdown=icon["md"])
    dashboard.add_sivo_block(block_id=icon["id"], sivo_app=sivo_app, col_span=1, grid_area=icon["id"])

# Left details panel
dashboard.add_details_panel(
    block_id="details",
    title="",
    placeholder="Select an issue above to learn more.",
    col_span=3,
    grid_area="details"
)

# Right image
dashboard.add_image_block(
    block_id="image",
    image_url="koura-blue.png",
    col_span=3,
    grid_area="image",
    object_fit="contain"
)

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
