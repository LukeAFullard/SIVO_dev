from sivo import Sivo
import os

def main():
    print("SIVO - Embed SVG Example")

    # We will create a parent SVG with a tiny placeholder rectangle
    outer_svg = """<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">
  <!-- A background to give context -->
  <rect id="background" x="0" y="0" width="1000" height="1000" fill="#f8fafc" />

  <text x="500" y="100" font-family="sans-serif" font-size="40" text-anchor="middle" fill="#334155">
    SIVO SVG Embedding
  </text>

  <!-- A frame around the target area -->
  <rect x="230" y="230" width="540" height="540" fill="none" stroke="#94a3b8" stroke-width="4" rx="20" />

  <!-- This target element represents where the embedded SVG will go -->
  <!-- It is extremely tiny (5x5) so it's practically invisible until zoomed -->
  <rect id="target_zone" x="500" y="500" width="5" height="5" fill="#e2e8f0" />

  <rect id="button" x="400" y="850" width="200" height="60" fill="#3b82f6" rx="10" />
  <text x="500" y="890" font-family="sans-serif" font-size="24" text-anchor="middle" fill="#ffffff" pointer-events="none">
    Zoom to Inner
  </text>
</svg>"""

    # We will create an inner SVG with its own viewBox
    inner_svg = """<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle id="inner_bg" cx="50" cy="50" r="45" fill="#fef08a" stroke="#ca8a04" stroke-width="2" />
  <path id="inner_shape_1" d="M30 30 L50 20 L70 30 L70 60 L50 70 L30 60 Z" fill="#ef4444" />
  <circle id="inner_shape_2" cx="50" cy="50" r="10" fill="#3b82f6" />
</svg>"""

    # 1. Initialize the Sivo app with the outer SVG and layout_size 99%
    app = Sivo.from_string(outer_svg, theme="light", disable_zoom_controls=False, layout_size="99%")

    # 2. Embed the inner SVG directly into the 'target_zone'
    # We set preserve_aspect_ratio=True to uniformly scale the circle without stretching
    app.embed_svg("target_zone", inner_svg, is_file=False, preserve_aspect_ratio=True, keep_target=False)

    # 3. Map interactivity on the main SVG elements
    app.map(
        "background",
        tooltip="Main Canvas Background",
        html="<p>This is the outer SVG canvas.</p>"
    )

    # Map the button to dynamically zoom into the "inner_bg" bounding box, fitting it to 99% of the viewport.
    app.map(
        "button",
        tooltip="Click to Zoom",
        html="<p>Navigating visually into the microscopic embedded SVG.</p>",
        hover_color="#2563eb",
        zoom_to="inner_bg",
        zoom_to_size="99%",
        zoom_duration_ms=1500
    )

    # 4. Map interactivity directly to the embedded inner SVG elements!
    # Because Sivo parsed and injected them natively, their IDs work seamlessly.
    app.map(
        "inner_bg",
        tooltip="Embedded Canvas",
        html="<h3>Inner SVG</h3><p>This element was embedded dynamically into a microscopic 5x5 bounding box.</p>",
        hover_color="#fde047"
    )

    app.map(
        "inner_shape_1",
        tooltip="Inner Hexagon",
        html="<p>Red hexagon from inner.svg</p>",
        color="#f87171",
        hover_color="#dc2626",
        zoom_to="inner_shape_1",
        zoom_to_size="50%"
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
