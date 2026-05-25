import sys
import os
import json
import re

# fix sys path to include root src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../../../src')))

from sivo.core.dashboard import SivoDashboard
from sivo.core.sivo import Sivo

base_dir = os.path.dirname(__file__)
json_path = os.path.abspath(os.path.join(base_dir, "../../state_summary.json"))

with open(json_path, 'r', encoding='utf-8') as f:
    state_summary = json.load(f)

parameters_state = {
    "Sediment": {"json_key": "Visual Clarity", "grades": ["A", "B", "C", "D"]},
    "Algae": {"json_key": "Chlorophyll A", "grades": ["A", "B", "C", "D"]},
    "Phosphorus": {"json_key": "DRP", "grades": ["A", "B", "C", "D"]},
    "ecoli": {"json_key": "E coli", "grades": ["A", "B", "C", "D", "E"]},
    "inverts": {"json_key": "MCI", "grades": ["A", "B", "C", "D"]},
}

for folder, p_info in parameters_state.items():
    template_path = os.path.join(base_dir, f"md/{folder}/state_placeholder_TEMPLATE.md")
    output_path = os.path.join(base_dir, f"md/{folder}/state_placeholder.md")

    fmu_data = state_summary["FMUs"]["Whangaehu"].get(p_info["json_key"])
    region_data = state_summary["Region"][p_info["json_key"]]
    fmu_sites = fmu_data["Total Sites for Attribute"] if fmu_data else 0

    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    template_content = template_content.replace("|NUMBER_SITES|", str(fmu_sites))

    for grade in p_info["grades"]:
        fmu_pct = float(fmu_data["Grades"][grade]["Percentage"]) if fmu_data and grade in fmu_data["Grades"] else 0.0
        fmu_count = fmu_data["Grades"][grade]["Count"] if fmu_data and grade in fmu_data["Grades"] else 0
        region_pct = float(region_data["Grades"][grade]["Percentage"])

        template_content = template_content.replace(f"|FMU_{grade}_PCT|", f"{fmu_pct:.1f}")
        template_content = template_content.replace(f"|FMU_{grade}_COUNT|", str(fmu_count))
        template_content = template_content.replace(f"|REGION_{grade}_PCT|", f"{region_pct:.1f}")
        template_content = template_content.replace(f"|REGION_{grade}_COUNT|", str(region_data["Grades"][grade]["Count"]))

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template_content)

# Special case for Nitrogen
nitrogen_template_path = os.path.join(base_dir, "md/Nitrogen/state_placeholder_TEMPLATE.md")
nitrogen_output_path = os.path.join(base_dir, "md/Nitrogen/state_placeholder.md")

with open(nitrogen_template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

ammo_fmu_data = state_summary["FMUs"]["Whangaehu"]["Ammoniacal-N"]
ammo_region_data = state_summary["Region"]["Ammoniacal-N"]
nitrate_fmu_data = state_summary["FMUs"]["Whangaehu"]["Nitrate-N"]
nitrate_region_data = state_summary["Region"]["Nitrate-N"]
fmu_sites = ammo_fmu_data["Total Sites for Attribute"] # Assuming both are evaluated together

template_content = template_content.replace("|NUMBER_SITES|", str(fmu_sites))

for grade in ["A", "B", "C", "D"]:
    fmu_pct = float(ammo_fmu_data["Grades"][grade]["Percentage"])
    region_pct = float(ammo_region_data["Grades"][grade]["Percentage"])
    template_content = template_content.replace(f"|AMMO_FMU_{grade}_PCT|", f"{fmu_pct:.1f}")
    template_content = template_content.replace(f"|AMMO_FMU_{grade}_COUNT|", str(ammo_fmu_data["Grades"][grade]["Count"]))
    template_content = template_content.replace(f"|AMMO_REGION_{grade}_PCT|", f"{region_pct:.1f}")
    template_content = template_content.replace(f"|AMMO_REGION_{grade}_COUNT|", str(ammo_region_data["Grades"][grade]["Count"]))

    fmu_pct = float(nitrate_fmu_data["Grades"][grade]["Percentage"])
    region_pct = float(nitrate_region_data["Grades"][grade]["Percentage"])
    template_content = template_content.replace(f"|NITRATE_FMU_{grade}_PCT|", f"{fmu_pct:.1f}")
    template_content = template_content.replace(f"|NITRATE_FMU_{grade}_COUNT|", str(nitrate_fmu_data["Grades"][grade]["Count"]))
    template_content = template_content.replace(f"|NITRATE_REGION_{grade}_PCT|", f"{region_pct:.1f}")
    template_content = template_content.replace(f"|NITRATE_REGION_{grade}_COUNT|", str(nitrate_region_data["Grades"][grade]["Count"]))

with open(nitrogen_output_path, 'w', encoding='utf-8') as f:
    f.write(template_content)


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
'details details details map map map map map'
'gap1 gap1 gap1 map map map map map'
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
    {"id": "icon1", "img": "../../../../../assets/water/20221123_OrangaWai_IconEcoli.png", "hover": "E. <i>coli</i>", "md_dir": "md/ecoli", "map_file": "results/Map_E coli.html"},
    {"id": "icon2", "img": "../../../../../assets/water/20221123_OrangaWai_IconSuspendedSediment.png", "hover": "Suspended sediment", "md_dir": "md/Sediment", "map_file": "results/Map_Visual Clarity.html"},
    {"id": "icon3", "img": "../../../../../assets/water/20221123_OrangaWai_IconN.png", "hover": "Nitrogen", "md_dir": "md/Nitrogen", "map_file": "results/Map_Nitrate-N.html"},
    {"id": "icon4", "img": "../../../../../assets/water/20221123_OrangaWai_IconP.png", "hover": "Phosphorus", "md_dir": "md/Phosphorus", "map_file": "results/Map_DRP.html"},
    {"id": "icon5", "img": "../../../../../assets/water/20221123_OrangaWai_IconChlA.png", "hover": "Algae", "md_dir": "md/Algae", "map_file": "results/Map_Chlorophyll A.html"},
    {"id": "icon6", "img": "../../../../../assets/water/20221123_OrangaWai_IconAquaticLife.png", "hover": "Invertebrates", "md_dir": "md/inverts", "map_file": "results/Map_MCI.html"}
]

