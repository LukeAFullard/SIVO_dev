from sivo import Sivo

svg_content = '<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg"><rect width="800" height="600" fill="#000033"/></svg>'

app = Sivo.from_string(
    svg_content,
    ambient_effect="water",
    ambient_speed=0.5,
    title="Ambient Water Effect",
    subtitle="With speed multiplier 0.5"
)

app.to_html("examples/49_ambient_effects/ambient_water.html")
print("Saved ambient_water.html")
