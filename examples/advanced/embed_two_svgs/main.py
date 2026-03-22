from sivo import Sivo
import os

def main():
    print("SIVO - Embed Two SVGs Example")

    # We will create a parent SVG with two tiny placeholder rectangles
    outer_svg = """<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">
  <rect id="background" x="0" y="0" width="1000" height="1000" fill="#f1f5f9" />

  <text x="500" y="100" font-family="sans-serif" font-size="40" text-anchor="middle" fill="#0f172a">
    Multi-SVG Journey
  </text>

  <!-- Tiny targets far away from each other -->
  <rect id="target_a" x="200" y="500" width="5" height="5" fill="#e2e8f0" />
  <rect id="target_b" x="800" y="500" width="5" height="5" fill="#e2e8f0" />

  <rect id="start_btn" x="400" y="850" width="200" height="60" fill="#2563eb" rx="10" />
  <text x="500" y="890" font-family="sans-serif" font-size="24" text-anchor="middle" fill="#ffffff" pointer-events="none">
    Start Journey
  </text>
</svg>"""

    # First embedded SVG
    svg_a = """<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <rect id="bg_a" x="0" y="0" width="100" height="100" fill="#fef08a" rx="10" />
  <text x="50" y="30" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#854d0e">Location A</text>

  <circle cx="50" cy="50" r="15" fill="#f59e0b" />

  <!-- Button inside SVG A to go to B -->
  <rect id="btn_to_b" x="20" y="70" width="60" height="20" fill="#eab308" rx="5" />
  <text x="50" y="83" font-family="sans-serif" font-size="8" text-anchor="middle" fill="#ffffff" pointer-events="none">Go to B</text>
</svg>"""

    # Second embedded SVG
    svg_b = """<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <rect id="bg_b" x="0" y="0" width="100" height="100" fill="#a7f3d0" rx="10" />
  <text x="50" y="30" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#065f46">Location B</text>

  <polygon points="50,40 60,60 40,60" fill="#10b981" />

  <!-- Button inside SVG B to go home -->
  <rect id="btn_to_home" x="20" y="70" width="60" height="20" fill="#059669" rx="5" />
  <text x="50" y="83" font-family="sans-serif" font-size="8" text-anchor="middle" fill="#ffffff" pointer-events="none">Go Home</text>
</svg>"""

    # 1. Initialize the Sivo app
    app = Sivo.from_string(outer_svg, theme="light", disable_zoom_controls=False, layout_size="99%")

    # 2. Embed both SVGs into their respective tiny targets
    app.embed_svg("target_a", svg_a, is_file=False, preserve_aspect_ratio=True, keep_target=False, scale_multiplier=2.0)
    app.embed_svg("target_b", svg_b, is_file=False, preserve_aspect_ratio=True, keep_target=False, scale_multiplier=2.0)

    # 3. Map Outer SVG Interactivity
    app.map("background", tooltip="World Map")

    # Map the start button to zoom into Location A
    app.map(
        "start_btn",
        tooltip="Click to start",
        hover_color="#1d4ed8",
        zoom_to="bg_a",
        zoom_to_size="80%",
        zoom_duration_ms=1000
    )

    # 4. Map Inner SVG A Interactivity
    app.map("bg_a", tooltip="Location A (Yellow Area)")

    # Map the button inside A to zoom across the map to Location B
    app.map(
        "btn_to_b",
        tooltip="Click to travel to B",
        hover_color="#ca8a04",
        zoom_to="bg_b",
        zoom_to_size="80%",
        zoom_duration_ms=1500
    )

    # 5. Map Inner SVG B Interactivity
    app.map("bg_b", tooltip="Location B (Green Area)")

    # Map the button inside B to zoom all the way back out to the main background
    app.map(
        "btn_to_home",
        tooltip="Click to return home",
        hover_color="#047857",
        zoom_to="background",
        zoom_to_size="99%",
        zoom_duration_ms=1500
    )

    # 6. Export to HTML
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    app.to_html(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
