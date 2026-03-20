import os
from sivo import Sivo

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
    <rect id="bg" width="400" height="300" fill="#f0f0f0"/>
    <circle id="forest_trigger" cx="200" cy="150" r="50" fill="#2ca02c"/>
    <text x="200" y="220" font-family="sans-serif" font-size="20" text-anchor="middle" fill="#333">Click the forest!</text>
</svg>"""

sivo_app = Sivo.from_string(svg_content, title="Pictorial Bar Chart Example")

# Data
categories = ['Pine', 'Oak', 'Maple', 'Birch']
data = [120, 80, 50, 90]

tree_path = 'path://M150 0 L75 200 L225 200 Z'

sivo_app.map_pictorial_bar_chart(
    element_id="forest_trigger",
    title="Forest Density",
    data=data,
    categories=categories,
    symbol=tree_path,
    symbol_repeat=True,
    symbol_size=[20, 20],
    color="#2ca02c",
    tooltip="View Forest Data",
    panel_position="right",
    extra_options={
        "series": [{
            "symbolMargin": 2,
            "z": 10
        }],
        "xAxis": {
            "axisLine": {"show": False},
            "axisTick": {"show": False},
            "splitLine": {"show": False}
        },
        "yAxis": {
            "axisLine": {"show": False},
            "axisTick": {"show": False},
            "splitLine": {"show": False}
        }
    }
)

output_path = os.path.join(os.path.dirname(__file__), "output.html")
html_str = sivo_app.to_html()

with open(output_path, "w") as f:
    f.write(html_str)

print(f"Generated {output_path}")
