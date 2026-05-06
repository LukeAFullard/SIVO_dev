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

# The rest of the dashboard should be fully wide, but the icon row thinner.
# We go to 8 columns and have an empty icon on each end.
dashboard = SivoDashboard(
    title="",
    columns=8,
    width="80%",
    mobile_width="100%",
    background_image_url="../water_bg.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    theme="transparent",
    gap="tight",
    navigation_menu=nav_menu
)

desktop_grid = """
'banner banner banner banner banner banner banner banner'
'subtitle subtitle subtitle subtitle subtitle subtitle subtitle subtitle'
'. icon1 icon2 icon3 icon4 icon5 icon6 .'
'details details details details image image image image'
"""

# For mobile, we probably still want 2 columns for icons
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
    col_span=8,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

dashboard.add_text_block(
    block_id="subtitle",
    text="Issues with Water Quality in the region",
    col_span=8,
    grid_area="subtitle",
    font_size="24px",
    min_height="auto"
)

# Define icons and their tooltips/markdown content files
icons = [
    {"id": "icon1", "img": "20221123_OrangaWai_IconEcoli.png", "hover": "E. <i>coli</i>", "md_file": "md/ecoli.md"},
    {"id": "icon2", "img": "20221123_OrangaWai_IconSuspendedSediment.png", "hover": "Suspended sediment", "md_file": "md/suspended_sediment.md"},
    {"id": "icon3", "img": "20221123_OrangaWai_IconN.png", "hover": "Nitrogen", "md_file": "md/nitrogen.md"},
    {"id": "icon4", "img": "20221123_OrangaWai_IconP.png", "hover": "Phosphorus", "md_file": "md/phosphorus.md"},
    {"id": "icon5", "img": "20221123_OrangaWai_IconChlA.png", "hover": "Algae", "md_file": "md/algae.md"},
    {"id": "icon6", "img": "20221123_OrangaWai_IconAquaticLife.png", "hover": "Invertebrates", "md_file": "md/invertebrates.md"}
]

for icon in icons:
    md_path = os.path.join(os.path.dirname(__file__), icon["md_file"])
    with open(md_path, "r", encoding="utf-8") as f:
        icon["md"] = f.read()

for icon in icons:
    sivo_app = Sivo.from_string(
        '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"></svg>',
        lock_canvas=True,
        disable_resizer=True,
        disable_zoom_controls=True,
        lock_zoom_out=True,
        lock_scroll_bounds=True
    )

    size = 75
    offset = (100 - size) / 2

    sivo_app.add_image_rect(
        element_id="img_vis",
        image_url=icon["img"],
        width=str(size),
        height=str(size),
        x=str(offset),
        y=str(offset),
        preserve_aspect_ratio="xMidYMid meet"
    )

    # Add an invisible but hit-testable rectangle on top for interaction and outline.
    # Set the name to " " so that the Details Panel header appears blank, as requested.
    blank_name = " "

    sivo_app.add_shape("rect", {
        "id": "img_interact",
        "name": blank_name,
        "x": str(offset),
        "y": str(offset),
        "width": str(size),
        "height": str(size),
        "fill": "rgba(255,255,255,0.01)", # ECharts hit testing requires non-transparent!
        "rx": "5",
        "ry": "5"
    })

    # Map the interactive layer using the blank name. Set hover_color to transparent.
    sivo_app.map(
        blank_name,
        tooltip=icon["hover"],
        markdown=icon["md"],
        color="rgba(255,255,255,0.01)",   # Keep it mostly invisible but hit-testable
        border_color="transparent",       # No border by default
        border_width=3,                   # Give it thickness so hover is visible
        hover_color="transparent",        # No highlight on hover
        glow=False                        # No shadow/glow on hover to prevent highlight
    )

    dashboard.add_sivo_block(block_id=icon["id"], sivo_app=sivo_app, col_span=1, grid_area=icon["id"], overflow_visible=True, min_height="100px")

# Left details panel (4 columns now)
placeholder_path = os.path.join(os.path.dirname(__file__), "md/placeholder.md")
with open(placeholder_path, "r", encoding="utf-8") as f:
    placeholder_text = f.read()

dashboard.add_details_panel(
    block_id="details",
    title="",
    placeholder=placeholder_text,
    col_span=4,
    grid_area="details"
)

# Right image (4 columns now)
dashboard.add_image_block(
    block_id="image",
    image_url="koura-blue.png",
    col_span=4,
    grid_area="image",
    object_fit="contain"
)

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
