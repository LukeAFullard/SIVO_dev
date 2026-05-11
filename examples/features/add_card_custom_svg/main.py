from sivo.core.sivo import Sivo
import os

def main():
    svg_string = """<svg viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
      <rect id="background" width="500" height="500" fill="#f0f0f0" />
    </svg>"""

    sivo_app = Sivo.from_string(svg_string)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    star_svg_path = os.path.join(current_dir, "star.svg")

    sivo_app.add_card(
        element_id="background",
        title="Star",
        value="100%",
        subtitle="A custom SVG shape",
        custom_svg=star_svg_path
    )

    output_path = os.path.join(current_dir, "output.html")
    sivo_app.to_html(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
