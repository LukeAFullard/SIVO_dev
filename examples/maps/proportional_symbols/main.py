import os
from sivo import Sivo

def main():
    svg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "basic", "hello_world", "sample.svg"))

    sivo_app = Sivo.from_svg(
        svg_path,
        title="Proportional Symbol Map",
        subtitle="Size represents budget",
        default_panel_position="right"
    )

    # Map the buildings to generate bounding boxes
    # Use 'html' instead of deprecated 'tooltip' parameter
    sivo_app.map("sun", html="Building A (Budget: $500k)")
    sivo_app.map("house", html="Building B (Budget: $250k)")
    sivo_app.map("river", html="Building C (Budget: $1.2M)")

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
