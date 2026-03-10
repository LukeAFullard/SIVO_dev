import os
from sivo import Sivo

svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
  <rect id="section1" x="100" y="100" width="200" height="200" fill="#f0f0f0" stroke="#ccc"/>
  <text x="200" y="200" font-size="24" text-anchor="middle">Data Center</text>

  <circle id="section2" cx="700" cy="200" r="100" fill="#f0f0f0" stroke="#ccc"/>
  <text x="700" y="200" font-size="24" text-anchor="middle">Logistics</text>

  <path id="section3" d="M 300 400 L 700 400 L 500 550 Z" fill="#f0f0f0" stroke="#ccc"/>
  <text x="500" y="470" font-size="24" text-anchor="middle">HQ</text>
</svg>
"""

# Initialize Sivo App
sivo_app = Sivo.from_string(svg_content)

# We use generic external audio links for demonstration purposes
audio_beep_1 = "https://actions.google.com/sounds/v1/alarms/beep_short.ogg"
audio_beep_2 = "https://actions.google.com/sounds/v1/alarms/digital_watch_alarm_long.ogg"

# Define Scrollytelling narrative with audio
steps = [
    {
        "content": "<h1>1. The Global Network</h1><p>Our operations span across three main hubs. Scroll down to trigger audio events as you explore.</p>",
        "colors": {
            "section1": "#f0f0f0",
            "section2": "#f0f0f0",
            "section3": "#f0f0f0"
        }
    },
    {
        "content": "<h2>2. The Data Center</h2><p>This is where all our processing happens. (Playing audio beep 1)</p>",
        "zoom_to": "section1",
        "zoom_level": 2.5,
        "audio_url": audio_beep_1,
        "colors": {
            "section1": "#3b82f6",  # Highlight blue
            "section2": "#f0f0f0",
            "section3": "#f0f0f0"
        },
        "show_tooltips": ["section1"]
    },
    {
        "content": "<h2>3. The Logistics Hub</h2><p>Physical goods are routed through this circular zone. (Playing audio beep 2)</p>",
        "zoom_to": "section2",
        "zoom_level": 2.5,
        "audio_url": audio_beep_2,
        "colors": {
            "section1": "#f0f0f0",
            "section2": "#10b981",  # Highlight green
            "section3": "#f0f0f0"
        },
        "show_tooltips": ["section2"]
    },
    {
        "content": "<h2>4. Headquarters</h2><p>The central triangle coordinates both data and physical routing.</p>",
        "zoom_to": "section3",
        "zoom_level": 2.0,
        "colors": {
            "section1": "#f0f0f0",
            "section2": "#f0f0f0",
            "section3": "#8b5cf6"  # Highlight purple
        },
        "show_tooltips": ["section3"]
    }
]

sivo_app.map("section1", tooltip="Data Center (Active)")
sivo_app.map("section2", tooltip="Logistics Hub (Active)")
sivo_app.map("section3", tooltip="Headquarters (Active)")

# Bind the scrollytelling steps
sivo_app.bind_scrollytelling(steps)

output_path = os.path.join(os.path.dirname(__file__), "scrollytelling_audio.html")
sivo_app.to_html(output_path)
print(f"Generated {output_path}")
