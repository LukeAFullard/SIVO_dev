# Basic: URL Navigation

This example demonstrates how to configure SVG elements in Sivo to act as hyperlinks, navigating users to external URLs upon interaction.

## What is being tested/demonstrated
* Loading an SVG file using `Sivo.from_svg()`.
* Mapping interactions on specific elements to open external web links using the `url` parameter.
* Styling hover states to indicate interactiveness.

## Key Code

```python
# Map interaction to external URL
sivo_app.map(
    element_id="sun",
    tooltip="Click to search about the Sun",
    url="https://en.wikipedia.org/wiki/Sun",
    hover_color="yellow",
    glow=True
)
```
