from sivo import Sivo

svg_content = '<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg"><rect width="800" height="600" fill="#87CEEB"/></svg>'

app = Sivo.from_string(
    svg_content,
    ambient_effect="wind",
    ambient_speed=3.0,
    title="Ambient Wind Effect",
    subtitle="With speed multiplier 3.0"
)

app.to_html("examples/49_ambient_effects/ambient_wind.html")
print("Saved ambient_wind.html")
