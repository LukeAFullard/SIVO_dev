import sys
import os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent / "src"))

from sivo import Sivo
from sivo.core.project import SivoProject

project = SivoProject(initial_view_id="main")

# Use a basic circle SVG
svg_str = """
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle id="lightbulb_area" cx="50" cy="50" r="40" fill="#cccccc" />
</svg>
"""

with open("temp.svg", "w") as f:
    f.write(svg_str)

app = Sivo.from_svg("temp.svg", lock_zoom_out=False)

# Lightbulb off and on image URLs (using placeholder images that are visually distinct)
dark_bulb = "https://images.unsplash.com/photo-1542617945-31c34a6e8e04?auto=format&fit=crop&q=80&w=200&h=200"
lit_bulb = "https://images.unsplash.com/photo-1493612276216-ee3925520721?auto=format&fit=crop&q=80&w=200&h=200"

app.map(
    "lightbulb_area",
    tooltip="Hover to light up!",
    fill_pattern={"image": dark_bulb},
    hover_image=lit_bulb
)

project.add_view("main", app)
project.to_html(Path(__file__).parent / "output.html")

# Cleanup temp svg
os.remove("temp.svg")
