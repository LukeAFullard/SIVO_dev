import os
from sivo import Sivo, SivoDashboard


# --- 1. Create a Base Sivo Map Block ---
map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
    <rect id="bg" width="1000" height="600" fill="#f8fafc" />
    <path id="state_ca" d="M 100 100 L 300 100 L 250 400 L 150 400 Z" fill="#e2e8f0" stroke="#fff" stroke-width="2"/>
    <path id="state_tx" d="M 400 300 L 700 250 L 650 550 L 350 500 Z" fill="#e2e8f0" stroke="#fff" stroke-width="2"/>
    <path id="state_ny" d="M 750 100 L 950 120 L 900 250 L 700 220 Z" fill="#e2e8f0" stroke="#fff" stroke-width="2"/>

    <text x="200" y="250" font-family="sans-serif" font-size="20" fill="#333" pointer-events="none" text-anchor="middle">CA</text>
    <text x="525" y="400" font-family="sans-serif" font-size="20" fill="#333" pointer-events="none" text-anchor="middle">TX</text>
    <text x="825" y="175" font-family="sans-serif" font-size="20" fill="#333" pointer-events="none" text-anchor="middle">NY</text>
</svg>"""

sivo_map = Sivo.from_string(map_svg, theme="light", title="National Sales Heatmap", subtitle="Hover or click for region details")

# --- 2. Advanced Feature: Choropleth ---
# Instead of manually mapping colors, we feed SIVO a data dictionary and it calculates a gradient.
sales_data = {
    "state_ca": 1250000,
    "state_tx": 850000,
    "state_ny": 2100000
}
sivo_map.apply_choropleth(sales_data, min_color="#eff6ff", max_color="#1e3a8a")

# --- 3. Advanced Feature: Path Animations ---
# Pulse the top-performing state path
sivo_map.map("state_ny", animation="pulse")

# Add rich interaction payloads for the Dashboard's no-code panels
sivo_map.map(
    "state_ca",
    html="<h4>California Operations</h4><p>Steady growth in Q3. Expanding warehouse capacity.</p>",
    callback_event="select",
    callback_payload={"revenue": "$1.25M", "growth": "+12%", "status": "On Track"}
)

sivo_map.map(
    "state_tx",
    html="<h4>Texas Operations</h4><p>Supply chain constraints identified in Houston hub.</p>",
    callback_event="select",
    callback_payload={"revenue": "$850K", "growth": "-3%", "status": "Action Required"}
)

sivo_map.map(
    "state_ny",
    html="<h4>New York Operations</h4><p>Record-breaking sales driven by new B2B partnerships.</p><img src='https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=400&q=80' style='width:100%; border-radius:8px;'/>",
    callback_event="select",
    callback_payload={"revenue": "$2.1M", "growth": "+25%", "status": "Exceeding Targets"}
)

# --- 4. Assemble the Advanced Dashboard ---
dashboard = SivoDashboard(title="Q3 Executive Insights")

# Add the interactive, animated choropleth map
dashboard.add_sivo_block("heat_map", sivo_map)

# Add standard No-Code panels that automatically react to map clicks
dashboard.add_metrics_panel("performance_metrics", title="Region Performance", metrics=["revenue", "growth", "status"])
dashboard.add_details_panel("region_insights", title="Executive Summary", placeholder="Click a state to view local operational notes.")

# Export the dashboard
output_file = os.path.join(os.path.dirname(__file__), "output.html")
dashboard.to_html(output_file)

print(f"Successfully generated advanced dashboard: {output_file}")
