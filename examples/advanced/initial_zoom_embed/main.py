from sivo import Sivo
import os

def main():
    print("SIVO - Initial Zoom Example")

    # We will create a parent SVG with a tiny placeholder rectangle
    outer_svg = """<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">
  <!-- A background to give context -->
  <rect id="background" x="0" y="0" width="1000" height="1000" fill="#f8fafc" />

  <text x="500" y="100" font-family="sans-serif" font-size="40" text-anchor="middle" fill="#334155">
    SIVO Initial Zoom Embedding
  </text>

  <!-- A frame around the target area -->
  <rect x="230" y="230" width="540" height="540" fill="none" stroke="#94a3b8" stroke-width="4" rx="20" />

  <!-- This target element represents where the embedded SVG will go -->
  <!-- It is extremely tiny (5x5) so it's practically invisible until zoomed -->
  <rect id="target_zone" x="500" y="500" width="5" height="5" fill="#e2e8f0" />
</svg>"""

    # We will create an inner SVG with its own viewBox
    inner_svg = """<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle id="inner_bg" cx="50" cy="50" r="45" fill="#fef08a" stroke="#ca8a04" stroke-width="2" />
  <path id="inner_shape_1" d="M30 30 L50 20 L70 30 L70 60 L50 70 L30 60 Z" fill="#ef4444" />
  <circle id="inner_shape_2" cx="50" cy="50" r="10" fill="#3b82f6" />
</svg>"""

    # 1. Initialize the Sivo app with the outer SVG and layout_size 99%
    # We pass initial_zoom_to="target_zone" and initial_zoom_to_size="80%" so the map starts zoomed in
    app = Sivo.from_string(
        outer_svg,
        theme="light",
        disable_zoom_controls=False,
        layout_size="99%",
        initial_zoom_to="inner_bg",
        initial_zoom_to_size="90%"
    )

    # 2. Embed the inner SVG directly into the 'target_zone'
    app.embed_svg("target_zone", inner_svg, is_file=False, preserve_aspect_ratio=True, keep_target=False, scale_multiplier=1.0)

    # 3. Map interactivity directly to the embedded inner SVG elements
    app.map(
        "inner_bg",
        tooltip="Embedded Canvas",
        html="<h3>Inner SVG</h3><p>The map loaded already zoomed in to this dynamically embedded element!</p>",
        hover_color="#fde047"
    )

    app.map(
        "inner_shape_1",
        tooltip="Inner Hexagon",
        html="<p>Red hexagon from inner.svg</p>",
        color="#f87171",
        hover_color="#dc2626"
    )

    app.map(
        "inner_shape_2",
        tooltip="Micro Zoom Target",
        html="<p>Blue center dot from inner.svg.</p>",
        color="#60a5fa",
        hover_color="#2563eb",
        glow=True
    )

    # 5. Export to HTML
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    app.to_html(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
