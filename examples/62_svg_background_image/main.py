import sys
sys.path.insert(0, 'src')
from sivo.core.sivo import Sivo
import os

def main():
    # Use the sample SVG map
    sample_svg = "examples/sample.svg"

    app = Sivo.from_svg(sample_svg, theme="dark", lock_zoom_out=True)

    app.infographic.title = "Global Expeditions"
    app.infographic.subtitle = "Using an SVG Background Image to enhance the map canvas."
    app.infographic.attribution = "Photo by Andrew Neel on Unsplash"

    unsplash_url = "https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&w=1920&q=80"

    # Add a grayscale background image to the SVG at 40% opacity.
    # We use insert_after="background" because sample.svg has a solid `<rect id="background">`
    # that would otherwise block an image placed at the absolute root index 0.
    app.add_svg_background_image(
        url=unsplash_url,
        opacity=0.4,
        grayscale=True,
        insert_after="background"
    )

    app.add_background_image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1920&q=80", opacity=0.1)

    try:
        app.map("US", tooltip="United States", color="rgba(56, 189, 248, 0.7)", hover_color="#38bdf8")
    except ValueError:
        pass

    output_path = os.path.join(os.path.dirname(__file__), "index.html")
    app.to_html(output_path)
    print(f"Generated example at {output_path}")

if __name__ == "__main__":
    main()
