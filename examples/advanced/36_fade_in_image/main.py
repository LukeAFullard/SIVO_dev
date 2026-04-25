from sivo import Sivo

svg_string = """
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="800" height="600" fill="#f0f0f0" />
  <image id="my_image" x="200" y="150" width="400" height="300" href="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" />
</svg>
"""

def main():
    app = Sivo.from_string(svg_string, render_mode="svg")

    # Map the image to fade in
    app.map(
        "my_image",
        fade_in=True,
        fade_start_time_ms=1000,
        fade_duration_ms=3000
    )

    app.to_html("examples/advanced/36_fade_in_image/index.html")

if __name__ == "__main__":
    main()
