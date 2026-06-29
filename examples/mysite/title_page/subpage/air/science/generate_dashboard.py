import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../')))

from src.sivo.core.dashboard import SivoDashboard

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../index.html"},
    {"label": "Air", "sublinks": [
        {"label": "Overview", "url": "../index.html"},
        {"label": "Pressures", "url": "../issues/index.html"},
        {"label": "State", "url": "index.html"},
        {"label": "Actions", "url": "../help/index.html"}
    ]},
    {"label": "Land", "url": "../../land/index.html"},
    {"label": "Water", "url": "../../water/index.html"}
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
'odometer_1'
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

def get_subtext(date, val):
    if not date or val == 0: return ""
    return f'<div style="font-size: 12px; color: #333; margin-top: 5px;">Date of last exceedance:<br><strong>{date}</strong></div>'

# Get Trend Data
t_trend_text = site_data.get("Taihape", {}).get("trend_text", "")
t_trend_rate = site_data.get("Taihape", {}).get("trend_rate", "")

tau_trend_text = site_data.get("Taumarunui", {}).get("trend_text", "")
tau_trend_rate = site_data.get("Taumarunui", {}).get("trend_rate", "")

def get_trend_color(text):
    text_lower = text.lower()
    if "improving" in text_lower: return "#10b981" # Green
    if "degrading" in text_lower: return "#ef4444" # Red
    return "#f97316" # Orange

odometer_1_html = f'''
<div style="display: flex; flex-direction: column; align-items: center; gap: 20px; text-align: center; padding: 20px;">
<div style="padding: 20px; background: rgba(255, 255, 255, 0.5); border-radius: 10px; width: 100%; max-width: 350px;">
<h3 style="margin-bottom: 5px; font-size: 16px; color: #333;">Taihape PM<sub>10</sub> trend</h3>
<div style="font-size: 32px; font-weight: bold; color: {get_trend_color(t_trend_text)};">{t_trend_text}</div>
<div style="font-size: 14px; color: #555; margin-top: 10px;">Trend rate: <strong>{t_trend_rate}</strong> &mu;g/m&sup3;</div>
</div>
<div style="padding: 20px; background: rgba(255, 255, 255, 0.5); border-radius: 10px; width: 100%; max-width: 350px;">
<h3 style="margin-bottom: 5px; font-size: 16px; color: #333;">Taumarunui PM<sub>10</sub> trend</h3>
<div style="font-size: 32px; font-weight: bold; color: {get_trend_color(tau_trend_text)};">{tau_trend_text}</div>
<div style="font-size: 14px; color: #555; margin-top: 10px;">Trend rate: <strong>{tau_trend_rate}</strong> &mu;g/m&sup3;</div>
</div>
<div style="font-size: 14px; color: #555; margin-top: 10px; text-align: center;">
Figure 2. Trend analysis of PM<sub>10</sub> concentrations in Taumarunui and Taihape between 2014 and 2025
</div>
</div>
'''

odometer_html = f'''
<div style="padding: 20px;">
<h2 style="text-align: center; margin-bottom: 10px;">Taihape</h2>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; text-align: center;">
<div style="padding: 20px; background: rgba(255, 255, 255, 0.5); border-radius: 10px;">
<h3 style="margin-bottom: 5px; font-size: 16px; color: #333;">Taihape PM<sub>10</sub> exceedances 5 years</h3>
<div style="font-size: 64px; font-weight: bold; color: {t_5yr_color};">{t_5yr}</div>{get_subtext(t_date, t_5yr)}</div>
<div style="padding: 20px; background: rgba(255, 255, 255, 0.5); border-radius: 10px;">
<h3 style="margin-bottom: 5px; font-size: 16px; color: #333;">Taihape PM<sub>10</sub> exceedances last year</h3>
<div style="font-size: 64px; font-weight: bold; color: {t_1yr_color};">{t_1yr}</div>{get_subtext(t_date, t_1yr)}</div>
</div>
<hr style="margin: 20px 0; border: none; border-top: 1px solid #ccc;">
<h2 style="text-align: center; margin-bottom: 10px;">Taumarunui</h2>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; text-align: center;">
<div style="padding: 20px; background: rgba(255, 255, 255, 0.5); border-radius: 10px;">
<h3 style="margin-bottom: 5px; font-size: 16px; color: #333;">Taumarunui PM<sub>10</sub> exceedances 5 years</h3>
<div style="font-size: 64px; font-weight: bold; color: {tau_5yr_color};">{tau_5yr}</div>{get_subtext(tau_date, tau_5yr)}</div>
<div style="padding: 20px; background: rgba(255, 255, 255, 0.5); border-radius: 10px;">
<h3 style="margin-bottom: 5px; font-size: 16px; color: #333;">Taumarunui PM<sub>10</sub> exceedances last year</h3>
<div style="font-size: 64px; font-weight: bold; color: {tau_1yr_color};">{tau_1yr}</div>{get_subtext(tau_date, tau_1yr)}</div>
</div>
</div>
'''

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

dashboard.add_details_panel(
    block_id="odometer_1",
    title="",
    placeholder=odometer_1_html,
    col_span=2,
    grid_area="odometer_1",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=1200,
    fade_duration_ms=2000
)

dashboard.add_details_panel(
    block_id="odometer_2",
    title="",
    placeholder=odometer_html,
    col_span=2,
    grid_area="odometer_2",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=1200,
    fade_duration_ms=2000
)

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
