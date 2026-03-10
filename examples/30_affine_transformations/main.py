from sivo import Sivo

svg_string = """
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <!-- Drawing ghost elements to clearly show the "before" state underneath the transformed ones -->
    <rect x="50" y="50" width="100" height="100" fill="none" stroke="#ccc" stroke-dasharray="5,5" />
    <rect id="rectRotate" x="50" y="50" width="100" height="100" fill="#3498db" />

    <circle cx="250" cy="100" r="50" fill="none" stroke="#ccc" stroke-dasharray="5,5" />
    <circle id="circleScale" cx="250" cy="100" r="50" fill="#e74c3c" />

    <polygon points="50,250 150,250 100,350" fill="none" stroke="#ccc" stroke-dasharray="5,5" />
    <polygon id="polyTranslate" points="50,250 150,250 100,350" fill="#2ecc71" />
</svg>
"""

# Native SVG rendering required to apply transforms to the DOM elements directly
sivo_app = Sivo.from_string(svg_string, render_mode="svg")

sivo_app.map(
    element_id="rectRotate",
    tooltip="Rotated 45 degrees",
    transform="rotate(45 100 100)" # rotate(angle cx cy)
)

sivo_app.map(
    element_id="circleScale",
    tooltip="Scaled by 1.25",
    transform="scale(1.25) translate(-50 -20)" # Scale also affects translation implicitly in SVG, so we offset to keep centered roughly
)

sivo_app.map(
    element_id="polyTranslate",
    tooltip="Translated by (100, 50)",
    transform="translate(100 50)"
)

import os

output_path = os.path.join(os.path.dirname(__file__), "affine_transformations.html")
sivo_app.to_html(output_path)
print(f"Exported to {output_path}")
