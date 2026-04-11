import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from sivo import Sivo

# 4:3 aspect ratio = 1200x900
svg_content = """<svg viewBox="0 0 1200 900" xmlns="http://www.w3.org/2000/svg">


  <text x="600" y="200" text-anchor="middle" dominant-baseline="middle" font-size="48" fill="#ffffff" font-family="sans-serif">The Microscopic Secret</text>
  <text x="600" y="280" text-anchor="middle" dominant-baseline="middle" font-size="24" fill="#888888" font-family="sans-serif">Click the button below to zoom automatically</text>

  <rect id="tiny_button" x="597.5" y="450" width="5" height="5" fill="#3498db" />
  <rect id="hidden_text" x="597.5" y="450" width="5" height="5" fill="transparent" pointer-events="none"></rect>

  <rect id="zoom_button" x="350" y="700" width="500" height="150" fill="#e74c3c" rx="20" />
  <text x="600" y="775" text-anchor="middle" dominant-baseline="middle" font-size="48" fill="#ffffff" pointer-events="none" font-family="sans-serif">ZOOM</text>
</svg>"""

app = Sivo.from_string(
    svg_content,
    disable_zoom_controls=False,
    layout_size="99%",
    default_panel_position="none",
    theme="dark"
)

# Background image over SVG canvas.
# We use encode_base64=True so ECharts draws the image immediately on the first render,
# bypassing the browser's asynchronous external image loading which would leave it blank.
image_url = "https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&w=1920&q=80"

app.add_svg_background_image(
    url=image_url,
    opacity=0.5,
    encode_base64=True
)

# Clip same image to tiny text area with 0.3 opacity.
# We set use_html_overlay=False because HTML CSS masking has precision issues
# when zooming natively to extreme microscopic levels (120x) on a 5px target.
# Setting it to False natively injects an <image> tag bounding box into the SVG.
app.clip_image_to_shape(
    element_id="hidden_text",
    image_url=image_url,
    opacity=0.3,
    use_html_overlay=False,
    encode_base64=True
)

app.fill_template_zone(
    element_id="hidden_text",
    text="You found the secret! SVG vector text remains perfectly crisp, even when scaling from a 5x5 pixel dot to fullscreen.",
    color="#ffffff",
    auto_shrink=True,
    font_size="10%"
)

app.map(
    element_id="zoom_button",
    hover_color="#c0392b",
    tooltip="Click to glide into the microscopic message!",
    zoom_to="hidden_text",
    zoom_to_size="auto",
    zoom_duration_ms=1500
)

# Tiny button uses the new default 500ms
app.map(
    element_id="tiny_button",
    hover_color="#2980b9",
    tooltip="You found it!",
    zoom_to="hidden_text",
    zoom_to_size="auto"
)

output_path = "examples/advanced/mobile_tiny_text_4_3/output.html"
app.to_html(output_path)
print(f"Created {output_path}")
