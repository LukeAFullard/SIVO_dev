import os
from sivo import Sivo

def main():
    # A simple SVG
    svg_str = """
    <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <rect id="block1" x="10" y="10" width="30" height="30" fill="blue" />
        <rect id="block2" x="60" y="10" width="30" height="30" fill="green" />
    </svg>
    """

    app = Sivo.from_string(
        svg_str,
        default_panel_position="overlay",
        panel_width="90%",
        panel_height="90%",
    )

    app.map(
        "block1",
        html="<h1>Block 1</h1><p>This panel is displayed as an overlay spanning 90% of the screen.</p>"
    )

    app.map(
        "block2",
        html="<h1>Block 2</h1><p>Here is another block opening the overlay.</p>"
    )

    output_path = os.path.join(os.path.dirname(__file__), "overlay_sidebar_example.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(app.to_html())

    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
