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

# Add custom HTML overlays to perfectly anchor to the SVG shapes
# Using standard HTML elements. The JS runtime applies translate(-50%, -50%) to ensure true centering.

# 1. Text Overlay
text_html = '<div style="background: white; color: #1e293b; padding: 8px 16px; border-radius: 8px; font-weight: bold; font-family: sans-serif; font-size: 14px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); white-space: nowrap;">✨ Hello SIVO!</div>'
app.add_overlay("box-1", text_html, scale_with_zoom=True)

# 2. Figure/Image Overlay
figure_html = '<div style="background: white; padding: 4px; border-radius: 12px; box-shadow: 0 10px 15px rgba(0,0,0,0.1); display: flex; flex-direction: column; align-items: center;"><img src="https://images.unsplash.com/photo-1614332287897-cdc485fa562d?q=80&w=100&auto=format&fit=crop" width="80" height="80" style="border-radius: 8px;" /><span style="font-family: sans-serif; font-size: 10px; margin-top: 4px; color: #64748b;">Figure 1</span></div>'
app.add_overlay("box-2", figure_html, scale_with_zoom=True)

# 3. Simple Marker Overlay
marker_html = '<div style="width: 48px; height: 48px; background: #0f172a; border: 4px solid white; border-radius: 50%; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; font-family: sans-serif; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">X</div>'
app.add_overlay("box-3", marker_html, scale_with_zoom=True)

# Generate the output HTML
output_html = "examples/60_overlay_geometry_fix/index.html"
app.to_html(output_html)

print(f"✅ Success! Interactive SVG with perfectly aligned geometry overlays saved to: {output_html}")
print("Open this file in your browser, zoom in/out, and resize the window to verify the 'X' markers stay pinned to the center of the colored squares.")
