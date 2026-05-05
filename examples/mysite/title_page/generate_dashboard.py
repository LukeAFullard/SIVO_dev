import sys
import os
# Add root to pythonpath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.sivo.core.dashboard import SivoDashboard

# Create the dashboard
dashboard = SivoDashboard(
    title="",
    columns=2,
    background_image_url="fish-green.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    gap="0.25rem",
    width="70%",
    mobile_width="85%",
    theme="transparent"
)

# Set the grid layout
desktop_grid = """
'env air'
'land water'
"""
mobile_grid = """
'env'
'air'
'land'
'water'
"""
dashboard.set_grid_layout(desktop=desktop_grid, mobile=mobile_grid)

# Add image blocks
dashboard.add_image_block(
    block_id="env",
    image_url="OurEnvironment.png",
    col_span=1,
    grid_area="env",
    object_fit="cover",
    border_radius="0px",
    fade_in=False
)
dashboard.add_image_block(
    block_id="air",
    image_url="Air.png",
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
    image_url="Land.png",
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
    image_url="Water.png",
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
