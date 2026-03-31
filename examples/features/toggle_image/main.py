from sivo.core.project import SivoProject
from sivo.core.sivo import Sivo

svg_str = """<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">
    <rect id="bg" x="0" y="0" width="1000" height="1000" fill="#333" rx="15" />
    <rect id="button" x="400" y="850" width="200" height="80" fill="#007bff" rx="10" class="btn" />
</svg>"""

app = Sivo.from_string(
    svg_str,
    title="Toggle Image Example",
    subtitle="Click the button below to cycle through background images.",
    layout_size="100%",
    theme="dark"
)

app.add_scalable_text(
    target_id="button",
    text="Toggle Image",
    color="#fff",
    font_weight="bold",
    align="center",
    interactive=True
)

# 3. Define a list of image URLs to cycle through
image_urls = [
    "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?w=800&q=80", # Nature
    "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=800&q=80", # City
    "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=800&q=80"  # Tech
]

# 4. Map the toggle_image action to the button, targeting the background ('bg')
app.map(
    "button",
    toggle_image={
        "target_id": "bg",
        "image_urls": image_urls
    },
    hover_color="#0056b3"
)

# 5. Ensure bg has an entry so it exists in ECharts
app.map("bg")

# Save HTML output to current directory
import os
output_path = os.path.join(os.path.dirname(__file__), "output.html")
app.to_html(output_path)
print(f"Generated toggle_image example at {output_path}")