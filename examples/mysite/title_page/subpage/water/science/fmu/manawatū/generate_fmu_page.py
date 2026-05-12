import sys
import os
import json

# fix sys path to include root src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../../../src')))

from sivo.core.dashboard import SivoDashboard
from sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "url": "../../../../air/index.html", "url_transition": "page-turn-enter"},
    {"label": "Land", "url": "../../../../land/index.html", "url_transition": "page-turn-enter"},
    {"label": "Water", "sublinks": [
        {"label": "Issues", "url": "../../../issues/index.html", "url_transition": "page-turn-enter"},
        {"label": "Science", "url": "../../index.html", "url_transition": "page-turn-enter"},
        {"label": "How to help", "url": "../../../help/index.html", "url_transition": "page-turn-enter"}
    ]}
]

dashboard = SivoDashboard(
    title="",
    columns=8,
    width="80%",
    mobile_width="100%",
    background_image_url="../../../../../assets/water/water_bg.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    theme="transparent",
    gap="tight",
    navigation_menu=nav_menu
)

desktop_grid = """
'banner banner banner banner banner banner banner banner'
'. icon1 icon2 icon3 icon4 icon5 icon6 .'
'details details details details map map map map'
'gap1 gap1 gap1 gap1 map map map map'
'state state state state trend trend trend trend'
'button_state button_state button_state button_state button_trend button_trend button_trend button_trend'
"""

mobile_grid = """
'banner banner'
'icon1 icon2'
'icon3 icon4'
'icon5 icon6'
'map map'
'details details'
'gap1 gap1'
'state state'
'button_state button_state'
'gap2 gap2'
'trend trend'
'button_trend button_trend'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../../../../../assets/water/water_banner.png",
    col_span=8,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

dashboard.add_html_block(block_id="gap1", html_content="<div style='height: 20px;'></div>", col_span=4, grid_area="gap1")
dashboard.add_html_block(block_id="gap2", html_content="<div style='height: 20px;'></div>", col_span=4, grid_area="gap2")

icons = [
    {"id": "icon1", "img": "../../../../../assets/water/20221123_OrangaWai_IconEcoli.png", "hover": "E. <i>coli</i>", "md_file": "md/ecoli.md"},
    {"id": "icon2", "img": "../../../../../assets/water/20221123_OrangaWai_IconSuspendedSediment.png", "hover": "Suspended sediment", "md_file": "md/suspended_sediment.md"},
    {"id": "icon3", "img": "../../../../../assets/water/20221123_OrangaWai_IconN.png", "hover": "Nitrogen", "md_file": "md/nitrogen.md"},
    {"id": "icon4", "img": "../../../../../assets/water/20221123_OrangaWai_IconP.png", "hover": "Phosphorus", "md_file": "md/phosphorus.md"},
    {"id": "icon5", "img": "../../../../../assets/water/20221123_OrangaWai_IconChlA.png", "hover": "Algae", "md_file": "md/algae.md"},
    {"id": "icon6", "img": "../../../../../assets/water/20221123_OrangaWai_IconAquaticLife.png", "hover": "Invertebrates", "md_file": "md/invertebrates.md"}
]

# We will populate md, state_md, trend_md
with open(os.path.join(os.path.dirname(__file__), "md/details_placeholder.md"), "r", encoding="utf-8") as f:
    details_default = f.read()

with open(os.path.join(os.path.dirname(__file__), "md/state_placeholder.md"), "r", encoding="utf-8") as f:
    state_default = f.read()

with open(os.path.join(os.path.dirname(__file__), "md/trend_placeholder.md"), "r", encoding="utf-8") as f:
    trend_default = f.read()

dashboard.add_details_panel(
    block_id="details",
    title="Details",
    placeholder=details_default,
    col_span=4,
    grid_area="details",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    fade_in=True,
    payload_key="details_md"
)

dashboard.add_details_panel(
    block_id="state",
    title="STATE",
    placeholder=state_default,
    col_span=4,
    grid_area="state",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    fade_in=True,
    payload_key="state_md"
)

dashboard.add_details_panel(
    block_id="trend",
    title="TREND",
    placeholder=trend_default,
    col_span=4,
    grid_area="trend",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    fade_in=True,
    payload_key="trend_md"
)

with open(os.path.join(os.path.dirname(__file__), "md/state_popup.md"), "r", encoding="utf-8") as f:
    state_popup = f.read()

dashboard.add_overlay_button(block_id="button_state", label="Click for more information", default_text=state_popup, payload_key="state_how", button_color="#772981", col_span=4, grid_area="button_state", panel_width="90%", panel_height="90%")

dashboard.add_overlay_button(block_id="button_trend", label="Click for more information", default_text="Default text for How we measure TREND", payload_key="trend_how", button_color="#772981", col_span=4, grid_area="button_trend", panel_width="90%", panel_height="90%")

for icon in icons:
    md_path = os.path.join(os.path.dirname(__file__), icon["md_file"])
    with open(md_path, "r", encoding="utf-8") as f:
        icon["md"] = f.read()

    icon["state_md"] = f"### State for {icon['hover']}\nThis is the state data for {icon['hover']}."
    icon["trend_md"] = f"### Trend for {icon['hover']}\nThis is the trend data for {icon['hover']}."
    icon["state_how"] = f"How we measure STATE for {icon['hover']}"
    icon["state_understand"] = f"Understanding STATE maps for {icon['hover']}"
    icon["trend_how"] = f"How we measure TREND for {icon['hover']}"
    icon["trend_understand"] = f"Understanding TREND maps for {icon['hover']}"

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

    blank_name = " "

    sivo_app.add_shape("rect", {
        "id": "img_interact",
        "name": blank_name,
        "x": str(offset),
        "y": str(offset),
        "width": str(size),
        "height": str(size),
        "fill": "rgba(255,255,255,0.01)",
        "rx": "5",
        "ry": "5"
    })

    payload = {
        "details_md": icon["md"],
        "state_md": icon["state_md"],
        "trend_md": icon["trend_md"],
        "state_how": icon["state_how"],
        "state_understand": icon["state_understand"],
        "trend_how": icon["trend_how"],
        "trend_understand": icon["trend_understand"]
    }

    sivo_app.map(
        blank_name,
        tooltip=icon["hover"],
        callback_payload=payload,
        color="rgba(255,255,255,0.01)",
        border_color="transparent",
        border_width=3,
        hover_color="transparent",
        glow=False
    )

    dashboard.add_sivo_block(block_id=icon["id"], sivo_app=sivo_app, col_span=1, grid_area=icon["id"], overflow_visible=True, min_height="100px")


with open(os.path.join(os.path.dirname(__file__), "md/map_placeholder.html"), "r", encoding="utf-8") as f:
    map_html = f.read()

dashboard.add_html_block(block_id="map", html_content=f"<div id='map_container' style='background:#f1f5f9; width:100%; height:100%; min-height:600px; display:flex; align-items:center; justify-content:center; border-radius:10px;'>{map_html}</div>", col_span=4, grid_area="map")

custom_js = None

output_file = os.path.join(os.path.dirname(__file__), "index.html")

dashboard.to_html(output_path=output_file, custom_js=custom_js)
print(f"FMU Dashboard generated at {output_file}")
