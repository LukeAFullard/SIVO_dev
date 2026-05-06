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
    width="100%",
    background_image_url="../water_bg.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    theme="transparent",
    gap="1rem",
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

    # Add an invisible but hit-testable rectangle on top for interaction and outline
    sivo_app.add_shape("rect", {
        "id": "img_interact",
        "name": "img_interact",
        "x": str(offset),
        "y": str(offset),
        "width": str(size),
        "height": str(size),
        "fill": "rgba(255,255,255,0.01)", # ECharts hit testing requires non-transparent!
        "rx": "5",
        "ry": "5"
    })

    # Map the interactive layer, adding a bold border and glow on hover
    sivo_app.map(
        "img_interact",
        tooltip=icon["hover"],
        markdown=icon["md"],
        color="rgba(255,255,255,0.01)",   # Keep it mostly invisible but hit-testable
        border_color="transparent",       # No border by default
        border_width=3,                   # Give it thickness so hover is visible
        hover_color="rgba(0,0,0,0.05)",   # Slight tint on hover
        glow=True                         # Shadow/glow on hover
    )

    dashboard.add_sivo_block(block_id=icon["id"], sivo_app=sivo_app, col_span=1, grid_area=icon["id"], overflow_visible=True)

# Left details panel (4 columns now)
dashboard.add_details_panel(
    block_id="details",
    title="",
    placeholder="Select an issue above to learn more.",
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
