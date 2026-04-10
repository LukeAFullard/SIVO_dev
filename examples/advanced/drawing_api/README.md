# Drawing API

This example demonstrates how to use the SIVO framework to dynamically draw native SVG elements (shapes and paths) onto a blank canvas entirely from Python, using the programmatic `add_shape` method. It bypasses the need for an external SVG editor.

## Key Features Showcased

1. **`Sivo.from_string()`**: The canvas is initialized dynamically via an empty base SVG string.
2. **`add_shape()`**: Demonstrates how to programmatically inject standard SVG tags (e.g., `rect`, `circle`, `path`, `text`) along with their respective attributes (coordinates, size, stroke, fill) into the live canvas.
3. **`text_content` Support**: Shows how to use the `text_content` key within the `add_shape` attributes dictionary to dynamically set inner text for `<text>` nodes.
4. **Interactive Mapping**: The dynamically added shapes are immediately available for interaction mapping via `sivo_app.map()`, seamlessly applying properties like tooltips, hover colors, and glow effects, identically to pre-existing SVG elements.

## Relevant Code Snippets

```python
# Initializing an empty SVG canvas
svg_string = \"\"\"
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <!-- Blank canvas -->
</svg>
\"\"\"
sivo_app = Sivo.from_string(svg_string)

# Drawing shapes programmatically
sivo_app.add_shape("circle", {
    "id": "myCircle",
    "cx": "250",
    "cy": "100",
    "r": "50",
    "fill": "#e74c3c"
})

# Adding text with the text_content attribute
sivo_app.add_shape("text", {
    "id": "myText",
    "x": "50",
    "y": "300",
    "font-family": "sans-serif",
    "font-size": "24",
    "fill": "#333",
    "text_content": "SIVO Drawing API"
})

# Mapping interactions to the newly drawn shapes
sivo_app.map(
    element_id="myCircle",
    tooltip="Dynamically drawn circle",
    hover_color="#c0392b"
)
```

## How to Run

1. Execute the Python script:
   ```bash
   PYTHONPATH=src python3 examples/advanced/drawing_api/main.py
   ```
2. Open the resulting `drawing.html` in a web browser.
3. Hover over the drawn rectangle and circle to see the configured tooltips, hover colors, and glow effects.
