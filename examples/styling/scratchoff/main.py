import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    # The default panel position is 'none', which is fine here as we are not
    # mapping any side panels or media overlays that require a panel.
    sivo_app = Sivo.from_svg(svg_path, title="Scratch-off Map Reveal", subtitle="Use your mouse to reveal the map!")

    sivo_app.map("sun", tooltip="The Sun!")

    # Enable a gray scratch-off layer with a 50px brush
    sivo_app.enable_scratchoff(color="#1e293b", brush_size=50)

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
