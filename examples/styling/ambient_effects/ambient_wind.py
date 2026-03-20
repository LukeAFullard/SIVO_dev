from sivo import Sivo

svg_content = """<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#87CEEB"/>
      <stop offset="100%" stop-color="#E0F6FF"/>
    </linearGradient>
    <linearGradient id="hillGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#32CD32"/>
      <stop offset="100%" stop-color="#228B22"/>
    </linearGradient>
  </defs>

  <rect width="800" height="600" fill="url(#skyGrad)"/>
  <circle cx="650" cy="150" r="60" fill="#FFD700" opacity="0.8"/>

  <path d="M-50,650 Q150,450 400,550 T850,550 L850,650 Z" fill="url(#hillGrad)" opacity="0.8"/>
  <path d="M-50,650 Q250,500 500,580 T850,500 L850,650 Z" fill="url(#hillGrad)"/>
</svg>"""

app = Sivo.from_string(
    svg_content,
    ambient_effect="wind",
    ambient_speed=3.0,
    title="Ambient Wind Effect",
    subtitle="With speed multiplier 3.0",
    transparent_template_lines=True
)

app.to_html("examples/49_ambient_effects/ambient_wind.html")
print("Saved ambient_wind.html")
