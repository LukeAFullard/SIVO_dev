import sys
import os

# Add src to the path so we can import sivo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), 'sample.svg')
    output_path = os.path.join(os.path.dirname(__file__), 'output.html')

    # Initialize Sivo with the sample SVG
    sivo_app = Sivo.from_svg(svg_path)

    # Map interactions to specific SVG elements
    sivo_app.map(
        "sun",
        tooltip="The Sun",
        html="<h3>The Sun</h3><p>The star at the center of the Solar System.</p>",
        color="#ffcc00",
        hover_color="#ffa500"
    )

    sivo_app.map(
        "mountain1",
        tooltip="Left Mountain",
        html="<h3>Left Mountain</h3><p>A tall, majestic mountain.</p>",
        color="#8c8c8c",
        url="https://en.wikipedia.org/wiki/Mountain"
    )

    sivo_app.map(
        "house",
        tooltip="A small house",
        html="<h3>Cozy House</h3><p>This is where someone lives.</p>",
        color="#a52a2a",
        drill_to="interior.svg"
    )

    sivo_app.map(
        "river",
        tooltip="Blue River",
        html="<h3>River</h3><p>A flowing body of water.</p>",
        color="#0000ff"
    )

    # Generate the interactive HTML
    print(f"Generating ECharts HTML to {output_path}...")
    sivo_app.to_html(output_path=output_path)
    print("Done!")

if __name__ == "__main__":
    main()
