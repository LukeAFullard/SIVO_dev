import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # 1. Map typical interactions
    sivo_app.map(
        element_id="sun",
        tooltip="A pulsing sun",
        animation="pulse",
        color="orange"
    )

    sivo_app.map(
        element_id="house",
        tooltip="Fading house",
        animation="fade",
        color="purple"
    )

    # 2. Add dynamic markers exactly centered on SVG elements
    sivo_app.add_marker(
        element_id="mountain1",
        icon="⛰️",
        label="Peak 1",
        offset_y=-30
    )

    sivo_app.add_marker(
        element_id="mountain2",
        icon="⛰️",
        label="Peak 2",
        offset_y=-20
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
