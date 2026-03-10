import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "..", "01_hello_world", "sample.svg")

    sivo_app = Sivo.from_svg(svg_path, title="Proportional Symbol Map", subtitle="Size represents budget")

    # Map the buildings to generate bounding boxes
    sivo_app.map("sun", tooltip="Building A (Budget: $500k)")
    sivo_app.map("house", tooltip="Building B (Budget: $250k)")
    sivo_app.map("river", tooltip="Building C (Budget: $1.2M)")

    # Apply proportional symbols
    sivo_app.apply_proportional_symbols(
        data_map={
            "sun": 500,
            "house": 250,
            "river": 1200
        },
        min_size=10,
        max_size=50,
        color="rgba(56, 189, 248, 0.7)" # Light blue semi-transparent
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()