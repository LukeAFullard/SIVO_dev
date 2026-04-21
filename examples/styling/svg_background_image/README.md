# SVG Background Image

This example demonstrates how to set a background image that is integrated directly into the SVG map elements using the `add_svg_background_image` method in SIVO.

This is different from adding a general background image to the container using `add_background_image`. An SVG background image becomes a part of the interactive map itself.

## Features Showcased
- Loading a `Sivo` map with `Sivo.from_svg()`.
- Adding an SVG background image with an external URL.
- Setting the opacity and grayscale modes of the SVG background image.
- Specifying the `insert_after` position to ensure the image appears behind map features but above the main structural backgrounds (e.g., `<rect id="background">`).
- Combining with a subtle overall container background image.
- Mapping standard interactions to specific parts of the map (e.g. highlighting "US" on hover).

## Code Snippets

```python
import sys
sys.path.insert(0, 'src')
from sivo.core.sivo import Sivo
import os

def main():
    # Load map from a local SVG file
    sample_svg = os.path.join(os.path.dirname(__file__), "sample.svg")
    app = Sivo.from_svg(sample_svg, theme="dark", lock_zoom_out=True)

    # Set some infographic metadata
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

    # Also add a general background image to the parent container
    app.add_background_image(
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1920&q=80",
        opacity=0.1
    )

    try:
        # Standard mapping
        app.map("US", tooltip="United States", color="rgba(56, 189, 248, 0.7)", hover_color="#38bdf8")
    except ValueError:
        pass

    # Save to HTML
    output_path = os.path.join(os.path.dirname(__file__), "index.html")
    app.to_html(output_path)

if __name__ == "__main__":
    main()
```
