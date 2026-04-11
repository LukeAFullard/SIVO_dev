# Mobile Pinch Zoom Example

This example demonstrates how SIVO handles touch interactions and zoom capabilities on mobile devices or smaller screens. While SIVO provides interactive capabilities out of the box, this specific test validates the mobile pinch-to-zoom feature on an SVG canvas, ensuring it can be zoomed natively via gesture.

## What is being tested

*   **Pinch-to-zoom functionality:** Checks if mobile gestures correctly scale the underlying SVG map/graphic.
*   **Overlay panel position:** Uses `default_panel_position="overlay"` so that interactive html text displays over the visualization.

## Setup & Run

To generate the example HTML file, run:

```bash
PYTHONPATH=src python examples/advanced/mobile_pinch_zoom/generate.py
```

This generates an `index.html` file that you can open in a web browser. To test the pinch zoom, you can either view it on a mobile device or use your browser's developer tools to emulate a mobile device and simulate pinch-to-zoom gestures.

## Relevant Code

The application is initialized using `Sivo.from_string()` and includes mapped HTML content:

```python
from sivo import Sivo

# Initialize Sivo with an SVG and set the default panel position to overlay
app = Sivo.from_string(
    '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect id="box" x="10" y="10" width="80" height="80" fill="lightblue"/></svg>',
    default_panel_position="overlay"
)

# Map HTML content to the box element
app.map("box", html="<h2>Pinch to zoom!</h2><p>Try it on mobile.</p>", hover_color="lightgreen")

# Output to HTML
app.to_html("examples/advanced/mobile_pinch_zoom/index.html")
```