import json
with open(os.path.join(os.path.dirname(__file__), "../../trend_summary.json"), "r", encoding="utf-8") as f:
    trend_data = json.load(f)

parameters_trend = {
    "Sediment": "Visual Clarity",
    "Algae": "Chlorophyll A",
    "Phosphorus": "Dissolved Reactive Phosphorus",
    "ecoli": "E. coli",
    "inverts": "MCI (Macroinvertebrate Community Index)",
}

for folder, json_key in parameters_trend.items():
    fmu_data = trend_data['FMUs']['Whangaehu'].get(json_key)
    region_data = trend_data['Region'][json_key]

    template_path = os.path.join(os.path.dirname(__file__), f"md/{folder}/trend_placeholder_TEMPLATE.md")
    output_path = os.path.join(os.path.dirname(__file__), f"md/{folder}/trend_placeholder.md")

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    replacements = {
        '|NUMBER_SITES|': str(fmu_data['Total Sites for Parameter']) if fmu_data else '0',
        '|FMU_IMPROVING_PCT|': str(fmu_data['Categories']['Improving']['Percentage']) if fmu_data else '0.0',
        '|FMU_IMPROVING_COUNT|': str(fmu_data['Categories']['Improving']['Count']) if fmu_data else '0',
        '|FMU_INDETERMINATE_PCT|': str(fmu_data['Categories']['Indeterminate']['Percentage']) if fmu_data else '0.0',
        '|FMU_INDETERMINATE_COUNT|': str(fmu_data['Categories']['Indeterminate']['Count']) if fmu_data else '0',
        '|FMU_DEGRADING_PCT|': str(fmu_data['Categories']['Degrading']['Percentage']) if fmu_data else '0.0',
        '|FMU_DEGRADING_COUNT|': str(fmu_data['Categories']['Degrading']['Count']) if fmu_data else '0',
        '|REGION_IMPROVING_PCT|': str(region_data['Categories']['Improving']['Percentage']),
        '|REGION_IMPROVING_COUNT|': str(region_data['Categories']['Improving']['Count']),
        '|REGION_INDETERMINATE_PCT|': str(region_data['Categories']['Indeterminate']['Percentage']),
        '|REGION_INDETERMINATE_COUNT|': str(region_data['Categories']['Indeterminate']['Count']),
        '|REGION_DEGRADING_PCT|': str(region_data['Categories']['Degrading']['Percentage']),
        '|REGION_DEGRADING_COUNT|': str(region_data['Categories']['Degrading']['Count']),
    }

    for k, v in replacements.items():
        template_content = template_content.replace(k, v)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template_content)

# Special case for Nitrogen
nitrogen_trend_template_path = os.path.join(base_dir, "md/Nitrogen/trend_placeholder_TEMPLATE.md")
nitrogen_trend_output_path = os.path.join(base_dir, "md/Nitrogen/trend_placeholder.md")

with open(nitrogen_trend_template_path, "r", encoding="utf-8") as f:
    template_content = f.read()

ammo_fmu_data = trend_data['FMUs']['Whangaehu']["Ammoniacal Nitrogen (NH4)"]
ammo_region_data = trend_data['Region']["Ammoniacal Nitrogen (NH4)"]
nitrate_fmu_data = trend_data['FMUs']['Whangaehu']["Nitrate Nitrogen (NO3)"]
nitrate_region_data = trend_data['Region']["Nitrate Nitrogen (NO3)"]
fmu_sites = ammo_fmu_data['Total Sites for Parameter']

