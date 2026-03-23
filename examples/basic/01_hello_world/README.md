# Basic: Hello World

This example demonstrates the most basic usage of the Sivo library. It shows how to load an SVG file and make specific elements interactive using their IDs.

## What is being tested/demonstrated
* Loading an SVG file using `Sivo.from_svg()`.
* Enabling the built-in search functionality.
* Mapping interactivity (tooltips, colors, hover effects, and HTML content) to specific SVG elements via `sivo_app.map()`.
* Exporting the resulting interactive application to a standalone HTML file.

## Key Code

```python
# 1. Initialize Sivo from an SVG file
sivo_app = Sivo.from_svg(svg_path, enable_search=True)

# 2. Map interactions
sivo_app.map(
    element_id="sun",
    tooltip="The Sun",
    html="<h3>The Sun</h3><p>It is very bright and hot.</p>",
    color="gold",
    hover_color="yellow",
    glow=True
)
```
