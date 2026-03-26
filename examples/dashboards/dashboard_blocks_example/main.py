import os
from sivo import Sivo, SivoDashboard


# --- 1. Create a Primary Sivo Map Block ---
map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
    <rect id="bg" width="800" height="600" fill="#f8fafc" />
    <path id="region_north" d="M 100 100 L 700 100 L 700 300 L 100 300 Z" fill="#cbd5e1" stroke="#fff" stroke-width="2"/>
    <path id="region_south" d="M 100 300 L 700 300 L 700 500 L 100 500 Z" fill="#94a3b8" stroke="#fff" stroke-width="2"/>
    <text x="350" y="200" font-family="sans-serif" font-size="24" fill="#333" pointer-events="none">North Region</text>
    <text x="350" y="400" font-family="sans-serif" font-size="24" fill="#333" pointer-events="none">South Region</text>
</svg>"""

sivo_map = Sivo.from_string(map_svg, theme="light")

# --- Rich Media in the Details Panel ---
# By passing HTML directly into the 'html' parameter, you can inject rich text,
# images (via <img>), videos (via <video> or <iframe> embeds), and complex layouts.
# When a user clicks this region, the pre-built Details Panel automatically renders it.

north_html_content = """
<div style="font-family: sans-serif;">
    <h4 style="color: #3b82f6; margin-top: 0;">Operations: Stable</h4>
    <p>The Northern facilities are currently operating at peak efficiency.</p>
    <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=400&q=80"
         alt="Office Building"
         style="width: 100%; border-radius: 8px; margin-top: 10px;" />
</div>
"""

south_html_content = """
<div style="font-family: sans-serif;">
    <h4 style="color: #ef4444; margin-top: 0;">Operations: Delayed</h4>
    <p>Severe weather has impacted supply chain logistics in the Southern sector.</p>
    <!-- Example of embedding a YouTube video or an iframe -->
    <iframe width="100%" height="200" src="https://www.youtube.com/embed/dQw4w9WgXcQ?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 8px; margin-top: 10px;"></iframe>
</div>
"""

sivo_map.map(
    "region_north",
    hover_color="#3b82f6",
    html=north_html_content,
    panel_position="none", # "none" means it only updates the in-grid panels.
    callback_event="select_region",
    callback_payload={"revenue": "$1.2M", "users": "45,000", "status": "Stable"}
)

sivo_map.map(
    "region_south",
    hover_color="#ef4444",
    html=south_html_content,
    panel_position="right", # "right" overrides the grid panel, sliding out a global sidebar instead (OR behavior).
    callback_event="select_region",
    callback_payload={"revenue": "$0.8M", "users": "32,000", "status": "Delayed"}
)

# --- 2. Create a Secondary Sivo Chart Block ---
# You are not limited to just one SVG block! The grid automatically arranges multiple SVGs.
chart_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
    <rect width="400" height="400" fill="#ffffff" />
    <text x="200" y="40" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle" fill="#333">Quarterly Performance</text>
    <!-- A simple bar chart representation -->
    <rect id="bar1" x="50" y="200" width="80" height="150" fill="#3b82f6" />
    <rect id="bar2" x="160" y="100" width="80" height="250" fill="#10b981" />
    <rect id="bar3" x="270" y="250" width="80" height="100" fill="#ef4444" />
    <text x="90" y="380" font-family="sans-serif" text-anchor="middle">Q1</text>
    <text x="200" y="380" font-family="sans-serif" text-anchor="middle">Q2</text>
    <text x="310" y="380" font-family="sans-serif" text-anchor="middle">Q3</text>
</svg>"""

sivo_chart = Sivo.from_string(chart_svg, theme="light")
sivo_chart.map("bar1", tooltip="Q1 Revenue: $400,000")
sivo_chart.map("bar2", tooltip="Q2 Revenue: $850,000")
sivo_chart.map("bar3", tooltip="Q3 Revenue: $250,000")


# --- 3. Assemble the Dashboard ---
# Using the SivoDashboard to combine multiple interactive blocks without writing HTML or JS
dashboard = SivoDashboard(title="Executive Operations Dashboard")

# First, add the interactive ECharts map
dashboard.add_sivo_block("regional_map", sivo_map)

# Add a pre-built Details Panel. This automatically renders the `html` content of clicked elements.
dashboard.add_details_panel("region_details", title="Region Details", placeholder="Select a region on the map to view rich media details.")

# Add a pre-built Metrics Panel. This automatically renders the keys from `callback_payload` of clicked elements.
dashboard.add_metrics_panel("region_metrics", title="Key Metrics", metrics=["revenue", "users", "status"])

# Add the secondary SVG block. The CSS Grid will place this below the Details Panel or alongside the map,
# and gracefully stack all blocks vertically on mobile devices.
dashboard.add_sivo_block("quarterly_chart", sivo_chart)


# Export to a single HTML file
output_file = os.path.join(os.path.dirname(__file__), "output.html")
dashboard.to_html(output_file)

print(f"Successfully generated responsive no-code dashboard: {output_file}")
