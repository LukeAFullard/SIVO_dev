import os
from sivo import Sivo
from sivo.core.project import SivoProject

svg_content1 = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
  <rect id="map_bg" width="1000" height="600" fill="#f8fafc" />
  <text x="500" y="50" font-size="24" text-anchor="middle" font-weight="bold">Global Monitoring Dashboard</text>

  <path id="region_a" d="M 100 100 L 400 100 L 400 400 L 100 400 Z" fill="#e2e8f0" stroke="#94a3b8" />
  <text x="250" y="250" font-size="18" text-anchor="middle">Click to drill through</text>

  <path id="region_b" d="M 500 100 L 900 100 L 900 400 L 500 400 Z" fill="#e2e8f0" stroke="#94a3b8" />
  <text x="700" y="250" font-size="18" text-anchor="middle">Click for Confetti!</text>

  <!-- Add paths so the parser computes their centers correctly -->
  <path id="node_1" d="M 240 190 L 260 190 L 260 210 L 240 210 Z" fill="transparent" />
  <path id="node_2" d="M 290 290 L 310 290 L 310 310 L 290 310 Z" fill="transparent" />
  <path id="node_3" d="M 690 290 L 710 290 L 710 310 L 690 310 Z" fill="transparent" />
</svg>
"""

svg_content2 = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
  <rect id="map_bg2" width="1000" height="600" fill="#f8fafc" />
  <text x="500" y="50" font-size="24" text-anchor="middle" font-weight="bold">Region A Details</text>

  <path id="sub_region_1" d="M 200 100 L 800 100 L 800 500 L 200 500 Z" fill="#e2e8f0" stroke="#94a3b8" />
  <text x="500" y="300" font-size="18" text-anchor="middle">Zoom transition successful!</text>
</svg>
"""

# Create the first SIVO app from the first SVG
sivo_app = Sivo.from_string(svg_content1)

# Map Drill Through to a new view ID. This tells SIVO to transition to "region_a_details" when "region_a" is clicked.
sivo_app.map("region_a", drill_through="region_a_details", drill_transition="zoom")

# Map Confetti Gamification. When "region_b" is clicked, it will trigger a confetti animation.
sivo_app.map("region_b", confetti={"particle_count": 200, "spread": 90}, tooltip="Goal Reached!", panel_position="right", html="<h1>Goal Reached!</h1><p>You have triggered the confetti gamification!</p>")

# Add Pulse Markers (Live Telemetry). Overlays proportional symbols with pulse animation enabled.
live_data = {
    "node_1": 100,
    "node_2": {"value": 50, "color": "#3b82f6"}, # Blue marker
    "node_3": {"value": 75, "color": "#10b981"}  # Green marker
}

sivo_app.apply_proportional_symbols(live_data, min_size=15, max_size=30, color="#ef4444", is_pulse=True)

# Create the second SIVO app for the drilled-through view
sivo_app2 = Sivo.from_string(svg_content2)

# Create a SivoProject, specifying the initial view ID
project = SivoProject("default_view")

# Add the views to the project
project.add_view("default_view", sivo_app)
project.add_view("region_a_details", sivo_app2)

# Set the output path relative to this script
output_path = os.path.join(os.path.dirname(__file__), "pulse_confetti.html")

# Generate the standalone HTML file encompassing all views
project.to_html(output_path=output_path)
print(f"Generated {output_path}")
