from sivo import Sivo

svg_string = """
<svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect id="gradientRect" x="10" y="50" width="180" height="100" fill="#ccc" />
    <circle id="patternCircle" cx="300" cy="100" r="80" fill="#ccc" />
</svg>
"""

sivo_app = Sivo.from_string(svg_string)

# Map a linear gradient to the rectangle
# We set panel_position to "right" and add HTML to demonstrate the interaction
sivo_app.map(
    element_id="gradientRect",
    tooltip="This rectangle uses a linear gradient",
    html="<h3>Gradient Rectangle</h3><p>This rectangle features a linear gradient applied via SIVO.</p>",
    panel_position="right",
    fill_gradient={
        "type": "linear",
        "x": 0, "y": 0, "x2": 1, "y2": 1,
        "stops": [
            {"offset": 0, "color": "#3498db"},
            {"offset": 1, "color": "#2ecc71"}
        ]
    }
)

# Map an image pattern to the circle
# We set panel_position to "left" and add HTML to demonstrate the interaction
pattern_image_url = "https://www.transparenttextures.com/patterns/cubes.png"

sivo_app.map(
    element_id="patternCircle",
    tooltip="This circle uses an image pattern",
    html="<h3>Pattern Circle</h3><p>This circle features an image pattern applied via SIVO.</p>",
    panel_position="left",
    fill_pattern={
        "image": pattern_image_url,
        "repeat": "repeat"
    }
)

import os

output_path = os.path.join(os.path.dirname(__file__), "gradients_patterns.html")
sivo_app.to_html(output_path)
print(f"Exported to {output_path}")
