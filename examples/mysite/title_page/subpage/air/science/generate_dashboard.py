import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "sublinks": [
        {"label": "Overview", "url": "../index.html", "url_transition": "page-turn-enter"},
        {"label": "Issues", "url": "../issues/index.html", "url_transition": "page-turn-enter"},
        {"label": "Science", "url": "index.html", "url_transition": "page-turn-enter"},
        {"label": "How to help", "url": "../help/index.html", "url_transition": "page-turn-enter"}
    ]},
    {"label": "Land", "url": "../../land/index.html", "url_transition": "page-turn-enter"},
    {"label": "Water", "url": "../../water/index.html", "url_transition": "page-turn-enter"}
]

dashboard = SivoDashboard(
    title="",
    columns=4,
    background_image_url="../../../assets/air/air_bg.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    width="80%",
    mobile_width="100%",
    theme="transparent",
    gap="tight",
    navigation_menu=nav_menu
)

# Read the markdown
with open(os.path.join(os.path.dirname(__file__), "content.md"), "r", encoding="utf-8") as f:
    md_content = f.read()

with open(os.path.join(os.path.dirname(__file__), "pm10_trends.md"), "r", encoding="utf-8") as f:
    pm10_trends = f.read()

with open(os.path.join(os.path.dirname(__file__), "pm10_exceedances.md"), "r", encoding="utf-8") as f:
    pm10_exceedances = f.read()

desktop_grid = """
'banner banner banner banner'
'. markdown markdown .'
'trends trends exceedances exceedances'
'odometer_1 odometer_2 odometer_3 odometer_4'
"""

mobile_grid = """
'banner'
'markdown'
'trends'
'exceedances'
'odometer_3'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../../../assets/air/air_banner.png",
    col_span=4,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

dashboard.add_details_panel(
    block_id="markdown",
    title="",
    placeholder=md_content,
    col_span=2,
    grid_area="markdown",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=300,
    fade_duration_ms=2000
)

# Read JSON Data
with open(os.path.join(os.path.dirname(__file__), "data.json"), "r") as f:
    site_data = json.load(f)

taihape_exc = site_data.get("Taihape", {}).get("exceedances_last_year", "0")
taihape_exc_val = int(taihape_exc) if taihape_exc.isdigit() else 0

color = "#10b981" # green
if taihape_exc_val == 1:
    color = "#eab308" # yellow
elif taihape_exc_val > 1:
    color = "#ef4444" # red

taihape_last_exc_date = site_data.get("Taihape", {}).get("date_of_last_exceedance", "")

subtext_svg = ""
if taihape_last_exc_date:
    subtext_svg = f"""
    <text x="150" y="160" font-size="14" fill="#333" font-family="sans-serif" text-anchor="middle">Date of last exceedance:</text>
    <text x="150" y="180" font-size="14" fill="#333" font-family="sans-serif" text-anchor="middle" font-weight="bold">{taihape_last_exc_date}</text>
    """

svg_content = f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" style="background:rgba(240, 240, 240, 0.7); border-radius: 10px; box-shadow: none;">
  <text x="150" y="40" font-size="16" fill="#333" font-family="sans-serif" font-weight="bold" text-anchor="middle">Taihape exceedances last year</text>
  <text id="taihape_val" x="150" y="120" font-size="64" fill="{color}" font-family="sans-serif" font-weight="bold" text-anchor="middle">0</text>
  {subtext_svg}
</svg>
"""

sivo_app = Sivo.from_string(svg_content, render_mode="svg")
sivo_app.map(
    element_id="taihape_val",
    odometer_value=taihape_exc_val,
    odometer_duration_ms=2500,
    odometer_format="int"
)

dashboard.add_sivo_block(
    block_id="odometer_3",
    sivo_app=sivo_app,
    col_span=1,
    grid_area="odometer_3"
)

dashboard.add_details_panel(
    block_id="trends",
    title="",
    placeholder=pm10_trends,
    col_span=2,
    grid_area="trends",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=600,
    fade_duration_ms=2000
)

dashboard.add_details_panel(
    block_id="exceedances",
    title="",
    placeholder=pm10_exceedances,
    col_span=2,
    grid_area="exceedances",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=900,
    fade_duration_ms=2000
)

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
