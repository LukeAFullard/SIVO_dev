import os
import sys

# Add the src directory to the path so we can import sivo locally
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src')))

from sivo import Sivo

def main():
    # A simple SVG map with two regions
    svg_string = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
        <rect id="regionA" x="10" y="10" width="80" height="80" fill="#cbd5e1" stroke="#334155" stroke-width="2" />
        <rect id="regionB" x="110" y="10" width="80" height="80" fill="#cbd5e1" stroke="#334155" stroke-width="2" />
    </svg>
    """

    # We tell SIVO to establish keyboard navigation order via presentation_order
    app = Sivo.from_string(
        svg_string,
        presentation_order=["regionA", "regionB"],
        default_panel_position="right",
        enable_a11y=True
    )

    # Map the first region with accessible attributes
    app.map(
        "regionA",
        tooltip="Region A",
        html="<h2>Region A Information</h2><p>This is accessible data for the first region.</p>",
        aria_label="First Region, press Enter to open details",
        role="button",
        tabindex="0"
    )

    # Map the second region with accessible attributes
    app.map(
        "regionB",
        tooltip="Region B",
        html="<h2>Region B Information</h2><p>This is accessible data for the second region.</p>",
        aria_label="Second Region, press Enter to open details",
        role="button",
        tabindex="0"
    )

    output_path = os.path.join(os.path.dirname(__file__), "a11y_example.html")
    app.to_html(output_path)
    print(f"Generated A11y example at {output_path}")

if __name__ == "__main__":
    main()
