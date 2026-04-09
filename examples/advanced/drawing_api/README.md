# Drawing Api

## Description
1. Initialize Sivo from a blank SVG string 2. Programmatically add shapes 3. Map interactions to the dynamically created shapes 4. Export to HTML

## Relevant Code
```python
sivo_app = Sivo.from_string(svg_string)
sivo_app.add_shape("rect", {
    "id": "myRect",
    "x": "50",
    "y": "50",
    "width": "100",
    "height": "100",
    "fill": "#3498db"
})
sivo_app.add_shape("circle", {
    "id": "myCircle",
    "cx": "250",
    "cy": "100",
    "r": "50",
    "fill": "#e74c3c"
})
sivo_app.add_shape("path", {
    "id": "myPath",
    "d": "M50 250 Q150 150 250 250 T400 250",
    "stroke": "#2ecc71",
    "stroke-width": "5",
    "fill": "none"
})
sivo_app.add_shape("text", {
    "id": "myText",
    "x": "50",
    "y": "300",
    "font-family": "sans-serif",
    "font-size": "24",
    "fill": "#333",
    "text_content": "SIVO Drawing API" # Needs support
})
sivo_app.map(
    element_id="myRect",
    tooltip="Dynamically drawn rectangle",
    hover_color="#2980b9",
    glow=True
)
sivo_app.map(
    element_id="myCircle",
    tooltip="Dynamically drawn circle",
    hover_color="#c0392b"
)
sivo_app.to_html(output_path)
```
