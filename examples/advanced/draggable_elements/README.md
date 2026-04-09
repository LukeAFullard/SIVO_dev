# Draggable Elements

## Description
Demonstrates the use of SIVO for draggable elements.

## Relevant Code
```python
sivo_app = Sivo.from_string(svg_string, render_mode="svg")
sivo_app.map(
    element_id="dragRect",
    tooltip="This rectangle is draggable",
    draggable=True
)
sivo_app.map(
    element_id="dragCircle",
    tooltip="This circle is draggable",
    draggable=True
)
sivo_app.to_html(output_path)
```
