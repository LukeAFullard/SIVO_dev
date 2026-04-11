# Zoom on Click Example

This example demonstrates how to configure SIVO elements to automatically zoom when clicked. It is useful for interactive maps, floor plans, and complex diagrams where focusing on a specific area is helpful for user context.

## What is being shown

The application loads a simple sample SVG featuring two labelled regions, "TX" and "CA".

We bind interactive properties to these two regions using the `sivo_app.map()` function.

### Key Concepts

*   **`zoom_on_click`**: When set to `True`, clicking the element dynamically changes the viewport to zoom in and center on the bounding box of that element.
*   **`zoom_level`**: Dictates the scale of the zoom. A value of `3.5` means the view zooms in to 3.5 times the original scale.
*   **`panel_position`**: Since default panels are hidden, we explicitly set `panel_position="right"` to render a side-panel containing context-specific HTML when an element is clicked.

## How to Run

1. Make sure your dependencies are installed.
2. From the repository root, run the example:

```bash
PYTHONPATH=src python3 examples/advanced/zoom_on_click/main.py
```

3. Open the generated `output.html` file in your browser to view the interactive diagram. Try clicking on the squares to observe the automatic zooming effect and the right-side information panel.