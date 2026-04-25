from sivo import Sivo, SivoDashboard

svg_string = """
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <rect id="my_box" x="100" y="100" width="600" height="400" fill="#f0f0f0" stroke="#ccc" />
</svg>
"""

def main():
    app = Sivo.from_string(svg_string, render_mode="svg")

    # Map the box to fade in immediately
    app.map("my_box", fade_in=True, fade_duration_ms=2000, color="#f0f0f0")

    # Add scalable text to the box, fading in after a 3 second delay
    app.add_scalable_text(
        "my_box",
        "Fading Text Overlay",
        font_size="15%",
        align="center",
        vertical_align="middle",
        fade_in=True,
        fade_start_time_ms=3000,
        fade_duration_ms=2000
    )

    dashboard = SivoDashboard(title="Fade Text Dashboard", theme="light")
    dashboard.add_sivo_block("main_app", app)

    dashboard.to_html("examples/advanced/35_fade_in_text/dashboard.html")

if __name__ == "__main__":
    main()
