import os
from sivo import Sivo

# A simple map representing a layout
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
    <circle id="regionA" cx="30" cy="50" r="20" fill="#e0f2fe" stroke="#0ea5e9" stroke-width="2"/>
    <circle id="regionB" cx="70" cy="50" r="20" fill="#e0f2fe" stroke="#0ea5e9" stroke-width="2"/>
</svg>"""

app = Sivo.from_string(svg_content)

app.map("regionA", tooltip="Region A")
app.map("regionB", tooltip="Region B")

# Add native ECharts graphic components over the visualization
# This adds a title text in the center and a watermark image
app.add_graphic({
    "type": "group",
    "left": "center",
    "top": "20%",
    "children": [
        {
            "type": "rect",
            "z": 100,
            "left": "center",
            "top": "middle",
            "shape": {
                "width": 250,
                "height": 50,
                "r": [5, 5, 5, 5]
            },
            "style": {
                "fill": "rgba(255,255,255,0.8)",
                "stroke": "#cbd5e1",
                "lineWidth": 1
            }
        },
        {
            "type": "text",
            "z": 100,
            "left": "center",
            "top": "middle",
            "style": {
                "fill": "#1e293b",
                "text": "Native ECharts Graphic Element",
                "font": "bold 16px sans-serif"
            }
        }
    ]
})

# Add a floating watermark graphic
app.add_graphic({
    "type": "text",
    "right": 20,
    "bottom": 20,
    "z": 100,
    "style": {
        "fill": "#94a3b8",
        "text": "SIVO x ECharts",
        "font": "italic 14px sans-serif"
    }
})

output_path = os.path.join(os.path.dirname(__file__), "output.html")
app.to_html(output_path)
print(f"Generated {output_path}")
