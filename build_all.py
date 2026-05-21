import os
import json
import shutil

base_dir = "examples/mysite/title_page/subpage/water/science/fmu"
state_summary_file = os.path.join(base_dir, "../state_summary.json")
trend_summary_file = os.path.join(base_dir, "../trend_summary.json")

with open(state_summary_file, 'r', encoding='utf-8') as f:
    state_summary = json.load(f)
with open(trend_summary_file, 'r', encoding='utf-8') as f:
    trend_summary = json.load(f)

fmus = list(state_summary['FMUs'].keys())
if 'Manawatū' in fmus:
    fmus.remove('Manawatū')

fmu_directories = {
    'Kai Iwi': 'kai-iwi',
    'Puketoi ki Tai': 'puketoi-ki-tai',
    'Rangitīkei-Turakina': 'rangitikei-turakina',
    'Waiopehu': 'waiopehu',
    'Whangaehu': 'whangaehu',
    'Whanganui': 'whanganui'
}

new_script_template = """import sys
import os
import json
import re

# fix sys path to include root src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../../../src')))

from sivo.core.dashboard import SivoDashboard
from sivo.core.sivo import Sivo

base_dir = os.path.dirname(__file__)
fmu_name = "{fmu_name}"

json_path = os.path.abspath(os.path.join(base_dir, "../../state_summary.json"))
with open(json_path, 'r', encoding='utf-8') as f:
    state_summary = json.load(f)

parameters_state = {{
    "Sediment": {{"json_key": "Visual Clarity", "grades": ["A", "B", "C", "D"]}},
    "Algae": {{"json_key": "Chlorophyll A", "grades": ["A", "B", "C", "D"]}},
    "Phosphorus": {{"json_key": "DRP", "grades": ["A", "B", "C", "D"]}},
    "ecoli": {{"json_key": "E coli", "grades": ["A", "B", "C", "D", "E"]}},
    "inverts": {{"json_key": "MCI", "grades": ["A", "B", "C", "D"]}},
}}

for folder, p_info in parameters_state.items():
    if p_info["json_key"] not in state_summary["FMUs"][fmu_name]:
        continue

    template_path = os.path.join(base_dir, f"md/{{folder}}/state_placeholder_TEMPLATE.md")
    output_path = os.path.join(base_dir, f"md/{{folder}}/state_placeholder.md")

    fmu_data = state_summary["FMUs"][fmu_name][p_info["json_key"]]
    region_data = state_summary["Region"][p_info["json_key"]]
    fmu_sites = fmu_data.get("Total Sites for Attribute", 0)

    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    template_content = template_content.replace("|NUMBER_SITES|", str(fmu_sites))

    for grade in p_info["grades"]:
        if grade in fmu_data["Grades"]:
            fmu_pct = float(fmu_data["Grades"][grade]["Percentage"])
            fmu_count = fmu_data["Grades"][grade]["Count"]
        else:
            fmu_pct, fmu_count = 0.0, 0

        if grade in region_data["Grades"]:
            region_pct = float(region_data["Grades"][grade]["Percentage"])
            region_count = region_data["Grades"][grade]["Count"]
        else:
            region_pct, region_count = 0.0, 0

        template_content = template_content.replace(f"|FMU_{{grade}}_PCT|", f"{{fmu_pct:.1f}}")
        template_content = template_content.replace(f"|FMU_{{grade}}_COUNT|", str(fmu_count))
        template_content = template_content.replace(f"|REGION_{{grade}}_PCT|", f"{{region_pct:.1f}}")
        template_content = template_content.replace(f"|REGION_{{grade}}_COUNT|", str(region_count))

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template_content)

# Special case for Nitrogen
nitrogen_template_path = os.path.join(base_dir, "md/Nitrogen/state_placeholder_TEMPLATE.md")
nitrogen_output_path = os.path.join(base_dir, "md/Nitrogen/state_placeholder.md")

if "Ammoniacal-N" in state_summary["FMUs"][fmu_name] and "Nitrate-N" in state_summary["FMUs"][fmu_name]:
    with open(nitrogen_template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    ammo_fmu_data = state_summary["FMUs"][fmu_name]["Ammoniacal-N"]
    ammo_region_data = state_summary["Region"]["Ammoniacal-N"]
    nitrate_fmu_data = state_summary["FMUs"][fmu_name]["Nitrate-N"]
    nitrate_region_data = state_summary["Region"]["Nitrate-N"]
    fmu_sites = ammo_fmu_data.get("Total Sites for Attribute", 0)

    template_content = template_content.replace("|NUMBER_SITES|", str(fmu_sites))

    for grade in ["A", "B", "C", "D"]:
        # Ammo
        if grade in ammo_fmu_data["Grades"]:
            fmu_pct = float(ammo_fmu_data["Grades"][grade]["Percentage"])
            fmu_count = ammo_fmu_data["Grades"][grade]["Count"]
        else:
            fmu_pct, fmu_count = 0.0, 0

        if grade in ammo_region_data["Grades"]:
            region_pct = float(ammo_region_data["Grades"][grade]["Percentage"])
            region_count = ammo_region_data["Grades"][grade]["Count"]
        else:
            region_pct, region_count = 0.0, 0

        template_content = template_content.replace(f"|AMMO_FMU_{{grade}}_PCT|", f"{{fmu_pct:.1f}}")
        template_content = template_content.replace(f"|AMMO_FMU_{{grade}}_COUNT|", str(fmu_count))
        template_content = template_content.replace(f"|AMMO_REGION_{{grade}}_PCT|", f"{{region_pct:.1f}}")
        template_content = template_content.replace(f"|AMMO_REGION_{{grade}}_COUNT|", str(region_count))

        # Nitrate
        if grade in nitrate_fmu_data["Grades"]:
            fmu_pct = float(nitrate_fmu_data["Grades"][grade]["Percentage"])
            fmu_count = nitrate_fmu_data["Grades"][grade]["Count"]
        else:
            fmu_pct, fmu_count = 0.0, 0

        if grade in nitrate_region_data["Grades"]:
            region_pct = float(nitrate_region_data["Grades"][grade]["Percentage"])
            region_count = nitrate_region_data["Grades"][grade]["Count"]
        else:
            region_pct, region_count = 0.0, 0

        template_content = template_content.replace(f"|NITRATE_FMU_{{grade}}_PCT|", f"{{fmu_pct:.1f}}")
        template_content = template_content.replace(f"|NITRATE_FMU_{{grade}}_COUNT|", str(fmu_count))
        template_content = template_content.replace(f"|NITRATE_REGION_{{grade}}_PCT|", f"{{region_pct:.1f}}")
        template_content = template_content.replace(f"|NITRATE_REGION_{{grade}}_COUNT|", str(region_count))

    with open(nitrogen_output_path, 'w', encoding='utf-8') as f:
        f.write(template_content)


nav_menu = [
    {{"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"}},
    {{"label": "Home", "url": "../../../../../index.html", "url_transition": "page-turn-enter"}},
    {{"label": "Air", "url": "../../../../air/index.html", "url_transition": "page-turn-enter"}},
    {{"label": "Land", "url": "../../../../land/index.html", "url_transition": "page-turn-enter"}},
    {{"label": "Water", "sublinks": [
        {{"label": "Issues", "url": "../../../issues/index.html", "url_transition": "page-turn-enter"}},
        {{"label": "Science", "url": "../../index.html", "url_transition": "page-turn-enter"}},
        {{"label": "How to help", "url": "../../../help/index.html", "url_transition": "page-turn-enter"}}
    ]}}
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

icons_full = [
    {{"id": "icon1", "key": "E coli", "img": "../../../../../assets/water/20221123_OrangaWai_IconEcoli.png", "hover": "E. <i>coli</i>", "md_dir": "md/ecoli", "map_file": "results/Map_E coli.html"}},
    {{"id": "icon2", "key": "Visual Clarity", "img": "../../../../../assets/water/20221123_OrangaWai_IconSuspendedSediment.png", "hover": "Suspended sediment", "md_dir": "md/Sediment", "map_file": "results/Map_Visual Clarity.html"}},
    {{"id": "icon3", "key": "Nitrate-N", "img": "../../../../../assets/water/20221123_OrangaWai_IconN.png", "hover": "Nitrogen", "md_dir": "md/Nitrogen", "map_file": "results/Map_Nitrate-N.html"}},
    {{"id": "icon4", "key": "DRP", "img": "../../../../../assets/water/20221123_OrangaWai_IconP.png", "hover": "Phosphorus", "md_dir": "md/Phosphorus", "map_file": "results/Map_DRP.html"}},
    {{"id": "icon5", "key": "Chlorophyll A", "img": "../../../../../assets/water/20221123_OrangaWai_IconChlA.png", "hover": "Algae", "md_dir": "md/Algae", "map_file": "results/Map_Chlorophyll A.html"}},
    {{"id": "icon6", "key": "MCI", "img": "../../../../../assets/water/20221123_OrangaWai_IconAquaticLife.png", "hover": "Invertebrates", "md_dir": "md/inverts", "map_file": "results/Map_MCI.html"}}
]

icons = []
for icon in icons_full:
    if os.path.exists(os.path.join(base_dir, icon['map_file'])):
        # Verify it has state summary data
        if icon['key'] in state_summary["FMUs"][fmu_name] or (icon['key'] == 'Nitrate-N' and 'Nitrate-N' in state_summary["FMUs"][fmu_name]):
            icons.append(icon)

icon_ids = [icon['id'] for icon in icons]
while len(icon_ids) < 8:
    icon_ids.append('.')

icon_row = f"'{{' '.join(icon_ids[:8])}}'"
if len(icons) == 4:
    icon_row = f"'. . {{icons[0]['id']}} {{icons[1]['id']}} {{icons[2]['id']}} {{icons[3]['id']}} . .'"
elif len(icons) == 5:
    icon_row = f"'. {{icons[0]['id']}} {{icons[1]['id']}} {{icons[2]['id']}} {{icons[3]['id']}} {{icons[4]['id']}} . .'"
elif len(icons) == 6:
    icon_row = f"'. {{icons[0]['id']}} {{icons[1]['id']}} {{icons[2]['id']}} {{icons[3]['id']}} {{icons[4]['id']}} {{icons[5]['id']}} .'"

desktop_grid = f\"\"\"
'banner banner banner banner banner banner banner banner'
{{icon_row}}
'details details details map map map map map'
'gap1 gap1 gap1 map map map map map'
'state state state state trend trend trend trend'
'button_state button_state button_state button_state button_trend button_trend button_trend button_trend'
\"\"\"

mobile_icon_rows = []
for i in range(0, len(icons), 2):
    if i+1 < len(icons):
        mobile_icon_rows.append(f"'{{icons[i]['id']}} {{icons[i+1]['id']}}'")
    else:
        mobile_icon_rows.append(f"'{{icons[i]['id']}} .'")

mobile_icon_str = "\\n".join(mobile_icon_rows)

mobile_grid = f\"\"\"
'banner banner'
{{mobile_icon_str}}
'map map'
'details details'
'gap1 gap1'
'state state'
'button_state button_state'
'gap2 gap2'
'trend trend'
'button_trend button_trend'
\"\"\"

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

with open(os.path.join(os.path.dirname(__file__), "../../trend_summary.json"), "r", encoding="utf-8") as f:
    trend_data = json.load(f)

parameters_trend = {{
    "Sediment": "Visual Clarity",
    "Algae": "Chlorophyll A",
    "Phosphorus": "Dissolved Reactive Phosphorus",
    "ecoli": "E. coli",
    "inverts": "MCI (Macroinvertebrate Community Index)",
}}

for folder, json_key in parameters_trend.items():
    if json_key not in trend_data['FMUs'][fmu_name]:
        continue

    fmu_data = trend_data['FMUs'][fmu_name][json_key]
    region_data = trend_data['Region'][json_key]

    template_path = os.path.join(os.path.dirname(__file__), f"md/{{folder}}/trend_placeholder_TEMPLATE.md")
    output_path = os.path.join(os.path.dirname(__file__), f"md/{{folder}}/trend_placeholder.md")

    if not os.path.exists(template_path):
        continue

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    def safe_get(d, cat, field):
        try:
            return str(d['Categories'][cat][field])
        except KeyError:
            return "0"

    replacements = {{
        '|NUMBER_SITES|': str(fmu_data.get('Total Sites for Parameter', 0)),
        '|FMU_IMPROVING_PCT|': safe_get(fmu_data, 'Improving', 'Percentage'),
        '|FMU_IMPROVING_COUNT|': safe_get(fmu_data, 'Improving', 'Count'),
        '|FMU_INDETERMINATE_PCT|': safe_get(fmu_data, 'Indeterminate', 'Percentage'),
        '|FMU_INDETERMINATE_COUNT|': safe_get(fmu_data, 'Indeterminate', 'Count'),
        '|FMU_DEGRADING_PCT|': safe_get(fmu_data, 'Degrading', 'Percentage'),
        '|FMU_DEGRADING_COUNT|': safe_get(fmu_data, 'Degrading', 'Count'),
        '|REGION_IMPROVING_PCT|': safe_get(region_data, 'Improving', 'Percentage'),
        '|REGION_IMPROVING_COUNT|': safe_get(region_data, 'Improving', 'Count'),
        '|REGION_INDETERMINATE_PCT|': safe_get(region_data, 'Indeterminate', 'Percentage'),
        '|REGION_INDETERMINATE_COUNT|': safe_get(region_data, 'Indeterminate', 'Count'),
        '|REGION_DEGRADING_PCT|': safe_get(region_data, 'Degrading', 'Percentage'),
        '|REGION_DEGRADING_COUNT|': safe_get(region_data, 'Degrading', 'Count'),
    }}

    for k, v in replacements.items():
        template_content = template_content.replace(k, v)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template_content)

# Special case for Nitrogen
nitrogen_trend_template_path = os.path.join(base_dir, "md/Nitrogen/trend_placeholder_TEMPLATE.md")
nitrogen_trend_output_path = os.path.join(base_dir, "md/Nitrogen/trend_placeholder.md")

if "Ammoniacal Nitrogen (NH4)" in trend_data['FMUs'][fmu_name] and "Nitrate Nitrogen (NO3)" in trend_data['FMUs'][fmu_name] and os.path.exists(nitrogen_trend_template_path):
    with open(nitrogen_trend_template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    ammo_fmu_data = trend_data['FMUs'][fmu_name]["Ammoniacal Nitrogen (NH4)"]
    ammo_region_data = trend_data['Region']["Ammoniacal Nitrogen (NH4)"]
    nitrate_fmu_data = trend_data['FMUs'][fmu_name]["Nitrate Nitrogen (NO3)"]
    nitrate_region_data = trend_data['Region']["Nitrate Nitrogen (NO3)"]
    fmu_sites = ammo_fmu_data.get('Total Sites for Parameter', 0)

    replacements = {{
        '|NUMBER_SITES|': str(fmu_sites),
        '|AMMO_FMU_IMPROVING_PCT|': safe_get(ammo_fmu_data, 'Improving', 'Percentage'),
        '|AMMO_FMU_IMPROVING_COUNT|': safe_get(ammo_fmu_data, 'Improving', 'Count'),
        '|AMMO_FMU_INDETERMINATE_PCT|': safe_get(ammo_fmu_data, 'Indeterminate', 'Percentage'),
        '|AMMO_FMU_INDETERMINATE_COUNT|': safe_get(ammo_fmu_data, 'Indeterminate', 'Count'),
        '|AMMO_FMU_DEGRADING_PCT|': safe_get(ammo_fmu_data, 'Degrading', 'Percentage'),
        '|AMMO_FMU_DEGRADING_COUNT|': safe_get(ammo_fmu_data, 'Degrading', 'Count'),
        '|AMMO_REGION_IMPROVING_PCT|': safe_get(ammo_region_data, 'Improving', 'Percentage'),
        '|AMMO_REGION_IMPROVING_COUNT|': safe_get(ammo_region_data, 'Improving', 'Count'),
        '|AMMO_REGION_INDETERMINATE_PCT|': safe_get(ammo_region_data, 'Indeterminate', 'Percentage'),
        '|AMMO_REGION_INDETERMINATE_COUNT|': safe_get(ammo_region_data, 'Indeterminate', 'Count'),
        '|AMMO_REGION_DEGRADING_PCT|': safe_get(ammo_region_data, 'Degrading', 'Percentage'),
        '|AMMO_REGION_DEGRADING_COUNT|': safe_get(ammo_region_data, 'Degrading', 'Count'),

        '|NITRATE_FMU_IMPROVING_PCT|': safe_get(nitrate_fmu_data, 'Improving', 'Percentage'),
        '|NITRATE_FMU_IMPROVING_COUNT|': safe_get(nitrate_fmu_data, 'Improving', 'Count'),
        '|NITRATE_FMU_INDETERMINATE_PCT|': safe_get(nitrate_fmu_data, 'Indeterminate', 'Percentage'),
        '|NITRATE_FMU_INDETERMINATE_COUNT|': safe_get(nitrate_fmu_data, 'Indeterminate', 'Count'),
        '|NITRATE_FMU_DEGRADING_PCT|': safe_get(nitrate_fmu_data, 'Degrading', 'Percentage'),
        '|NITRATE_FMU_DEGRADING_COUNT|': safe_get(nitrate_fmu_data, 'Degrading', 'Count'),
        '|NITRATE_REGION_IMPROVING_PCT|': safe_get(nitrate_region_data, 'Improving', 'Percentage'),
        '|NITRATE_REGION_IMPROVING_COUNT|': safe_get(nitrate_region_data, 'Improving', 'Count'),
        '|NITRATE_REGION_INDETERMINATE_PCT|': safe_get(nitrate_region_data, 'Indeterminate', 'Percentage'),
        '|NITRATE_REGION_INDETERMINATE_COUNT|': safe_get(nitrate_region_data, 'Indeterminate', 'Count'),
        '|NITRATE_REGION_DEGRADING_PCT|': safe_get(nitrate_region_data, 'Degrading', 'Percentage'),
        '|NITRATE_REGION_DEGRADING_COUNT|': safe_get(nitrate_region_data, 'Degrading', 'Count'),
    }}

    for k, v in replacements.items():
        template_content = template_content.replace(k, v)

    with open(nitrogen_trend_output_path, "w", encoding="utf-8") as f:
        f.write(template_content)

# We will populate md, state_md, trend_md
with open(os.path.join(os.path.dirname(__file__), "md/details_placeholder.md"), "r", encoding="utf-8") as f:
    details_default = f.read()

# Fallback for state and trend placeholder
state_default_path = os.path.join(os.path.dirname(__file__), "md/state_placeholder.md")
if os.path.exists(state_default_path):
    with open(state_default_path, "r", encoding="utf-8") as f:
        state_default = f.read()
else:
    state_default = "Select an indicator to view state."

trend_default_path = os.path.join(os.path.dirname(__file__), "md/trend_placeholder.md")
if os.path.exists(trend_default_path):
    with open(trend_default_path, "r", encoding="utf-8") as f:
        trend_default = f.read()
else:
    trend_default = "Select an indicator to view trend."

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
                h_match = re.search(r'height":(\\d+)', html_content)
                if h_match:
                    height = int(h_match.group(1)) + 50
                    md_content = re.sub(r'height="\\d+px"', f'height="{{height}}px"', md_content)
        except Exception as e:
            print(f"Warning: Could not adjust height for {{chart_file}}: {{e}}")
    return md_content

state_popup_path = os.path.join(os.path.dirname(__file__), "md/state_popup.md")
if os.path.exists(state_popup_path):
    with open(state_popup_path, "r", encoding="utf-8") as f:
        state_popup = adjust_iframe_height(f.read(), os.path.dirname(__file__))
else:
    state_popup = "Details not available."

trend_popup_path = os.path.join(os.path.dirname(__file__), "md/trend_popup.md")
if os.path.exists(trend_popup_path):
    with open(trend_popup_path, "r", encoding="utf-8") as f:
        trend_popup = adjust_iframe_height(f.read(), os.path.dirname(__file__))
else:
    trend_popup = "Details not available."

dashboard.add_overlay_button(block_id="button_state", label="Click for more state information", default_text=state_popup, payload_key="state_how", button_color="#772981", col_span=4, grid_area="button_state", panel_width="90%", panel_height="90%")

dashboard.add_overlay_button(block_id="button_trend", label="Click for more trend information", default_text=trend_popup, payload_key="trend_how", button_color="#772981", col_span=4, grid_area="button_trend", panel_width="90%", panel_height="90%")

for icon in icons:
    md_dir = os.path.join(os.path.dirname(__file__), icon["md_dir"])

    ph_path = os.path.join(md_dir, "placeholder.md")
    if os.path.exists(ph_path):
        with open(ph_path, "r", encoding="utf-8") as f:
            icon["md"] = f.read()
    else:
        icon["md"] = "Placeholder not available."

    sph_path = os.path.join(md_dir, "state_placeholder.md")
    if os.path.exists(sph_path):
        with open(sph_path, "r", encoding="utf-8") as f:
            icon["state_md"] = f.read()
    else:
        icon["state_md"] = "State not available."

    tph_path = os.path.join(md_dir, "trend_placeholder.md")
    if os.path.exists(tph_path):
        with open(tph_path, "r", encoding="utf-8") as f:
            icon["trend_md"] = f.read()
    else:
        icon["trend_md"] = "Trend not available."

    sp_path = os.path.join(md_dir, "state_popup.md")
    if os.path.exists(sp_path):
        with open(sp_path, "r", encoding="utf-8") as f:
            icon["state_how"] = adjust_iframe_height(f.read(), os.path.dirname(__file__))
    else:
        icon["state_how"] = "No state chart."

    tp_path = os.path.join(md_dir, "trend_popup.md")
    if os.path.exists(tp_path):
        with open(tp_path, "r", encoding="utf-8") as f:
            icon["trend_how"] = adjust_iframe_height(f.read(), os.path.dirname(__file__))
    else:
        icon["trend_how"] = "No trend chart."

    map_path = os.path.join(os.path.dirname(__file__), icon["map_file"])
    if os.path.exists(map_path):
        with open(map_path, "r", encoding="utf-8") as f:
            map_content = f.read()
            if map_content.strip().lower().startswith("<!doctype html>") or map_content.strip().lower().startswith("<html"):
                icon["map_html"] = f"<div id='map_container' style='background:#f1f5f9; width:100%; height:100%; min-height:600px; display:flex; align-items:center; justify-content:center; border-radius:10px;'><iframe src='{{icon['map_file']}}' width='100%' height='100%' style='border:none; border-radius:10px;'></iframe></div>"
            else:
                icon["map_html"] = f"<div id='map_container' style='background:#f1f5f9; width:100%; height:100%; min-height:600px; display:flex; align-items:center; justify-content:center; border-radius:10px;'>{{map_content}}</div>"
    else:
        icon["map_html"] = "<p>Map not found.</p>"

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

    sivo_app.add_shape("rect", {{
        "id": "img_interact",
        "name": blank_name,
        "x": str(offset),
        "y": str(offset),
        "width": str(size),
        "height": str(size),
        "fill": "rgba(255,255,255,0.01)",
        "rx": "5",
        "ry": "5"
    }})

    payload = {{
        "details_md": icon["md"],
        "state_md": icon["state_md"],
        "trend_md": icon["trend_md"],
        "state_how": icon["state_how"],
        "trend_how": icon["trend_how"],
        "map_html": icon["map_html"]
    }}

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


fmu_bound = os.path.join(os.path.dirname(__file__), "results/FMU_Boundary_Only.html")
if os.path.exists(fmu_bound):
    with open(fmu_bound, "r", encoding="utf-8") as f:
        map_html = f.read()
        if map_html.strip().lower().startswith("<!doctype html>") or map_html.strip().lower().startswith("<html"):
            map_content_block = f"<div id='map_container' style='background:#f1f5f9; width:100%; height:100%; min-height:600px; display:flex; align-items:center; justify-content:center; border-radius:10px;'><iframe src='results/FMU_Boundary_Only.html' width='100%' height='100%' style='border:none; border-radius:10px;'></iframe></div>"
        else:
            map_content_block = f"<div id='map_container' style='background:#f1f5f9; width:100%; height:100%; min-height:600px; display:flex; align-items:center; justify-content:center; border-radius:10px;'>{{map_html}}</div>"
else:
    map_content_block = "<div>Map not available</div>"

dashboard.add_html_block(block_id="map", html_content=map_content_block, col_span=4, grid_area="map", payload_key="map_html")

custom_js = None

output_file = os.path.join(os.path.dirname(__file__), "index.html")

dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file, custom_js=custom_js)
print(f"FMU Dashboard generated at {{output_file}}")
"""

manawatu_md_dir = os.path.join(base_dir, 'manawatū/md')

for fmu_name in fmus:
    dir_name = fmu_directories[fmu_name]
    target_dir = os.path.join(base_dir, dir_name)
    target_md_dir = os.path.join(target_dir, 'md')

    if os.path.exists(target_md_dir):
        shutil.rmtree(target_md_dir)

    shutil.copytree(manawatu_md_dir, target_md_dir)

    # Replace "Manawatū" with fmu_name in all md files
    for root, dirs, files in os.walk(target_md_dir):
        for file in files:
            if file.endswith('.md') or file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = content.replace("Manawatū", fmu_name)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

    # Replace specific file content for formatting properly
    script_content = new_script_template.format(fmu_name=fmu_name)

    # Clean up double curly braces inside the string that we escaped
    script_content = script_content.replace('{{', '{').replace('}}', '}')

    script_path = os.path.join(target_dir, 'generate_fmu_page.py')
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_content)

    print(f"Generated files for {fmu_name}")
