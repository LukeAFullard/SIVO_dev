from sivo import Sivo

svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
  <rect id="gallery" x="100" y="100" width="200" height="200" fill="#e5e7eb" stroke="#94a3b8" stroke-width="2"/>
  <text x="200" y="200" font-size="24" text-anchor="middle">Art Gallery</text>

  <rect id="cafe" x="700" y="100" width="200" height="200" fill="#e5e7eb" stroke="#94a3b8" stroke-width="2"/>
  <text x="800" y="200" font-size="24" text-anchor="middle">Cafe</text>

  <rect id="giftshop" x="400" y="400" width="200" height="150" fill="#e5e7eb" stroke="#94a3b8" stroke-width="2"/>
  <text x="500" y="480" font-size="24" text-anchor="middle">Gift Shop</text>
</svg>
"""

sivo_app = Sivo.from_string(svg_content)

# Map standard tooltips for the tour to trigger
sivo_app.map("gallery", tooltip="Main Art Gallery", html="<p>Featuring modern artists.</p>")
sivo_app.map("cafe", tooltip="Museum Cafe", html="<p>Coffee and pastries.</p>")
sivo_app.map("giftshop", tooltip="Gift Shop", html="<p>Souvenirs and books.</p>")

# Define Guided Tour Steps
steps = [
    {
        "content": "<h3>Welcome to the Museum Tour</h3><p>We'll guide you through the main exhibits. Click <b>Next</b> to begin.</p>",
    },
    {
        "content": "<h3>1. Art Gallery</h3><p>First stop: the main exhibition hall.</p>",
        "zoom_to": "gallery",
        "zoom_level": 2.5,
        "show_tooltips": ["gallery"]
    },
    {
        "content": "<h3>2. Museum Cafe</h3><p>Take a break and grab a coffee.</p>",
        "zoom_to": "cafe",
        "zoom_level": 2.5,
        "show_tooltips": ["cafe"]
    },
    {
        "content": "<h3>3. Gift Shop</h3><p>Don't forget to exit through the gift shop!</p>",
        "zoom_to": "giftshop",
        "zoom_level": 2.5,
        "show_tooltips": ["giftshop"]
    },
    {
        "content": "<h3>End of Tour</h3><p>Enjoy the rest of your visit!</p>"
    }
]

# Bind the tour to the app
sivo_app.bind_tour(steps)

import os

output_path = os.path.join(os.path.dirname(__file__), "guided_tour.html")
sivo_app.to_html(output_path)
print(f"Generated {output_path}")
