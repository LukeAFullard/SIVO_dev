import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src')))

from sivo import Sivo
from sivo.core.project import SivoProject

project = SivoProject(initial_view_id="main")

# Use a basic circle SVG
svg_str = """
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle id="lightbulb_area" cx="50" cy="50" r="40" fill="#cccccc" />
</svg>
"""

output_dir = os.path.dirname(__file__)
if not output_dir:
    output_dir = "."
temp_svg_path = os.path.join(output_dir, "temp.svg")
with open(temp_svg_path, "w") as f:
    f.write(svg_str)

app = Sivo.from_svg(temp_svg_path, lock_zoom_out=False)

# Lightbulb off and on image URLs (using placeholder images that are visually distinct)
dark_bulb = "https://images.unsplash.com/photo-1542617945-31c34a6e8e04?auto=format&fit=crop&q=80&w=200&h=200"
lit_bulb = "https://images.unsplash.com/photo-1493612276216-ee3925520721?auto=format&fit=crop&q=80&w=200&h=200"

app.map(
    "lightbulb_area",
    tooltip="Hover to light up!",
    fill_pattern={"image": dark_bulb},
    hover_image=lit_bulb,
    html="<h2>Lightbulb Clicked!</h2><p>You can map a side panel to the same element that has a hover effect.</p>",
    panel_position="right"
)

project.add_view("main", app)
project.to_html(os.path.join(output_dir, "output.html"))

# Cleanup temp svg
os.remove(temp_svg_path)
