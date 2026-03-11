import os
from sivo import Sivo

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
    <rect id="bg" width="400" height="300" fill="#fcfcfc"/>
    <rect id="city_trigger" x="150" y="100" width="100" height="100" rx="10" fill="#1f77b4" />
    <text x="200" y="220" font-family="sans-serif" font-size="20" text-anchor="middle" fill="#333">Click for City Stats</text>
</svg>"""

sivo_app = Sivo.from_string(svg_content, title="Pictorial Bar Chart (Buildings)")

# Data
categories = ['NYC', 'LA', 'Chicago', 'Houston']
data = [180, 150, 110, 80]

# Add a pictorial bar chart that pops up when clicking the blue rounded rect
# Here we use standard 'rect' symbol to mimic building blocks
sivo_app.map_pictorial_bar_chart(
    element_id="city_trigger",
    title="City Skyscraper Count",
    data=data,
    categories=categories,
    symbol="rect",
    symbol_repeat=True,
    symbol_size=[30, 10], # 30px wide, 10px tall blocks
    color="#1f77b4",
    tooltip="View Skyscraper Data",
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
