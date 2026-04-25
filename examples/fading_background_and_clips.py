from sivo.core.sivo import Sivo

svg_string = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
    <!-- Base background rect -->
    <rect id="bg_rect" x="0" y="0" width="800" height="600" fill="#f8fafc"/>

    <text x="400" y="50" font-size="32" font-family="sans-serif" font-weight="bold" fill="#334155" text-anchor="middle">SIVO Fading Capabilities Demo</text>

    <!-- Target areas for clipped images -->
    <!-- Top Left: SVG background image (fade_in) -->
    <!-- Top Right: SVG background image (fade_pulse) -->

    <g transform="translate(100, 150)">
        <text x="150" y="-20" font-size="18" font-family="sans-serif" fill="#64748b" text-anchor="middle">HTML Overlay (Fade In)</text>
        <rect id="html_overlay_fade_in" x="0" y="0" width="300" height="200" rx="15" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
    </g>

    <g transform="translate(450, 150)">
        <text x="150" y="-20" font-size="18" font-family="sans-serif" fill="#64748b" text-anchor="middle">HTML Overlay (Fade Pulse)</text>
        <circle id="html_overlay_fade_pulse" cx="150" cy="100" r="100" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
    </g>

    <g transform="translate(100, 450)">
        <text x="150" y="-20" font-size="18" font-family="sans-serif" fill="#64748b" text-anchor="middle">Native SVG Image (Fade In)</text>
        <polygon id="svg_image_fade_in" points="150,0 300,200 0,200" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
    </g>

    <g transform="translate(450, 450)">
        <text x="150" y="-20" font-size="18" font-family="sans-serif" fill="#64748b" text-anchor="middle">Native SVG Image (Fade Pulse)</text>
        <rect id="svg_image_fade_pulse" x="0" y="0" width="300" height="200" rx="15" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
    </g>
</svg>
"""

def generate():
    app = Sivo.from_string(svg_string)

    # 1. Container Background Image (Fade In)
    app.add_background_image(
        "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?q=80&w=2070",
        opacity=0.3,
        fade_in=True,
        fade_duration_ms=4000
    )

    # 2. Clip image using HTML Overlay (Fade In)
    app.clip_image_to_shape(
        "html_overlay_fade_in",
        "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=2070",
        use_html_overlay=True,
        fade_in=True,
        fade_duration_ms=3000
    )

    # 3. Clip image using HTML Overlay (Fade Pulse)
    app.clip_image_to_shape(
        "html_overlay_fade_pulse",
        "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=2072",
        use_html_overlay=True,
        fade_pulse=True,
        fade_duration_ms=4000,
        fade_start_time_ms=1000
    )

    # 4. Clip image natively inside the SVG (Fade In)
    app.clip_image_to_shape(
        "svg_image_fade_in",
        "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=2070",
        use_html_overlay=False,
        fade_in=True,
        fade_duration_ms=3000
    )

    # 5. Clip image natively inside the SVG (Fade Pulse)
    app.clip_image_to_shape(
        "svg_image_fade_pulse",
        "https://images.unsplash.com/photo-1505144808419-1957a94ca61e?q=80&w=2000",
        use_html_overlay=False,
        fade_pulse=True,
        fade_duration_ms=4000,
        fade_start_time_ms=1000
    )

    app.to_html("fading_capabilities_demo.html")
    print("Successfully generated fading_capabilities_demo.html")

if __name__ == "__main__":
    generate()
