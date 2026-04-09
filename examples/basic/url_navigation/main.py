import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # Map interactions to external URLs
    sivo_app.map(
        element_id="sun",
        tooltip="Click to search about the Sun",
        url="https://en.wikipedia.org/wiki/Sun",
        hover_color="yellow",
        glow=True
    )

    sivo_app.map(
        element_id="mountain1",
        tooltip="Click to search about Mountains",
        url="https://en.wikipedia.org/wiki/Mountain",
        hover_color="#c0c0c0"
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
