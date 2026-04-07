# 01 Hello World

This example demonstrates the basic usage of SIVO. It loads an SVG file and maps simple interactions (tooltips, colors, hover colors, and glow) to specific elements in the SVG.

### Key Code

```python
sivo_app = Sivo.from_svg(svg_path, enable_search=True)

# Map interactions
sivo_app.map(
    element_id="sun",
    tooltip="The Sun",
    html="<h3>The Sun</h3><p>It is very bright and hot.</p>",
    color="gold",
    hover_color="yellow",
    glow=True
)
```
