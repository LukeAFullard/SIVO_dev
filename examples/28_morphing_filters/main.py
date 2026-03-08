from sivo import Sivo

svg_string = """
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <filter id="blurFilter">
            <feGaussianBlur stdDeviation="5" />
        </filter>
        <filter id="dropShadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="red" />
        </filter>
    </defs>
    <!-- We must have the same number of path commands for smooth morphing if we were using CSS, but native SMIL/anime can handle mismatch depending on library, ECharts handles basic morphing nicely if render_mode is used -->
    <!-- For CSS native d-path morphing to work smoothly in Chromium, the paths should ideally have the same number/type of commands. We use a 4-point polygon to a 4-point polygon (triangle with a redundant point). -->
    <path id="myMorphPath" d="M50,50 L150,50 L150,150 L50,150 Z" fill="#3498db" />
    <circle id="myFilterCircle" cx="250" cy="100" r="50" fill="#e74c3c" />
</svg>
"""

# Enable render_mode='svg' to use native SVG properties
sivo_app = Sivo.from_string(svg_string, render_mode="svg")

# Map path morphing
sivo_app.map(
    element_id="myMorphPath",
    tooltip="This path will morph to a triangle",
    morph_to_path="M100,20 L180,180 L20,180 Z",
    morph_duration_ms=2000
)

# Map an SVG filter
sivo_app.map(
    element_id="myFilterCircle",
    tooltip="This circle has a blur filter applied",
    filter="url(#dropShadow)"
)

sivo_app.to_html("examples/28_morphing_filters/morphing_filters.html")
print("Exported to examples/28_morphing_filters/morphing_filters.html")
