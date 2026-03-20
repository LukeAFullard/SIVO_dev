from sivo import Sivo

svg_content = """<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="skyNight" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#000022"/>
      <stop offset="100%" stop-color="#1A1A40"/>
    </linearGradient>
    <linearGradient id="waterGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#003366"/>
      <stop offset="100%" stop-color="#001133"/>
    </linearGradient>
    <radialGradient id="moonGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Night Sky -->
  <rect width="800" height="300" fill="url(#skyNight)"/>

  <!-- Moon -->
  <circle cx="150" cy="100" r="80" fill="url(#moonGlow)"/>
  <circle cx="150" cy="100" r="40" fill="#F0F8FF"/>

  <!-- Stars -->
  <circle cx="300" cy="50" r="2" fill="#FFFFFF" opacity="0.6"/>
  <circle cx="500" cy="150" r="1.5" fill="#FFFFFF" opacity="0.8"/>
  <circle cx="700" cy="80" r="2.5" fill="#FFFFFF" opacity="0.5"/>
  <circle cx="450" cy="220" r="1" fill="#FFFFFF" opacity="0.4"/>
  <circle cx="600" cy="30" r="2" fill="#FFFFFF" opacity="0.7"/>

  <!-- Water Surface -->
  <rect x="0" y="300" width="800" height="300" fill="url(#waterGrad)"/>

  <!-- Moon Reflection -->
  <rect x="110" y="300" width="80" height="150" fill="url(#moonGlow)" opacity="0.2"/>
  <path d="M120,320 L180,320 M130,340 L170,340 M115,360 L185,360 M125,380 L175,380 M135,400 L165,400" stroke="#FFFFFF" stroke-width="2" opacity="0.3"/>
</svg>"""

app = Sivo.from_string(
    svg_content,
    ambient_effect="water",
    ambient_speed=0.5,
    title="Ambient Water Effect",
    subtitle="With speed multiplier 0.5 (Night River)",
    transparent_template_lines=True
)

app.to_html("examples/49_ambient_effects/ambient_water.html")
print("Saved ambient_water.html")
