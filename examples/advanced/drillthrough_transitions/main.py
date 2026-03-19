import sys
import os

# Add the src directory to the path so we can import sivo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def create_drillthrough_example():
    # Create two separate SVGs to represent distinct HTML pages

    # Page 1: Overview
    svg_page1 = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
        <rect width="800" height="600" fill="#fee2e2" />
        <text x="400" y="200" font-family="sans-serif" font-size="48" font-weight="bold" fill="#991b1b" text-anchor="middle">Page 1: Multi-file</text>

        <g id="btn_next" cursor="pointer">
            <rect x="300" y="300" width="200" height="60" rx="8" fill="#ef4444" />
            <text x="400" y="338" font-family="sans-serif" font-size="24" fill="white" text-anchor="middle">Go to Page 2</text>
        </g>
    </svg>
    """

    # Page 2: Details
    svg_page2 = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
        <rect width="800" height="600" fill="#fef9c3" />
        <text x="400" y="200" font-family="sans-serif" font-size="48" font-weight="bold" fill="#854d0e" text-anchor="middle">Page 2: Details</text>

        <g id="btn_back" cursor="pointer">
            <rect x="300" y="300" width="200" height="60" rx="8" fill="#eab308" />
            <text x="400" y="338" font-family="sans-serif" font-size="24" fill="white" text-anchor="middle">Back to Page 1</text>
        </g>
    </svg>
    """

    app1 = Sivo.from_string(svg_page1, disable_panel=True, disable_zoom_controls=True)
    app2 = Sivo.from_string(svg_page2, disable_panel=True, disable_zoom_controls=True)

    # Link them using drill_through (which loads a new URL) rather than drill_to (which swaps views in a single page app)
    # We use a relative URL here assuming both HTML files are in the same folder.
    app1.map("btn_next", drill_through="page2.html", drill_transition="flip", hover_color="#b91c1c")
    app2.map("btn_back", drill_through="page1.html", drill_transition="slide-left", hover_color="#a16207")

    out_dir = os.path.dirname(__file__)

    app1.to_html(output_path=os.path.join(out_dir, "page1.html"))
    app2.to_html(output_path=os.path.join(out_dir, "page2.html"))

    print(f"Generated page1.html and page2.html in {out_dir}")
    print("Open page1.html in your browser and click the button to see the multi-file transition!")

if __name__ == "__main__":
    create_drillthrough_example()
