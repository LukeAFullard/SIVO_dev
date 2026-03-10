from sivo import Sivo

svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
  <!-- Base Map Layer -->
  <g id="layer_basemap">
      <rect x="50" y="50" width="900" height="500" fill="#f8fafc" stroke="#cbd5e1" stroke-width="4" rx="10"/>
      <path d="M 200 50 L 200 550" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="10,10"/>
      <path d="M 800 50 L 800 550" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="10,10"/>
  </g>

  <!-- Electrical Wiring Layer -->
  <g id="layer_wiring">
      <path id="wire1" d="M 100 300 L 900 300" stroke="#ef4444" stroke-width="5" fill="none"/>
      <path id="wire2" d="M 500 100 L 500 500" stroke="#ef4444" stroke-width="5" fill="none"/>
      <circle cx="500" cy="300" r="15" fill="#b91c1c"/>
  </g>

  <!-- HVAC Layer -->
  <g id="layer_hvac">
      <rect x="150" y="150" width="100" height="300" fill="#bae6fd" opacity="0.7"/>
      <rect x="750" y="150" width="100" height="300" fill="#bae6fd" opacity="0.7"/>
  </g>
</svg>
"""

# Must use render_mode="svg" to correctly toggle visibility of unmapped generic <g> layer wrappers
sivo_app = Sivo.from_string(svg_content, render_mode="svg")

# Add layer toggles to create an interactive legend
sivo_app.add_layer_toggle(label="Base Map", element_ids=["layer_basemap"], default_visible=True)
sivo_app.add_layer_toggle(label="Electrical Wiring", element_ids=["layer_wiring"], default_visible=True)
sivo_app.add_layer_toggle(label="HVAC Systems", element_ids=["layer_hvac"], default_visible=False) # Hidden by default

# Add standard interactive mapping to an element inside a layer
sivo_app.map("wire1", tooltip="Main Power Line")

import os

output_path = os.path.join(os.path.dirname(__file__), "layer_toggles.html")
sivo_app.to_html(output_path)
print(f"Generated {output_path}")
