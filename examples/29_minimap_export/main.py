from sivo import Sivo

svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2000 2000">
  <rect x="0" y="0" width="2000" height="2000" fill="#f8fafc" />

  <g id="zone_nw">
      <rect x="200" y="200" width="400" height="400" fill="#cbd5e1" />
      <text x="400" y="400" font-size="48" text-anchor="middle">North West</text>
  </g>

  <g id="zone_ne">
      <rect x="1400" y="200" width="400" height="400" fill="#cbd5e1" />
      <text x="1600" y="400" font-size="48" text-anchor="middle">North East</text>
  </g>

  <g id="zone_sw">
      <rect x="200" y="1400" width="400" height="400" fill="#cbd5e1" />
      <text x="400" y="1600" font-size="48" text-anchor="middle">South West</text>
  </g>

  <g id="zone_se">
      <rect x="1400" y="1400" width="400" height="400" fill="#cbd5e1" />
      <text x="1600" y="1600" font-size="48" text-anchor="middle">South East</text>
  </g>

  <circle cx="1000" cy="1000" r="100" fill="#ef4444" id="center_core" />
</svg>
"""

# Enable minimap and export capabilities
sivo_app = Sivo.from_string(svg_content, enable_minimap=True, enable_export=True)

sivo_app.map("zone_nw", tooltip="North West Zone", hover_color="#94a3b8")
sivo_app.map("zone_ne", tooltip="North East Zone", hover_color="#94a3b8")
sivo_app.map("zone_sw", tooltip="South West Zone", hover_color="#94a3b8")
sivo_app.map("zone_se", tooltip="South East Zone", hover_color="#94a3b8")
sivo_app.map("center_core", tooltip="Core Facility", glow=True)

import os

output_path = os.path.join(os.path.dirname(__file__), "minimap_export.html")
sivo_app.to_html(output_path)
print(f"Generated {output_path}")
