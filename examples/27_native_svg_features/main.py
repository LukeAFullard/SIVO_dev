import os
from sivo import Sivo

def main():
    # 1. Initialize Sivo from an SVG file, enabling native SVG render mode
    # This mode injects a synchronized SVG overlay to perform advanced manipulations.
    sivo_app = Sivo.from_svg(
        filepath=os.path.join(os.path.dirname(__file__), "shapes.svg"),
        render_mode="svg",
        default_panel_position="right"
    )

    # 2. Map a shape to morph into a different path
    # We take the square 'morphing_shape' and instruct it to transition into a circle path over 2 seconds.
    # The 'morph_to_path' uses standard SVG path commands.
    circle_path_data = "M 50 10 A 40 40 0 1 0 50 90 A 40 40 0 1 0 50 10"

    sivo_app.map(
        element_id="morphing_shape",
        tooltip="This shape morphs on load!",
        morph_to_path=circle_path_data,
        morph_duration_ms=2000,
        filter="5" # Applies a simple drop shadow filter
    )

    # 3. Add text along a curved path
    # We bind a text label to the 'text_curve' path, leveraging native SVG <textPath> elements.
    sivo_app.add_path_label(
        element_id="text_curve",
        text="Hello, text on a path!",
        font_size=12,
        color="#e74c3c"
    )

    # 4. Export to interactive HTML
    output_path = os.path.join(os.path.dirname(__file__), "interactive_shapes.html")
    sivo_app.to_html(output_path)
    print(f"Interactive infographic exported to: {output_path}")

if __name__ == "__main__":
    main()