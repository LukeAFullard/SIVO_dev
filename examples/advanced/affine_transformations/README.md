# Affine Transformations Example

This example demonstrates how to apply standard SVG affine transformations (like rotate, scale, and translate) directly to elements within a SIVO application.

This functionality relies on setting `render_mode="svg"` when initializing the `Sivo` application to ensure transformations are applied directly to native SVG DOM nodes instead of a canvas overlay.

## What is being shown
- We initialize a small SVG document containing multiple basic shapes: a rectangle, a circle, and a polygon.
- Behind each shape, there is a "ghost" element (dashed and grey) to show the original un-transformed position of each shape.
- We use the `sivo_app.map(...)` function and pass the `transform` parameter to manipulate the targeted SVG shapes dynamically.
- When you hover over the transformed elements in the generated output, you'll see a tooltip showing what transformation was applied.

## Key Code Snippets

### 1. Enabling SVG Render Mode
In order to apply native SVG transformations, `Sivo` must be initialized in `svg` render mode:

```python
sivo_app = Sivo.from_string(svg_string, render_mode="svg")
```

### 2. Applying Transformations
Transformations use standard CSS/SVG transform strings via the `sivo_app.map()` function.

**Rotating:**
```python
sivo_app.map(
    element_id="rectRotate",
    tooltip="Rotated 45 degrees",
    transform="rotate(45 100 100)" # rotate(angle cx cy)
)
```

**Scaling:**
*(Note: In SVG, scaling also implicitly affects translation relative to the origin, so translating might be needed to offset it.)*
```python
sivo_app.map(
    element_id="circleScale",
    tooltip="Scaled by 1.25",
    transform="scale(1.25) translate(-50 -20)"
)
```

**Translating:**
```python
sivo_app.map(
    element_id="polyTranslate",
    tooltip="Translated by (100, 50)",
    transform="translate(100 50)"
)
```

## Running the Example
To run this example locally and generate the interactive `affine_transformations.html` file, run:

```bash
PYTHONPATH=src python examples/advanced/affine_transformations/main.py
```
