# Draggable Elements Example

This example demonstrates how to make elements in an SVG graphic draggable using the SIVO library.

## Purpose
The purpose of this example is to show how setting `draggable=True` inside `sivo.map()` allows users to drag SVG elements around within the visualization, making the experience more interactive.

## How it works

1. We define a simple SVG string with a rectangle and a circle.
2. We load this SVG string into SIVO via `Sivo.from_string()`.
3. We configure the rectangle (`id="dragRect"`) and the circle (`id="dragCircle"`) to have a tooltip and enable the drag functionality by passing `draggable=True`.
4. Finally, we output the result to an HTML file.

### Key Code Snippet

The critical piece of code is the `.map()` method call, which attaches the `draggable=True` property to specific SVG elements:

```python
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
```

By adding `draggable=True`, the generated ECharts runtime automatically applies draggable behavior to these graphical elements.

## Running the Example

Run the Python script directly to generate the output HTML:

```bash
python3 main.py
```

This will create or update `draggable_elements.html` in the same directory. Open `draggable_elements.html` in your browser to interact with the draggable elements.
