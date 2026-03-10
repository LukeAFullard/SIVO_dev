from sivo import Sivo

svg_string = """
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <rect id="dragRect" x="50" y="50" width="100" height="100" fill="#3498db" />
    <circle id="dragCircle" cx="250" cy="100" r="50" fill="#e74c3c" />
</svg>
"""

sivo_app = Sivo.from_string(svg_string, render_mode="svg")

sivo_app.map(
    element_id="dragRect",
    tooltip="This rectangle is draggable",
    draggable=True
)

sivo_app.map(
    element_id="dragCircle",
    tooltip="This circle is draggable",
    draggable=True
)

import os

output_path = os.path.join(os.path.dirname(__file__), "draggable_elements.html")
sivo_app.to_html(output_path)
print(f"Exported to {output_path}")
