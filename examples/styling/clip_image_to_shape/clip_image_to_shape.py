import os
from sivo import Sivo

# 1. Create a dummy SVG with a circle and a rectangle
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
    <!-- A circular shape -->
    <circle id="my_circle" cx="200" cy="300" r="150" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />

    <!-- A rectangular shape with rounded corners -->
    <rect id="my_rect" x="450" y="150" width="250" height="300" rx="20" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />

    <!-- A complex path shape (star) -->
    <path id="my_star" d="M 400 50 L 430 140 L 520 140 L 450 200 L 480 290 L 400 240 L 320 290 L 350 200 L 280 140 L 370 140 Z" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />
</svg>
"""

# Initialize Sivo directly from the SVG string
# Using default_panel_position="none" so we don't open an empty side panel when shapes are clicked
app = Sivo.from_string(svg_content, default_panel_position="none", title="Image Clipping Example")

# 2. Clip a square image to the circular shape
app.clip_image_to_shape(
    element_id="my_circle",
    image_url="https://images.unsplash.com/photo-1579546929518-9e396f3cc809", # A square-ish colorful gradient image
    preserve_aspect_ratio="xMidYMid slice"
)

# Map an interaction to the circle to prove it's still interactive
app.map(
    element_id="my_circle",
    tooltip="I am a circle with a clipped image!",
    hover_color="rgba(0, 0, 0, 0.2)" # Add a dark tint on hover
)

# 3. Clip an image to the rectangle with scaling, rotation, and translation panning
app.clip_image_to_shape(
    element_id="my_rect",
    image_url="https://images.unsplash.com/photo-1557683316-973673baf926",
    scale=1.5,
    rotate=15, # Rotate 15 degrees
    translate_x=-30, # Pan the image 30 pixels left within the clipped region
    translate_y=20,  # Pan the image 20 pixels down within the clipped region
    opacity=0.8
)

# Map an interaction to the rectangle
app.map(
    element_id="my_rect",
    tooltip="I am a rectangle with a scaled, rotated image!",
    hover_color="rgba(255, 255, 255, 0.3)" # Add a light tint on hover
)

# 4. Clip an image to the complex star shape
app.clip_image_to_shape(
    element_id="my_star",
    image_url="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe",
    scale=1.2
)

# Map an interaction to the star
app.map(
    element_id="my_star",
    tooltip="I am a complex star shape with a clipped image!",
    glow=True
)

# 5. Export the result to an HTML file
import os
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, "clip_image_to_shape.html")
app.to_html(output_path)

print(f"Successfully generated {output_path}")
