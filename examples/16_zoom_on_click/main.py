import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # 1. Map elements to zoom on click
    sivo_app.map(
        element_id="TX",
        tooltip="Texas Region",
        html="<h3>Texas Region</h3><p>Zoomed in automatically to Texas.</p>",
        zoom_on_click=True,
        zoom_level=3.5
    )

    sivo_app.map(
        element_id="CA",
        tooltip="California Region",
        html="<h3>California Region</h3><p>Zoomed in automatically to California.</p>",
        zoom_on_click=True,
        zoom_level=3.5
    )

    # 3. Export to HTML
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported Zoom Action HTML to {output_path}")

if __name__ == "__main__":
    main()
