import sys
import os
# Add root to pythonpath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.sivo.core.dashboard import SivoDashboard

nav_menu = [
    {"label": "Horizons Regional Council", "url": "https://www.horizons.govt.nz/"},
    {"label": "Home", "url": "../../index.html", "url_transition": "page-turn-enter"},
    {"label": "Air", "url": "../air/index.html", "url_transition": "page-turn-enter"},
    {"label": "Land", "url": "../land/index.html", "url_transition": "page-turn-enter"},
    {"label": "Water", "url": "../water/index.html", "url_transition": "page-turn-enter"},
]

# Create the dashboard
dashboard = SivoDashboard(
    title="",
    columns=4,
    background_image_url="assets/fish-green.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    gap="tight",
    width="65%",
    mobile_width="85%",
    theme="transparent",
    navigation_menu=nav_menu
)

# Read the markdown
with open(os.path.join(os.path.dirname(__file__), "welcome.md"), "r", encoding="utf-8") as f:
    md_content = f.read()

# Set the grid layout
desktop_grid = """
'markdown markdown env air'
'markdown markdown land water'
"""
mobile_grid = """
'markdown'
'env'
'air'
'land'
'water'
"""
dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)


# Add layout toggle button
dashboard.add_layout_toggle_button(
    block_id="toggle",
    position="bottom-right"
)

# Add details panel
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

# Add image blocks
dashboard.add_image_block(
    block_id="env",
    image_url="assets/OurEnvironment.png",
    col_span=1,
    grid_area="env",
    object_fit="cover",
    border_radius="0px",
    fade_in=False
)
dashboard.add_image_block(
    block_id="air",
    image_url="assets/air/Air.png",
    col_span=1,
    grid_area="air",
    object_fit="cover",
    border_radius="0px",
    url="subpage/air/index.html",
    url_transition="page-turn-enter",
    fade_in=True,
    fade_start_time_ms=300,
    fade_duration_ms=2000
)
dashboard.add_image_block(
    block_id="land",
    image_url="assets/land/Land.png",
    col_span=1,
    grid_area="land",
    object_fit="cover",
    border_radius="0px",
    url="subpage/land/index.html",
    url_transition="page-turn-enter",
    fade_in=True,
    fade_start_time_ms=600,
    fade_duration_ms=2000
)
dashboard.add_image_block(
    block_id="water",
    image_url="assets/water/Water.png",
    col_span=1,
    grid_area="water",
    object_fit="cover",
    border_radius="0px",
    url="subpage/water/index.html",
    url_transition="page-turn-enter",
    fade_in=True,
    fade_start_time_ms=900,
    fade_duration_ms=2000
)

# Generate HTML
output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
