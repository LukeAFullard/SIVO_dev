import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

dashboard = SivoDashboard(
    title="",
    columns=4,
    theme="transparent",
    gap="tight"
)

desktop_grid = """
'icon1 icon2 icon3 icon4'
'markdown markdown markdown markdown'
"""

mobile_grid = """
'icon1 icon2'
'icon3 icon4'
'markdown markdown'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

icons = [
    {"id": "icon1", "img": "../../../assets/air/air_icon1.png", "hover": "Air Icon 1", "md_file": "md2/icon1.md"},
    {"id": "icon2", "img": "../../../assets/air/air_icon2.png", "hover": "Air Icon 2", "md_file": "md2/icon2.md"},
    {"id": "icon3", "img": "../../../assets/air/air_icon3.png", "hover": "Air Icon 3", "md_file": "md2/icon3.md"},
    {"id": "icon4", "img": "../../../assets/air/air_icon4.png", "hover": "Air Icon 4", "md_file": "md2/icon4.md"}
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

    size = 100
    offset = 0

    sivo_app.add_image_rect(
        element_id="img_vis",
        image_url=icon["img"],
        width=str(size),
        height=str(size),
        x=str(offset),
        y=str(offset),
        preserve_aspect_ratio="xMidYMid meet"
    )

    blank_name = " "

    sivo_app.add_shape("rect", {
        "id": "img_interact",
        "name": blank_name,
        "x": str(offset),
        "y": str(offset),
        "width": str(size),
        "height": str(size),
        "fill": "rgba(255,255,255,0.01)"
    })

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

dashboard.add_details_panel(
    block_id="markdown",
    title="",
    placeholder="Click an icon above to view details.",
    col_span=4,
    grid_area="markdown",
    background_color="transparent",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=300,
    fade_duration_ms=2000
)

output_file = os.path.join(os.path.dirname(__file__), "sub_dashboard.html")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
