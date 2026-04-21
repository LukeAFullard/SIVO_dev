# SIVO Example Infographic

This example demonstrates how to build a simple interactive infographic using SIVO.

## What is being shown
- Loading a static SVG file (`sample.svg`) using `Sivo.from_svg()`.
- Applying multiple interactive layers by mapping different `id` elements within the SVG using `sivo_app.map()`.
- Adding rich HTML content that renders in side panels upon clicking an element.
- Demonstrating URL navigation when clicking an element (e.g., `url="https://en.wikipedia.org/wiki/Mountain"`).
- Setting custom colors and hover effects for SVG elements.

## Key Code Snippets

```python
# Map an element to display custom HTML content and open a URL
sivo_app.map(
    "mountain1",
    tooltip="Left Mountain",
    html="<h3>Left Mountain</h3><p>A tall, majestic mountain.</p>",
    color="#8c8c8c",
    url="https://en.wikipedia.org/wiki/Mountain"
)
```

## Running the example
To run the example and generate the HTML output:
```bash
python example_infographic.py
```
Open the generated `output.html` in your browser. Note: the `drill_to` action on the "house" element requires `interior.svg` and running a local HTTP server to function correctly, though this example primarily demonstrates syntax.
