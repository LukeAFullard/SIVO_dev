from sivo import Sivo

svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" style="background:#0f172a;">
  <rect id="kpi_box1" x="100" y="200" width="300" height="200" fill="#1e293b" rx="10"/>
  <text x="250" y="260" font-size="24" fill="#94a3b8" font-family="sans-serif" text-anchor="middle">Total Revenue</text>
  <text id="revenue_val" x="250" y="340" font-size="64" fill="#38bdf8" font-family="sans-serif" font-weight="bold" text-anchor="middle">0</text>

  <rect id="kpi_box2" x="600" y="200" width="300" height="200" fill="#1e293b" rx="10"/>
  <text x="750" y="260" font-size="24" fill="#94a3b8" font-family="sans-serif" text-anchor="middle">Active Users</text>
  <text id="users_val" x="750" y="340" font-size="64" fill="#10b981" font-family="sans-serif" font-weight="bold" text-anchor="middle">0</text>
</svg>
"""

# Must use render_mode="svg" for odometers as it manipulates native SVG text nodes
sivo_app = Sivo.from_string(svg_content, render_mode="svg")

# Map odometer properties to the text nodes
sivo_app.map(
    element_id="revenue_val",
    odometer_value=124500.50,
    odometer_duration_ms=3000,
    odometer_format="currency"
)

sivo_app.map(
    element_id="users_val",
    odometer_value=8432,
    odometer_duration_ms=2500,
    odometer_format="int"
)

import os

output_path = os.path.join(os.path.dirname(__file__), "odometers.html")
sivo_app.to_html(output_path)
print(f"Generated {output_path}")
