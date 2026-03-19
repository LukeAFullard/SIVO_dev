import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from sivo import Sivo
from sivo.core.actions import ZoomAction

svg_content = """<svg viewBox="0 0 1000 1750" xmlns="http://www.w3.org/2000/svg">
  <rect width="1000" height="1750" fill="#1e1e1e" />

  <text x="500" y="300" text-anchor="middle" dominant-baseline="middle" font-size="48" fill="#ffffff" font-family="sans-serif">The Microscopic Secret</text>
  <text x="500" y="380" text-anchor="middle" dominant-baseline="middle" font-size="24" fill="#888888" font-family="sans-serif">Click the button below to zoom 120x</text>

  <rect id="tiny_button" x="497.5" y="850" width="5" height="5" fill="#3498db" />
  <rect id="hidden_text" x="497.5" y="850" width="5" height="5" fill="transparent" pointer-events="none"></rect>

  <rect id="zoom_button" x="250" y="1400" width="500" height="150" fill="#e74c3c" rx="20" />
  <text x="500" y="1475" text-anchor="middle" dominant-baseline="middle" font-size="48" fill="#ffffff" pointer-events="none" font-family="sans-serif">ZOOM 120x</text>
</svg>"""

app = Sivo.from_string(
    svg_content,
    disable_zoom_controls=False,
    layout_size="99%",
    disable_panel=True
)

app.fill_template_zone(
    element_id="hidden_text",
    text="You found the secret! SVG vector text remains perfectly crisp, even when scaling from a 5x5 pixel dot to fullscreen.",
    color="#ffffff",
    auto_shrink=True,
    font_size="10%"
)

target_center = app.infographic.get_element_center("hidden_text")

app.map(
    element_id="zoom_button",
    hover_color="#c0392b",
    tooltip="Click to glide into the microscopic message!"
)

# Set the slow zoom to 1500 ms as requested
if target_center:
    app.infographic.mappings["zoom_button"].actions.append(ZoomAction(center=target_center, zoom_level=120.0, duration_ms=1500))

# Tiny button uses the new default 500ms
app.map(
    element_id="tiny_button",
    hover_color="#2980b9",
    tooltip="You found it!",
    zoom_on_click=True,
    zoom_level=120.0
)

output_path = "examples/mobile_tiny_text/mobile_tiny_text.html"
app.to_html(output_path)
print(f"Created {output_path}")
