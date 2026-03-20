import os
from sivo import Sivo

svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
    <rect width="100%" height="100%" fill="#ffffff" />
    <g id="shapes">
        <rect id="rect1" x="50" y="50" width="80" height="80" fill="#3498db" />
        <circle id="circ1" cx="200" cy="90" r="40" fill="#e74c3c" />
        <polygon id="poly1" points="300,50 340,130 260,130" fill="#2ecc71" />

        <rect id="rect2" x="50" y="170" width="80" height="80" fill="#9b59b6" />
        <circle id="circ2" cx="200" cy="210" r="40" fill="#f1c40f" />
        <polygon id="poly2" points="300,170 340,250 260,250" fill="#e67e22" />
    </g>
</svg>
"""

def main():
    print("Building Fade Unselected Example...")

    # Initialize Sivo with fade_unselected=True
    sivo_app = Sivo.from_string(svg_content, fade_unselected=True)

    # Map a few elements
    sivo_app.map(
        element_id="rect1",
        tooltip="Blue Rectangle",
        html="<h3>Blue Rectangle</h3><p>Notice how all other shapes fade out when you click me.</p>",
        hover_color="#2980b9"
    )

    sivo_app.map(
        element_id="circ1",
        tooltip="Red Circle",
        html="<h3>Red Circle</h3><p>Click the background canvas to deselect and close this panel.</p>",
        hover_color="#c0392b"
    )

    sivo_app.map(
        element_id="poly2",
        tooltip="Orange Triangle",
        html="<h3>Orange Triangle</h3><p>Fading works across all mapped objects automatically.</p>",
        hover_color="#d35400"
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)

    print(f"Map successfully generated at: {output_path}")

if __name__ == "__main__":
    main()
