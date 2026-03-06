import os
from sivo import Sivo

def main():
    # 1. Initialize Sivo from an SVG file
    svg_path = "sample.svg"

    # Check if we are running from root or examples dir
    if not os.path.exists(svg_path):
        svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # 2. Map interactions
    sivo_app.map(
        element_id="sun",
        tooltip="The Sun",
        html="<h3>The Sun</h3><p>It is very bright and hot.</p>",
        color="gold",
        hover_color="yellow",
        glow=True
    )

    sivo_app.map(
        element_id="mountain1",
        tooltip="Mountain 1",
        color="#a0a0a0",
        hover_color="#c0c0c0"
    )

    sivo_app.map(
        element_id="house",
        tooltip="A small house",
        color="brown",
        hover_color="#a52a2a"
    )

    # 3. Export to HTML
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
