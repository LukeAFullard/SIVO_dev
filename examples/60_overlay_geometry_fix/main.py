from sivo import Sivo
from sivo.core.config import ProjectConfig

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
    <rect width="800" height="600" fill="#f0f0f0" />
    <rect id="box-1" x="100" y="100" width="100" height="100" fill="#ff9999" />
    <rect id="box-2" x="350" y="250" width="100" height="100" fill="#99ff99" />
    <rect id="box-3" x="600" y="400" width="100" height="100" fill="#9999ff" />
</svg>"""

with open("examples/60_overlay_geometry_fix/test.svg", "w") as f:
    f.write(svg_content)

app = Sivo.from_svg("examples/60_overlay_geometry_fix/test.svg")

dot_html = '<div style="width: 20px; height: 20px; background: black; border-radius: 50%; color: white; display:flex; align-items:center; justify-content:center; font-size: 10px;">X</div>'

app.add_overlay("box-1", dot_html, scale_with_zoom=True)
app.add_overlay("box-2", dot_html, scale_with_zoom=True)
app.add_overlay("box-3", dot_html, scale_with_zoom=True)

app.to_html("examples/60_overlay_geometry_fix/index.html")
print("Saved to examples/60_overlay_geometry_fix/index.html")
