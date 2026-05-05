import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..')))

from src.sivo.core.dashboard import SivoDashboard
from src.sivo.core.sivo import Sivo

dashboard = SivoDashboard(
    title="",
    columns=1,
    background_image_url="air_bg.png",
    background_image_opacity=0.25,
    background_image_size="100%",
    theme="transparent",
    gap="1rem"
)

desktop_grid = """
'banner'
'issues'
'science'
'help'
"""

dashboard.set_grid_layout(desktop=desktop_grid, mobile=desktop_grid)

dashboard.add_image_block(
    block_id="banner",
    image_url="air_banner.png",
    col_span=1,
    grid_area="banner",
    object_fit="contain",
    border_radius="0px"
)

dashboard.add_text_block(
    block_id="issues",
    text="What are the issues?",
    url="issues/index.html",
    col_span=1,
    grid_area="issues"
)

dashboard.add_text_block(
    block_id="science",
    text="What does the science say?",
    url="science/index.html",
    col_span=1,
    grid_area="science"
)

dashboard.add_text_block(
    block_id="help",
    text="What can we do to help?",
    url="help/index.html",
    col_span=1,
    grid_area="help"
)

output_file = os.path.join(os.path.dirname(__file__), "index.html")
dashboard.to_html(output_path=output_file)
print(f"Dashboard generated at {output_file}")
