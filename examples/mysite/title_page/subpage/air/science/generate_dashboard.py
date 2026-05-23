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
'odometer_1 odometer_1 odometer_2 odometer_2'
"""

mobile_grid = """
'banner'
'markdown'
'trends'
'exceedances'
'odometer_2'
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

def get_color(val):
    if val == 0: return "#10b981"
    if val == 1: return "#eab308"
    return "#ef4444"

# Taihape 1 year
t_1yr = int(site_data.get("Taihape", {}).get("exceedances_last_year", "0"))
t_1yr_color = get_color(t_1yr)

# Taihape 5 year
t_5yr = int(site_data.get("Taihape", {}).get("exceedances_5_year", "0"))
t_5yr_color = get_color(t_5yr)

# Taumarunui 1 year
tau_1yr = int(site_data.get("Taumarunui", {}).get("exceedances_last_year", "0"))
tau_1yr_color = get_color(tau_1yr)

# Taumarunui 5 year
tau_5yr = int(site_data.get("Taumarunui", {}).get("exceedances_5_year", "0"))
tau_5yr_color = get_color(tau_5yr)

t_date = site_data.get("Taihape", {}).get("date_of_last_exceedance", "")
tau_date = site_data.get("Taumarunui", {}).get("date_of_last_exceedance", "")

def get_subtext(date, val, x, y):
    if not date or val == 0: return ""
    return f'''
    <text x="{x}" y="{y}" font-size="12" fill="#333" font-family="sans-serif" text-anchor="middle">Date of last exceedance:</text>
    <text x="{x}" y="{y+20}" font-size="12" fill="#333" font-family="sans-serif" text-anchor="middle" font-weight="bold">{date}</text>
    '''

svg_content = f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" style="background:rgba(220, 230, 240, 0.9); border-radius: 10px; box-shadow: none;">
<style>.hide-native {{ opacity: 0; }}</style>
  <!-- Taihape 5 year (Top Left) -->
  <text x="150" y="40" font-size="16" fill="#333" font-family="sans-serif" font-weight="bold" text-anchor="middle">Taihape exceedances 5 years</text>
  <text class="hide-native" id="t_5yr_val" x="150" y="120" font-size="64" fill="{t_5yr_color}" font-family="sans-serif" font-weight="bold" text-anchor="middle">{t_5yr}</text>
  {get_subtext(t_date, t_5yr, 150, 160)}

  <!-- Taihape 1 year (Top Right) -->
  <text x="450" y="40" font-size="16" fill="#333" font-family="sans-serif" font-weight="bold" text-anchor="middle">Taihape exceedances last year</text>
  <text class="hide-native" id="t_1yr_val" x="450" y="120" font-size="64" fill="{t_1yr_color}" font-family="sans-serif" font-weight="bold" text-anchor="middle">{t_1yr}</text>
  {get_subtext(t_date, t_1yr, 450, 160)}

  <!-- Taumarunui 5 year (Bottom Left) -->
  <text x="150" y="240" font-size="16" fill="#333" font-family="sans-serif" font-weight="bold" text-anchor="middle">Taumarunui exceedances 5 years</text>
  <text class="hide-native" id="tau_5yr_val" x="150" y="320" font-size="64" fill="{tau_5yr_color}" font-family="sans-serif" font-weight="bold" text-anchor="middle">{tau_5yr}</text>
  {get_subtext(tau_date, tau_5yr, 150, 360)}

  <!-- Taumarunui 1 year (Bottom Right) -->
  <text x="450" y="240" font-size="16" fill="#333" font-family="sans-serif" font-weight="bold" text-anchor="middle">Taumarunui exceedances last year</text>
  <text class="hide-native" id="tau_1yr_val" x="450" y="320" font-size="64" fill="{tau_1yr_color}" font-family="sans-serif" font-weight="bold" text-anchor="middle">{tau_1yr}</text>
  {get_subtext(tau_date, tau_1yr, 450, 360)}
</svg>
'''

sivo_app = Sivo.from_string(svg_content, render_mode="svg", transparent_template_lines=True, lock_canvas=True, disable_zoom_controls=True, disable_resizer=True, lock_zoom_out=True, lock_scroll_bounds=True)
sivo_app.map(element_id="t_5yr_val", odometer_value=t_5yr, odometer_duration_ms=2500, odometer_format="int")
sivo_app.map(element_id="t_1yr_val", odometer_value=t_1yr, odometer_duration_ms=2500, odometer_format="int")
sivo_app.map(element_id="tau_5yr_val", odometer_value=tau_5yr, odometer_duration_ms=2500, odometer_format="int")
sivo_app.map(element_id="tau_1yr_val", odometer_value=tau_1yr, odometer_duration_ms=2500, odometer_format="int")

dashboard.add_sivo_block(
    block_id="odometer_2",
    sivo_app=sivo_app,
    col_span=2,
    grid_area="odometer_2"
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
