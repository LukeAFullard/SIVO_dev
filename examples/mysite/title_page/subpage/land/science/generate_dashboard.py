import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../src')))

from sivo.core.dashboard import SivoDashboard
from sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "url": "../../air/index.html", "url_transition": "page-turn-enter"},
    {"label": "Land", "sublinks": [
        {"label": "Issues", "url": "../issues/index.html", "url_transition": "page-turn-enter"},
        {"label": "What we are doing", "url": "index.html", "url_transition": "page-turn-enter"},
        {"label": "How to help", "url": "../help/index.html", "url_transition": "page-turn-enter"}
    ]},
    {"label": "Water", "url": "../../water/index.html", "url_transition": "page-turn-enter"}
]

fmus = [
    "Puketoi ki Tai",
    "Manawatū",
    "Rangitīkei-Turakina",
    "Waiopehu",
    "Kai Iwi",
    "Whangaehu",
    "Whanganui"
]

app = Sivo.from_svg(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../assets/water/sivo_template.svg")),
    enable_geocoder=True,
    geocode_provider="nominatim",
    geocode_country_codes="nz",
    geocoder_position="top-left",
    disable_zoom_controls=True,
    lock_canvas=True,
    disable_resizer=True,
    lock_zoom_out=True,
    lock_scroll_bounds=True,
    transparent_template_lines=True,
    layout_size="130%",
    mobile_layout_size="100%"
)

app.add_svg_background_image(
    "../../../assets/water/nz_comms_map_04_zoomed_detailed.png",
    insert_after="background"
)

app.bind_geocoder_intersection(
    geojson_url="https://services1.arcgis.com/VuN78wcRdq1Oj69W/arcgis/rest/services/FMU_20210122/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=geojson",
    display_element_id="null", # Output handled by overlay, we just put null
    property_name="Name",
    no_result_text="Address not found in any FMU zone."
)

with open(os.path.join(os.path.dirname(__file__), "susceptible.md"), "r", encoding="utf-8") as f:
    susceptible_md_content = f.read()

for fmu in fmus:
    slug = fmu.lower().replace(" ", "-").replace("ā", "a").replace("ī", "i")
    element_id = fmu.replace(" ", "_")

    md_path = os.path.join(os.path.dirname(__file__), "fmu", slug, "md", "info.md")
    with open(md_path, "r", encoding="utf-8") as f:
        fmu_md = f.read()

    html_path = os.path.join(os.path.dirname(__file__), "fmu", slug, "results", "chart.html")
    with open(html_path, "r", encoding="utf-8") as f:
        fmu_html = f.read()

    app.map(
        element_id=element_id,
        hover_color="lightgray",
        tooltip=fmu,
        glow=True,
        markdown=susceptible_md_content,
        callback_payload={"fmu_md": fmu_md, "fmu_html": fmu_html}
    )


dashboard = SivoDashboard(
    title="",
    columns=4,
    background_image_url="../../../assets/land/land_bg.png",
    background_image_opacity=0.15,
    background_image_size="50%",
    width="80%",
    mobile_width="100%",
    theme="transparent",
    gap="1rem",
    navigation_menu=nav_menu
)

# Read the markdown
with open(os.path.join(os.path.dirname(__file__), "welcome.md"), "r", encoding="utf-8") as f:
    welcome_md_content = f.read()

with open(os.path.join(os.path.dirname(__file__), "mitigation.md"), "r", encoding="utf-8") as f:
    mitigation_md_content = f.read()

with open(os.path.join(os.path.dirname(__file__), "time_lag.md"), "r", encoding="utf-8") as f:
    time_lag_md_content = f.read()


desktop_grid = """
'banner banner banner banner'
'markdown markdown markdown markdown'
'search map map map'
'text2 map map map'
'fmu_text fmu_html fmu_html fmu_html'
'mitigation_text mitigation_text mitigation_image mitigation_image'
'time_lag_text time_lag_text . .'
'tree_soil_image tree_soil_image erosion_time_lag_image erosion_time_lag_image'
"""

mobile_grid = """
'banner'
'markdown'
'search'
'text2'
'map'
'fmu_text'
'fmu_html'
'mitigation_text'
'mitigation_image'
'time_lag_text'
'tree_soil_image'
'erosion_time_lag_image'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../../../assets/land/land_banner.png",
    col_span=4,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

dashboard.add_details_panel(
    block_id="markdown",
    title="",
    placeholder=welcome_md_content,
    col_span=4,
    grid_area="markdown",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=300,
    fade_duration_ms=2000
)

dashboard.add_geocoder_block(
    block_id="search",
    col_span=1,
    grid_area="search",
    min_height="50px",
    overflow_visible=True
)

dashboard.add_details_panel(
    block_id="text2",
    title="",
    placeholder=susceptible_md_content,
    col_span=1,
    grid_area="text2",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=600,
    fade_duration_ms=2000
)


dashboard.add_sivo_block("map", app, col_span=3, grid_area="map", min_height="500px")

dashboard.add_details_panel(
    block_id="fmu_text",
    title="",
    placeholder="Click an FMU on the map to see details here.",
    col_span=1,
    grid_area="fmu_text",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=900,
    fade_duration_ms=2000,
    payload_key="fmu_md"
)

# add_html_block doesn't accept background_color and border_radius, need to wrap in div
html_content = '<div style="background-color: rgba(240, 240, 240, 0.7); border-radius: 10px; padding: 10px; height: 100%;">Click an FMU on the map to see charts here.</div>'
dashboard.add_html_block(
    block_id="fmu_html",
    html_content=html_content,
    col_span=3,
    grid_area="fmu_html",
    payload_key="fmu_html"
)

dashboard.add_details_panel(
    block_id="mitigation_text",
    title="",
    placeholder=mitigation_md_content,
    col_span=2,
    grid_area="mitigation_text",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=1200,
    fade_duration_ms=2000
)

dashboard.add_image_block(
    block_id="mitigation_image",
    image_url="../../../assets/land/tree_important.png",
    col_span=2,
    grid_area="mitigation_image",
    object_fit="contain",
    border_radius="10px",
    fade_in=True,
    fade_start_time_ms=1500,
    fade_duration_ms=2000
)

dashboard.add_details_panel(
    block_id="time_lag_text",
    title="",
    placeholder=time_lag_md_content,
    col_span=2,
    grid_area="time_lag_text",
    background_color="rgba(240, 240, 240, 0.7)",
    border_radius="10px",
    padding="10px",
    show_element_name=False,
    fade_in=True,
    fade_start_time_ms=1800,
    fade_duration_ms=2000
)

dashboard.add_image_block(
    block_id="tree_soil_image",
    image_url="../../../assets/land/tree_soil.png",
    col_span=2,
    grid_area="tree_soil_image",
    object_fit="contain",
    border_radius="10px",
    fade_in=True,
    fade_start_time_ms=2100,
    fade_duration_ms=2000
)

dashboard.add_image_block(
    block_id="erosion_time_lag_image",
    image_url="../../../assets/land/erosion_time_lag.png",
    col_span=2,
    grid_area="erosion_time_lag_image",
    object_fit="contain",
    border_radius="10px",
    fade_in=True,
    fade_start_time_ms=2400,
    fade_duration_ms=2000
)


output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
