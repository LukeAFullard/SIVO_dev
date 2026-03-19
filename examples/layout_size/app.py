import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from sivo import Sivo

svg_content = """<svg viewBox="0 0 200 500" xmlns="http://www.w3.org/2000/svg">
    <rect id="background" width="200" height="500" fill="#f0f0f0" stroke="#cccccc" stroke-width="5" />
    <circle id="center_dot" cx="100" cy="250" r="30" fill="#ff5722" />
    <text x="100" y="350" font-family="Arial" font-size="14" text-anchor="middle" fill="#333333">
        SIVO Layout Size
    </text>
    <text x="100" y="380" font-family="Arial" font-size="10" text-anchor="middle" fill="#666666">
        Scales to 99% automatically!
    </text>
</svg>"""

# Using layout_size="99%" ensures that no matter the screen size (mobile, desktop, ultrawide),
# the SVG will scale so its longest dimension takes up exactly 99% of the screen.
# This prevents the graphic from looking tiny with massive blank white borders.
app = Sivo.from_string(
    svg_content,
    layout_size="99%",
    title="Responsive Layout Demo"
)

app.map(
    element_id="center_dot",
    hover_color="#e64a19",
    html="<h3>Center</h3><p>This is the center of the scalable graphic.</p>"
)

# Render to an HTML file
output_path = os.path.join(os.path.dirname(__file__), "layout_demo.html")
with open(output_path, "w") as f:
    f.write(app.to_html())

print(f"Successfully created {output_path}! Open this file in your browser to see the responsive layout in action.")
