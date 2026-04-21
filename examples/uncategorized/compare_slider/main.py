import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    # Set default_panel_position="left" is already correct from memory
    sivo_app = Sivo.from_svg(svg_path, title="Image Comparison Slider", default_panel_position="left")

    # For compare to open in a panel, we must either rely on default_panel_position="left" or explicit panel_position
    sivo_app.map(
        "sun",
        tooltip="Main Admin",
        compare={
            "before_image": "https://picsum.photos/id/10/800/600",
            "after_image": "https://picsum.photos/id/11/800/600",
            "label_before": "1990",
            "label_after": "2024"
        },
        html="<p>Slide to compare the old and new building designs.</p>",
        panel_position="left"
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
