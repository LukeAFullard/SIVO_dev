import os
from sivo import Sivo

def main():
    svg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "basic", "hello_world", "sample.svg"))

    sivo_app = Sivo.from_svg(svg_path, title="Audio Guided Tour", default_panel_position="none")

    sivo_app.map("sun", html="Building A")
    sivo_app.map("house", html="Building B")
    sivo_app.map("river", html="Building C")

    # Define tour steps with short royalty-free sample audio URLs (like a voiceover)
    sivo_app.bind_tour([
        {
            "content": "<h3>Welcome to the Audio Tour!</h3><p>Make sure your volume is turned up.</p>",
            "audio_url": "https://actions.google.com/sounds/v1/water/rain_drips_on_tin_roof.ogg", # Sample ambient/short sound
            "zoom_to": "mountain1",
            "zoom_level": 1.2
        },
        {
            "content": "<h3>Building A</h3><p>Notice the modern architecture.</p>",
            "audio_url": "https://actions.google.com/sounds/v1/alarms/beep_short.ogg",
            "zoom_to": "sun",
            "show_tooltips": ["sun"],
            "zoom_level": 2.5
        },
        {
            "content": "<h3>Building B</h3><p>Our engineering center.</p>",
            "audio_url": "https://actions.google.com/sounds/v1/alarms/digital_watch_alarm_long.ogg",
            "zoom_to": "house",
            "show_tooltips": ["house"],
            "zoom_level": 3.0
        }
    ])

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
