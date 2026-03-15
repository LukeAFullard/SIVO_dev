from sivo import Sivo
from sivo.core.config import ProjectConfig
import os

# Create a clean directory
os.makedirs("examples/60_overlay_geometry_fix", exist_ok=True)

# Generate a simple SVG file with distinct shapes to test overlay alignment
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
    <rect width="800" height="600" fill="#f0f4f8" />

    <!-- Top Left Box -->
    <rect id="box-1" x="100" y="100" width="100" height="100" fill="#f87171" rx="12" />

    <!-- Center Box -->
    <rect id="box-2" x="350" y="250" width="100" height="100" fill="#4ade80" rx="12" />

    <!-- Bottom Right Box -->
    <rect id="box-3" x="600" y="400" width="100" height="100" fill="#60a5fa" rx="12" />
</svg>"""

svg_path = "examples/60_overlay_geometry_fix/test_geometry.svg"
with open(svg_path, "w") as f:
    f.write(svg_content)

# Initialize the App
app = Sivo.from_svg(
    svg_path,
    title="HTML Overlay Geometry Test",
    subtitle="The black HTML overlays should stay perfectly centered on the colored SVG rectangles, even when zooming or resizing the window on mobile.",
    theme="light"
)

# Add custom HTML overlays to perfectly anchor and SCALE to the SVG shapes.
# The JS runtime now applies exact width/height from the ECharts affine matrix, so 100% width fits the box perfectly.

# 1. Responsive Text Box Overlay
# It spans the full width of the box.
text_html = '<div style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.2); border-radius: 12px;"><span style="color: #ffffff; font-weight: 800; font-family: sans-serif; font-size: 18px; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">BOX 1</span></div>'
app.add_overlay("box-1", text_html, scale_with_zoom=True)

# 2. Figure/Image Overlay
# Scales exactly inside the bounding box.
figure_html = '<div style="width: 100%; height: 100%; padding: 4px; box-sizing: border-box; border-radius: 12px; display: flex; flex-direction: column; align-items: center;"><img src="https://images.unsplash.com/photo-1614332287897-cdc485fa562d?q=80&w=100&auto=format&fit=crop" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; box-shadow: 0 10px 15px rgba(0,0,0,0.3);" /></div>'
app.add_overlay("box-2", figure_html, scale_with_zoom=True)

# 3. Formatted Content Overlay
# Utilizing the flexible box dimensions to flow text
content_html = '<div style="width: 100%; height: 100%; padding: 12px; box-sizing: border-box; background: rgba(15, 23, 42, 0.8); border-radius: 12px; color: white; display: flex; flex-direction: column; justify-content: space-between;"><span style="font-weight: 900; font-family: sans-serif; font-size: 24px;">$42M</span><span style="font-family: sans-serif; font-size: 12px; color: #94a3b8;">Revenue Q3</span></div>'
app.add_overlay("box-3", content_html, scale_with_zoom=True)

# Generate the output HTML
output_html = "examples/60_overlay_geometry_fix/index.html"
app.to_html(output_html)

print(f"✅ Success! Interactive SVG with perfectly aligned geometry overlays saved to: {output_html}")
print("Open this file in your browser, zoom in/out, and resize the window to verify the 'X' markers stay pinned to the center of the colored squares.")
