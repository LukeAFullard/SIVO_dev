from sivo import Sivo

svg_content = '<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg"><rect width="800" height="600" fill="#228B22"/></svg>'

app = Sivo.from_string(
    svg_content,
    ambient_effect="plants",
    ambient_speed=2.0,
    title="Ambient Plants Effect",
    subtitle="With speed multiplier 2.0"
)

app.to_html("examples/49_ambient_effects/ambient_plants.html")
print("Saved ambient_plants.html")
