from sivo import Sivo

svg_string = (
    '<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">\n'
    '    <rect id="dragRect" x="50" y="50" width="100" '
    'height="100" fill="#3498db" />\n'
    '    <circle id="dragCircle" cx="250" cy="100" r="50" fill="#e74c3c" />\n'
    '</svg>'
)

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

import os  # noqa: E402

output_path = os.path.join(os.path.dirname(__file__), "draggable_elements.html")  # noqa: E501
sivo_app.to_html(output_path)
print(f"Exported to {output_path}")
