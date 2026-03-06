import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # Drill down logic - click on the house to load another SVG.
    # We will use floor1.svg to simulate going inside the house.
    sivo_app.map(
        element_id="house",
        tooltip="Click to enter the house",
        drill_to="floor1.svg",
        hover_color="orange",
        glow=True
    )

    # We can also map something to sun, but just normal tooltip
    sivo_app.map(
        element_id="sun",
        tooltip="The Sun",
        color="gold"
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
