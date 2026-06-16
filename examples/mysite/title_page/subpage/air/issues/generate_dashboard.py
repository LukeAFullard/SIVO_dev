import sys
import os
import subprocess

# Run the sub-dashboard generator first
sub_dashboard_script = os.path.join(os.path.dirname(__file__), "generate_sub_dashboard.py")
subprocess.run([sys.executable, sub_dashboard_script], check=True)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "sublinks": [
        {"label": "Overview", "url": "../index.html", "url_transition": "page-turn-enter"},
        {"label": "Pressures", "url": "index.html", "url_transition": "page-turn-enter"},
        {"label": "Science", "url": "../science/index.html", "url_transition": "page-turn-enter"},
        {"label": "Actions", "url": "../help/index.html", "url_transition": "page-turn-enter"}
    ]},
    {"label": "Land", "url": "../../land/index.html", "url_transition": "page-turn-enter"},
    {"label": "Water", "url": "../../water/index.html", "url_transition": "page-turn-enter"}
]

dashboard = SivoDashboard(
    title="",
    columns=3,
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

import urllib.parse

def read_md(name):
    with open(os.path.join(os.path.dirname(__file__), "md", name + ".md"), "r", encoding="utf-8") as f:
        return f.read()

desktop_grid = """
'banner banner banner'
'pm markdown markdown'
'importance markdown markdown'
'influences markdown markdown'
'. markdown markdown'
"""

mobile_grid = """
'banner'
'markdown'
'pm'
'importance'
'influences'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="../../../assets/air/air_banner.png",
    col_span=3,
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

# Function to generate an interactive block using raw HTML that mimics details panel trigger behavior.
def add_interactive_text_block(block_id, text, md_name, grid_area, delay_ms):
    md_content = read_md(md_name)
    encoded_md = urllib.parse.quote(md_content)
    html_content = f'''
    <div onclick="
        const panel = document.querySelector('.sivo-details-panel[data-block-id=\\\'markdown\\\'] .sivo-details-content');
        if(panel) {{
            panel.innerHTML = marked.parse(decodeURIComponent('{encoded_md}'));
        }}
    " style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; font-family: Arial, sans-serif; font-size: 36px; font-weight: bold; color: #333; background-color: #f0f8ff; border: 2px solid #87cefa; border-radius: 15px; text-align: center; box-sizing: border-box; cursor: pointer;">
        {text}
    </div>
    '''

    fade_style = f"opacity: 0; animation: sivo-fade-in-card 2s ease-in-out forwards; animation-delay: {delay_ms/1000.0}s;"
    wrapped_html = f'<div style="width: 100%; height: 100%; {fade_style}">{html_content}</div>'

    dashboard.add_html_block(
        block_id=block_id,
        html_content=wrapped_html,
        col_span=1,
        grid_area=grid_area
    )

add_interactive_text_block("pm", "What is particulate matter?", "pm", "pm", 300)
add_interactive_text_block("importance", "Why do we care about air quality?", "importance", "importance", 600)
add_interactive_text_block("influences", "What influences air quality?", "influences", "influences", 900)

custom_css = """
@media (min-width: 901px) {
    .dashboard-container {
        grid-template-rows: max-content max-content max-content max-content 1fr;
    }
    #card-pm, #card-importance, #card-influences {
        align-self: start;
    }
}
"""

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.add_layout_toggle_button("mobile_toggle", "📱", hover_text="Toggle Mobile View")
dashboard.to_html(output_path=output_file, custom_css=custom_css)
print(f"Dashboard generated at {output_file}")
