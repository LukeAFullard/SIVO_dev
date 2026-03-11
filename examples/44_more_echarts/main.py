import os
from sivo import Sivo, ProjectConfig

SVG_FILE = os.path.join(os.path.dirname(__file__), 'bg.svg')

with open(SVG_FILE, 'w') as f:
    f.write("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
    <rect id="rect1" x="0" y="0" width="400" height="300" fill="#f0f0f0"/>
    <rect id="rect2" x="400" y="0" width="400" height="300" fill="#e0e0e0"/>
    <rect id="rect3" x="0" y="300" width="400" height="300" fill="#d0d0d0"/>
    <rect id="rect4" x="400" y="300" width="400" height="300" fill="#c0c0c0"/>
    <text x="200" y="150" text-anchor="middle">Click for Effect Scatter</text>
    <text x="600" y="150" text-anchor="middle">Click for Lines</text>
    <text x="200" y="450" text-anchor="middle">Click for Funnel</text>
    <text x="600" y="450" text-anchor="middle">Click for Tree</text>
</svg>""")

config = ProjectConfig(
    svg_file=SVG_FILE,
    title="More ECharts Types Demo",
    subtitle="Demonstrating effectScatter, lines, funnel, and tree",
    theme="light"
)

sivo_app = Sivo.from_config(config)

# 1. Effect Scatter
sivo_app.map_effect_scatter_chart(
    element_id="rect1",
    title="Effect Scatter",
    data=[
        [10.0, 8.04],
        [8.0, 6.95],
        [13.0, 7.58],
        [9.0, 8.81],
        [11.0, 8.33],
        [14.0, 9.96],
        [6.0, 7.24],
        [4.0, 4.26],
        [12.0, 10.84],
        [7.0, 4.82],
        [5.0, 5.68]
    ],
    color="#ff3333",
    panel_position="right"
)

# 2. Lines
sivo_app.map_lines_chart(
    element_id="rect2",
    title="Lines",
    data=[
        {"coords": [[0, 0], [10, 10]]},
        {"coords": [[10, 10], [20, 5]]},
        {"coords": [[20, 5], [30, 15]]}
    ],
    color="#3399ff",
    panel_position="right"
)

# 3. Funnel
sivo_app.map_funnel_chart(
    element_id="rect3",
    title="Sales Funnel",
    data=[
        {"value": 100, "name": "Impressions"},
        {"value": 80, "name": "Clicks"},
        {"value": 60, "name": "Visits"},
        {"value": 40, "name": "Inquiries"},
        {"value": 20, "name": "Orders"}
    ],
    panel_position="right"
)

# 4. Tree
tree_data = [
    {
        "name": "CEO",
        "children": [
            {
                "name": "VP Eng",
                "children": [{"name": "Eng 1"}, {"name": "Eng 2"}]
            },
            {
                "name": "VP Sales",
                "children": [{"name": "Sales 1"}]
            }
        ]
    }
]

sivo_app.map_tree_chart(
    element_id="rect4",
    title="Organization Tree",
    data=tree_data,
    panel_position="right"
)

output_path = os.path.join(os.path.dirname(__file__), 'output.html')
sivo_app.to_html(output_path)
print(f"Generated {output_path}")
