# Gradients and Patterns

This example demonstrates how to apply linear gradients and image patterns to SVG elements using the SIVO library.

## What is being tested

- Applying a linear gradient to an SVG rectangle using the `fill_gradient` parameter.
- Applying an image pattern to an SVG circle using the `fill_pattern` parameter.
- The `tooltip` parameter is used to provide context when hovering over the elements.
- The `panel_position` and `html` parameters are used to provide more details about the clicked element. When clicking the elements, an HTML side panel or overlay appears to provide further context about the visual styles applied to them.

## Code Snippets

### Linear Gradient
```python
sivo_app.map(
    element_id="gradientRect",
    tooltip="This rectangle uses a linear gradient",
    html="<h3>Gradient Rectangle</h3><p>This rectangle features a linear gradient applied via SIVO.</p>",
    panel_position="right",
    fill_gradient={
        "type": "linear",
        "x": 0, "y": 0, "x2": 1, "y2": 1,
        "stops": [
            {"offset": 0, "color": "#3498db"},
            {"offset": 1, "color": "#2ecc71"}
        ]
    }
)
```

### Image Pattern
```python
pattern_image_url = "https://www.transparenttextures.com/patterns/cubes.png"

sivo_app.map(
    element_id="patternCircle",
    tooltip="This circle uses an image pattern",
    html="<h3>Pattern Circle</h3><p>This circle features an image pattern applied via SIVO.</p>",
    panel_position="left",
    fill_pattern={
        "image": pattern_image_url,
        "repeat": "repeat"
    }
)
```

## Running the Example

Run the `main.py` script to generate the HTML output file `gradients_patterns.html`.

```bash
python main.py
```
