# Layer Toggles Example

This example demonstrates how to create an interactive legend that toggles the visibility of native SVG layer groups.

## Features Shown

*   **Native SVG Overlays:** The `render_mode="svg"` configuration is used to ensure the interactive elements are mapped to native SVG nodes rather than ECharts canvas elements.
*   **Layer Visibility:** The `add_layer_toggle()` method creates a floating control panel (legend) that allows users to show or hide entire groups (`<g>`) of SVG elements simultaneously.
*   **Coordinate Alignment:** The example relies on the core library automatically extracting the SVG `viewBox` and using it to set the `bounding_coords` globally. This ensures the native SVG overlay is perfectly scaled and aligned with the underlying ECharts layout matrix.

## Running the Example

```bash
PYTHONPATH=src python3 examples/advanced/layer_toggles/main.py
```
This will generate `layer_toggles.html` in the same directory.
