from src.sivo.core.sivo import Sivo

svg = """<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect id="rect1" x="10" y="10" width="80" height="80" fill="gray"/>
  <rect id="rect2" x="110" y="10" width="80" height="80" fill="gray"/>
</svg>"""

sivo = Sivo.from_string(svg)
data = {
    "2020": {"rect1": {"val": 10}, "rect2": {"val": 20}},
    "2021": {"rect1": {"val": 30}, "rect2": {"val": 40}}
}
sivo.bind_timeline(data, "val", ["#ff0000", "#0000ff"], 0, 50, show_play_btn=False, control_position="right", loop=False)

sivo.to_html("test_timeline_output.html")
print("HTML generated")
