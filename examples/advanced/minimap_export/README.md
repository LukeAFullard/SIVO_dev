# Minimap and Export Example

This example demonstrates how to enable the minimap and export toolbar in a SIVO application.

## What is being tested/shown

1. **Minimap**: A small overview map of the entire SVG canvas that allows users to quickly navigate and see their current viewport relative to the whole image. It is especially useful for large, complex SVGs where the user might zoom in and lose context.
2. **Export Toolbar**: A set of controls that allows users to export the current view as an image (e.g., PNG or SVG) or download the underlying data.

## Code highlights

The key feature being demonstrated is the use of `enable_minimap=True` and `enable_export=True` parameters when initializing the `Sivo` application from an SVG string.

```python
# Enable minimap and export capabilities during initialization
sivo_app = Sivo.from_string(
    svg_content,
    enable_minimap=True,
    enable_export=True
)
```

By passing these two flags:
- `enable_minimap=True`: A minimap will be rendered in the corner of the interactive canvas.
- `enable_export=True`: An export/download toolbar is added to the UI, giving the user the ability to save the visual state.

## How to run

To generate the `minimap_export.html` file, run the following command from the root of the repository:

```bash
PYTHONPATH=src python3 examples/advanced/minimap_export/main.py
```