replacements = {
    '|NUMBER_SITES|': str(fmu_sites),
    '|AMMO_FMU_IMPROVING_PCT|': str(ammo_fmu_data['Categories']['Improving']['Percentage']),
    '|AMMO_FMU_IMPROVING_COUNT|': str(ammo_fmu_data['Categories']['Improving']['Count']),
    '|AMMO_FMU_INDETERMINATE_PCT|': str(ammo_fmu_data['Categories']['Indeterminate']['Percentage']),
    '|AMMO_FMU_INDETERMINATE_COUNT|': str(ammo_fmu_data['Categories']['Indeterminate']['Count']),
    '|AMMO_FMU_DEGRADING_PCT|': str(ammo_fmu_data['Categories']['Degrading']['Percentage']),
    '|AMMO_FMU_DEGRADING_COUNT|': str(ammo_fmu_data['Categories']['Degrading']['Count']),
    '|AMMO_REGION_IMPROVING_PCT|': str(ammo_region_data['Categories']['Improving']['Percentage']),
    '|AMMO_REGION_IMPROVING_COUNT|': str(ammo_region_data['Categories']['Improving']['Count']),
    '|AMMO_REGION_INDETERMINATE_PCT|': str(ammo_region_data['Categories']['Indeterminate']['Percentage']),
    '|AMMO_REGION_INDETERMINATE_COUNT|': str(ammo_region_data['Categories']['Indeterminate']['Count']),
    '|AMMO_REGION_DEGRADING_PCT|': str(ammo_region_data['Categories']['Degrading']['Percentage']),
    '|AMMO_REGION_DEGRADING_COUNT|': str(ammo_region_data['Categories']['Degrading']['Count']),

    '|NITRATE_FMU_IMPROVING_PCT|': str(nitrate_fmu_data['Categories']['Improving']['Percentage']),
    '|NITRATE_FMU_IMPROVING_COUNT|': str(nitrate_fmu_data['Categories']['Improving']['Count']),
    '|NITRATE_FMU_INDETERMINATE_PCT|': str(nitrate_fmu_data['Categories']['Indeterminate']['Percentage']),
    '|NITRATE_FMU_INDETERMINATE_COUNT|': str(nitrate_fmu_data['Categories']['Indeterminate']['Count']),
    '|NITRATE_FMU_DEGRADING_PCT|': str(nitrate_fmu_data['Categories']['Degrading']['Percentage']),
    '|NITRATE_FMU_DEGRADING_COUNT|': str(nitrate_fmu_data['Categories']['Degrading']['Count']),
    '|NITRATE_REGION_IMPROVING_PCT|': str(nitrate_region_data['Categories']['Improving']['Percentage']),
    '|NITRATE_REGION_IMPROVING_COUNT|': str(nitrate_region_data['Categories']['Improving']['Count']),
    '|NITRATE_REGION_INDETERMINATE_PCT|': str(nitrate_region_data['Categories']['Indeterminate']['Percentage']),
    '|NITRATE_REGION_INDETERMINATE_COUNT|': str(nitrate_region_data['Categories']['Indeterminate']['Count']),
    '|NITRATE_REGION_DEGRADING_PCT|': str(nitrate_region_data['Categories']['Degrading']['Percentage']),
    '|NITRATE_REGION_DEGRADING_COUNT|': str(nitrate_region_data['Categories']['Degrading']['Count']),
}

for k, v in replacements.items():
    template_content = template_content.replace(k, v)

with open(nitrogen_trend_output_path, "w", encoding="utf-8") as f:
    f.write(template_content)

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

