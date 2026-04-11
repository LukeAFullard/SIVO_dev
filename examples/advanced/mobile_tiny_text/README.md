# Mobile Tiny Text

This example demonstrates how SVG vector text remains perfectly crisp even when scaling to extreme levels. In this case, automatically zooming into a 5x5 pixel dot to reveal a microscopic message.

## What is being tested
- Extreme zoom levels and native SVG vector scaling crispness.
- Using `zoom_to_size="auto"` parameter in `app.map()` combined with `zoom_to` which allows you to zoom into a target element with an automatically calculated zoom strength based on the target's bounding box.
- Filling tiny invisible zones with text using `app.fill_template_zone()`.

## Relevant Code

We create a tiny 5x5 rect in the center of the canvas that serves as the placeholder for our secret text.

```xml
<rect id="hidden_text" x="497.5" y="850" width="5" height="5" fill="transparent" pointer-events="none"></rect>
```

We then programmatically inject the text into this tiny area. Notice `auto_shrink=True`, which ensures it fits inside the small bounds.

```python
app.fill_template_zone(
    element_id="hidden_text",
    text="You found the secret! SVG vector text remains perfectly crisp...",
    color="#ffffff",
    auto_shrink=True,
    font_size="10%"
)
```

Finally, we map the large red button to zoom into that tiny text block. We pass `zoom_to="hidden_text"` to center the camera on it, and define `zoom_to_size="auto"` to tell SIVO to calculate the zoom scale required to fit the target element in the viewport automatically.

```python
app.map(
    element_id="zoom_button",
    hover_color="#c0392b",
    tooltip="Click to glide into the microscopic message!",
    zoom_to="hidden_text",
    zoom_to_size="auto",
    zoom_duration_ms=1500
)
```

## Running the Example
```bash
PYTHONPATH=src python3 examples/advanced/mobile_tiny_text/example.py
```
This generates `output.html`. Open it in your browser and click the red button to experience the extreme zoom effect.
