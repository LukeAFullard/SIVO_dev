# Hover Image Example

This example demonstrates how to use the `hover_image` and `fill_pattern` features in SIVO to dynamically change the image fill of an SVG element when a user hovers over it, while also maintaining a side panel integration on click.

## What is being tested/demonstrated
- **`fill_pattern`**: Used to map an initial static image as the base fill of an SVG element.
- **`hover_image`**: Specifies a new image URL that seamlessly appears on mouse hover, creating a dynamic visual effect (e.g., turning on a lightbulb).
- **`panel_position`**: Explicitly set to `"right"` to ensure that clicking the element opens an informative side panel, testing the interoperability of hover themes with click actions.

## Steps Involved
1. A basic SVG circle with the ID `lightbulb_area` is defined.
2. The `Sivo.from_svg()` method loads the graphic.
3. Two distinct image URLs (a dark bulb and a lit bulb) are provided.
4. The `Sivo.map()` function attaches these images to the `lightbulb_area` ID, applying the dark image via `fill_pattern` and the lit image via `hover_image`.
5. An `html` payload and `panel_position="right"` are added to ensure click behavior opens a panel on the right side.
6. The project is exported to HTML.

## Relevant Code Snippets

```python
# Use a basic circle SVG
svg_str = \"\"\"
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle id="lightbulb_area" cx="50" cy="50" r="40" fill="#cccccc" />
</svg>
\"\"\"

...

# Map the hover effect and side panel to the circle ID
app.map(
    "lightbulb_area",
    tooltip="Hover to light up!",
    fill_pattern={"image": dark_bulb},
    hover_image=lit_bulb,
    html="<h2>Lightbulb Clicked!</h2><p>You can map a side panel to the same element that has a hover effect.</p>",
    panel_position="right"
)
```
