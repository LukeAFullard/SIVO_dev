from sivo import Sivo

svg_string = """
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <clipPath id="myClip">
            <circle cx="200" cy="200" r="100" />
        </clipPath>
        <mask id="myMask">
            <rect x="0" y="0" width="400" height="400" fill="white" />
            <circle cx="200" cy="200" r="100" fill="black" />
        </mask>
    </defs>

    <rect id="rectToClip" x="0" y="0" width="400" height="200" fill="#3498db" />
    <rect id="rectToMask" x="0" y="200" width="400" height="200" fill="#e74c3c" />
</svg>
"""

sivo_app = Sivo.from_string(svg_string, render_mode="svg")

sivo_app.map(
    element_id="rectToClip",
    tooltip="This rectangle is clipped by a circle",
    clip_path="url(#myClip)"
)

sivo_app.map(
    element_id="rectToMask",
    tooltip="This rectangle is masked by a circle",
    mask="url(#myMask)"
)

import os

output_path = os.path.join(os.path.dirname(__file__), "masking_clipping.html")
sivo_app.to_html(output_path)
print(f"Exported to {output_path}")
