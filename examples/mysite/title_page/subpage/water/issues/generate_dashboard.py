import sys
import os

# fix sys path to include root src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../..')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../index.html"},
    {"label": "Air", "url": "../../air/index.html"},
    {"label": "Land", "url": "../../land/index.html"},
    {"label": "Water", "sublinks": [
        {"label": "Overview", "url": "../index.html"},
        {"label": "Pressures", "url": "index.html"},
        {"label": "State", "url": "../science/index.html"},
        {"label": "Actions", "url": "../help/index.html"}
    ]}
]

# The rest of the dashboard should be fully wide, but the icon row thinner.
# We go to 8 columns and have an empty icon on each end.
dashboard = SivoDashboard(
    title="",
    columns=8,
    width="80%",
    mobile_width="100%",
    background_image_url="../../../assets/water/water_bg.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    theme="transparent",
    gap="tight",
    navigation_menu=nav_menu
)

desktop_grid = """
'banner banner banner banner banner banner banner banner'
'. icon1 icon2 icon3 icon4 icon5 icon6 .'
'details details details details image image image image'
"""

# For mobile, we probably still want 2 columns for icons
mobile_grid = """
'banner banner'
'icon1 icon2'
'icon3 icon4'
'icon5 icon6'
'details details'
'image image'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../../../assets/water/water_banner.png",
    col_span=8,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

# Define icons and their tooltips/markdown content files
icons = [
    {"id": "icon1", "img": "../../../assets/water/20221123_OrangaWai_IconEcoli.png", "hover": "E. <i>coli</i>", "md_file": "md/ecoli.md"},
    {"id": "icon2", "img": "../../../assets/water/20221123_OrangaWai_IconSuspendedSediment.png", "hover": "Suspended sediment", "md_file": "md/suspended_sediment.md"},
    {"id": "icon3", "img": "../../../assets/water/20221123_OrangaWai_IconN.png", "hover": "Nitrogen", "md_file": "md/nitrogen.md"},
    {"id": "icon4", "img": "../../../assets/water/20221123_OrangaWai_IconP.png", "hover": "Phosphorus", "md_file": "md/phosphorus.md"},
    {"id": "icon5", "img": "../../../assets/water/20221123_OrangaWai_IconChlA.png", "hover": "Algae", "md_file": "md/algae.md"},
    {"id": "icon6", "img": "../../../assets/water/20221123_OrangaWai_IconAquaticLife.png", "hover": "Invertebrates", "md_file": "md/invertebrates.md"}
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

    sivo_app.add_shape("circle", {
        "id": "img_interact",
        "name": blank_name,
        "cx": str(offset + size / 2),
        "cy": str(offset + size / 2),
        "r": str(size / 2),
        "fill": "rgba(255,255,255,0.01)"
    })

    # map img_vis
    sivo_app.map(
        "img_vis",
        tooltip=icon["hover"],
        markdown=icon["md"],
        color="rgba(255,255,255,0.01)",
        border_color="transparent",
        border_width=3,
        hover_color="transparent",
        glow=False,
        fade_pulse=False
    )

    # map blank_name for pulsing
    sivo_app.map(
        blank_name,
        tooltip=icon["hover"],
        markdown=icon["md"],
        color="transparent",
        border_color="#ccffcc",
        border_width=8,
        hover_color="transparent",
        glow=True,
        fade_pulse=True
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
    grid_area="details",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    fade_in=True,
    fade_start_time_ms=300,
    fade_duration_ms=2000
)

# Right image (4 columns now)
dashboard.add_image_block(
    block_id="image",
    image_url="../../../assets/water/koura-blue.png",
    col_span=4,
    grid_area="image",
    object_fit="contain"
)

output_file = os.path.join(os.path.dirname(__file__), "index.html")

dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
