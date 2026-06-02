import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "sublinks": [
        {"label": "Overview", "url": "../index.html", "url_transition": "page-turn-enter"},
        {"label": "Issues", "url": "../issues/index.html", "url_transition": "page-turn-enter"},
        {"label": "Science", "url": "../science/index.html", "url_transition": "page-turn-enter"},
        {"label": "How to help", "url": "index.html", "url_transition": "page-turn-enter"}
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


def read_md(name):
    with open(os.path.join(os.path.dirname(__file__), "md", name + ".md"), "r", encoding="utf-8") as f:
        return f.read()

desktop_grid = """
'banner banner banner banner'
'. markdown markdown .'
'bad bad good good'
'bad_cap bad_cap good_cap good_cap'
"""

mobile_grid = """
'banner'
'markdown'
'bad'
'bad_cap'
'good'
'good_cap'
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

bad_air_svg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../assets/air/bad_template.svg"))
bad_air = Sivo.from_svg(
    bad_air_svg_path,
    theme="transparent",
    render_mode="canvas",
    disable_zoom_controls=True,
    lock_canvas=True,
    disable_resizer=True,
    lock_zoom_out=True,
    lock_scroll_bounds=True,
    transparent_template_lines=False,
    default_panel_position="overlay",
    panel_width="90%",
    panel_height="90%",
)
bad_air.add_svg_background_image(
    url="../../../assets/air/J420218 - Practices vs Good Practices Illustrations V3-04.png",
    insert_after="background"
)
bad_air.map(element_id="bad_logs_in_fireplace", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("bad_logs_in_fireplace"), border_color="yellow", border_width=3)
bad_air.map(element_id="bad_fireplace", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("bad_fireplace"), border_color="yellow", border_width=3)
bad_air.map(element_id="bad_log_stack", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("bad_log_stack"), border_color="yellow", border_width=3)
bad_air.map(element_id="bad_car", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("bad_car"), border_color="yellow", border_width=3)
bad_air.map(element_id="bad_rubbish", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("bad_rubbish"), border_color="yellow", border_width=3)
bad_air.map(element_id="bad_chimney", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("bad_chimney"), border_color="yellow", border_width=3)

good_air_svg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../assets/air/good_template.svg"))
good_air = Sivo.from_svg(
    good_air_svg_path,
    theme="transparent",
    render_mode="canvas",
    disable_zoom_controls=True,
    lock_canvas=True,
    disable_resizer=True,
    lock_zoom_out=True,
    lock_scroll_bounds=True,
    transparent_template_lines=False,
    default_panel_position="overlay",
    panel_width="90%",
    panel_height="90%",
)
good_air.add_svg_background_image(
    url="../../../assets/air/J420218 - Practices vs Good Practices Illustrations V3-03.png",
    insert_after="background"
)
good_air.map(element_id="good_chimney", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("good_chimney"), border_color="yellow", border_width=3)
good_air.map(element_id="good_wood_in_fireplace", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("good_wood_in_fireplace"), border_color="yellow", border_width=3)
good_air.map(element_id="good_fireplace", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("good_fireplace"), border_color="yellow", border_width=3)
good_air.map(element_id="good_bus", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("good_bus"), border_color="yellow", border_width=3)
good_air.map(element_id="good_log_stack", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("good_log_stack"), border_color="yellow", border_width=3)
good_air.map(element_id="good_compost", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("good_compost"), border_color="yellow", border_width=3)
good_air.map(element_id="good_woodshed", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("good_woodshed"), border_color="yellow", border_width=3)
good_air.map(element_id="good_brush", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("good_brush"), border_color="yellow", border_width=3)
good_air.map(element_id="good_bike", tooltip="Click me!", glow=True, fade_pulse=True, hover_color="rgba(255, 255, 0, 0.8)", markdown=read_md("good_bike"), border_color="yellow", border_width=3)


dashboard.add_sivo_block(
    block_id="bad",
    sivo_app=bad_air,
    col_span=2,
    grid_area="bad",
)

dashboard.add_sivo_block(
    block_id="good",
    sivo_app=good_air,
    col_span=2,
    grid_area="good",
)

dashboard.add_text_block(
    block_id="bad_cap",
    text="<div style='text-align: center; width: 100%;'><i>Activities contributing to poor air quality.</i></div>",
    font_size="16px",
    font_weight="normal",
    background_color="transparent",
    border="none",
    col_span=2,
    grid_area="bad_cap"
)

dashboard.add_text_block(
    block_id="good_cap",
    text="<div style='text-align: center; width: 100%;'><i>Activities contributing to good air quality.</i></div>",
    font_size="16px",
    font_weight="normal",
    background_color="transparent",
    border="none",
    col_span=2,
    grid_area="good_cap"
)


output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
