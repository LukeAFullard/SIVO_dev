import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # Click the shape to play a sound (e.g., pronunciation, ambient noise)
    # Using a free sample URL
    sivo_app.map(
        element_id="play_button",
        tooltip="Click to hear a sound",
        audio="https://actions.google.com/sounds/v1/alarms/beep_short.ogg",
        html="<h2>Audio Playback Example</h2><p>You clicked the button and should hear a short beep.</p>",
        panel_position="right",
        hover_color="#32a852",
        glow=True
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported audio playback interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