def adjust_iframe_height(md_content, base_dir):
    match = re.search(r'<iframe src="(results/[^"]+)"', md_content)
    if match:
        chart_file = match.group(1).replace('%20', ' ')
        chart_path = os.path.join(base_dir, chart_file)
        try:
            with open(chart_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
                h_match = re.search(r'height":(\d+)', html_content)
                if h_match:
                    height = int(h_match.group(1)) + 50
                    md_content = re.sub(r'height="\d+px"', f'height="{height}px"', md_content)
        except Exception as e:
            print(f"Warning: Could not adjust height for {chart_file}: {e}")
    return md_content

with open(os.path.join(os.path.dirname(__file__), "md/state_popup.md"), "r", encoding="utf-8") as f:
    state_popup = adjust_iframe_height(f.read(), os.path.dirname(__file__))

with open(os.path.join(os.path.dirname(__file__), "md/trend_popup.md"), "r", encoding="utf-8") as f:
    trend_popup = adjust_iframe_height(f.read(), os.path.dirname(__file__))

dashboard.add_overlay_button(block_id="button_state", label="Click for more state information", default_text=state_popup, payload_key="state_how", button_color="#772981", col_span=4, grid_area="button_state", panel_width="90%", panel_height="90%")

dashboard.add_overlay_button(block_id="button_trend", label="Click for more trend information", default_text=trend_popup, payload_key="trend_how", button_color="#772981", col_span=4, grid_area="button_trend", panel_width="90%", panel_height="90%")


for icon in icons:
    md_dir = os.path.join(os.path.dirname(__file__), icon["md_dir"])

    with open(os.path.join(md_dir, "placeholder.md"), "r", encoding="utf-8") as f:
        icon["md"] = f.read()
    with open(os.path.join(md_dir, "state_placeholder.md"), "r", encoding="utf-8") as f:
        icon["state_md"] = f.read()
    with open(os.path.join(md_dir, "trend_placeholder.md"), "r", encoding="utf-8") as f:
        icon["trend_md"] = f.read()
    with open(os.path.join(md_dir, "state_popup.md"), "r", encoding="utf-8") as f:
        state_how_content = f.read()
        icon["state_how"] = adjust_iframe_height(state_how_content, os.path.dirname(__file__))
    with open(os.path.join(md_dir, "trend_popup.md"), "r", encoding="utf-8") as f:
        trend_how_content = f.read()
        icon["trend_how"] = adjust_iframe_height(trend_how_content, os.path.dirname(__file__))

    map_file_path = os.path.join(os.path.dirname(__file__), icon["map_file"])
    if not os.path.exists(map_file_path):
        map_file_path = os.path.join(os.path.dirname(__file__), "results/FMU_Boundary_Only.html")
        icon["map_file"] = "results/FMU_Boundary_Only.html"

    with open(map_file_path, "r", encoding="utf-8") as f:
        map_content = f.read()
        if map_content.strip().lower().startswith("<!doctype html>") or map_content.strip().lower().startswith("<html"):
            icon["map_html"] = f"<div id='map_container' style='background:#f1f5f9; width:100%; height:100%; min-height:600px; display:flex; align-items:center; justify-content:center; border-radius:10px;'><iframe src='{icon['map_file']}' width='100%' height='100%' style='border:none; border-radius:10px;'></iframe></div>"
        else:
            icon["map_html"] = f"<div id='map_container' style='background:#f1f5f9; width:100%; height:100%; min-height:600px; display:flex; align-items:center; justify-content:center; border-radius:10px;'>{map_content}</div>"

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

    sivo_app.add_shape("circle", {
        "id": "img_interact",
        "name": blank_name,
        "cx": str(offset + size / 2),
        "cy": str(offset + size / 2),
        "r": str(size / 2),
        "fill": "rgba(255,255,255,0.01)"
    })

    payload = {
        "details_md": icon["md"],
        "state_md": icon["state_md"],
        "trend_md": icon["trend_md"],
        "state_how": icon["state_how"],
        "trend_how": icon["trend_how"],
        "map_html": icon["map_html"]
    }


    # map img_vis
    sivo_app.map(
        "img_vis",
        tooltip=icon["hover"],
        callback_payload=payload,
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
        callback_payload=payload,
        color="transparent",
        border_color="#ccffcc",
        border_width=8,
        hover_color="transparent",
        glow=True,
        fade_pulse=True
    )

    dashboard.add_sivo_block(block_id=icon["id"], sivo_app=sivo_app, col_span=1, grid_area=icon["id"], overflow_visible=True, min_height="100px")


with open(os.path.join(os.path.dirname(__file__), "results/FMU_Boundary_Only.html"), "r", encoding="utf-8") as f:
    map_html = f.read()
    if map_html.strip().lower().startswith("<!doctype html>") or map_html.strip().lower().startswith("<html"):
        # map_placeholder is currently a simple html snippet, but this handles future changes
        map_content_block = f"<div id='map_container' style='background:#f1f5f9; width:100%; height:100%; min-height:600px; display:flex; align-items:center; justify-content:center; border-radius:10px;'><iframe src='results/FMU_Boundary_Only.html' width='100%' height='100%' style='border:none; border-radius:10px;'></iframe></div>"
    else:
        map_content_block = f"<div id='map_container' style='background:#f1f5f9; width:100%; height:100%; min-height:600px; display:flex; align-items:center; justify-content:center; border-radius:10px;'>{map_html}</div>"

dashboard.add_html_block(block_id="map", html_content=map_content_block, col_span=4, grid_area="map", payload_key="map_html")

custom_js = None

output_file = os.path.join(os.path.dirname(__file__), "index.html")

dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file, custom_js=custom_js)
print(f"FMU Dashboard generated at {output_file}")
