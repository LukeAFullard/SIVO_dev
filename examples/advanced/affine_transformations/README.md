# Affine Transformations Example

This example demonstrates how to apply standard SVG affine transformations (`rotate`, `scale`, `translate`) to individual SVG elements within SIVO.

By default, SIVO uses a ZRender-based "canvas" render mode, which does not support direct CSS transforms on elements. To use CSS or inline SVG transforms directly on the elements themselves, you must instantiate SIVO using the `render_mode="svg"` configuration.

## What is being tested/demonstrated
*   **SVG Rendering Mode:** The use of `render_mode="svg"` to allow native DOM manipulation of the visualization.
*   **`transform` property:** The ability to pass standard CSS/SVG transformation strings directly to `sivo_app.map()`.
*   **Rotation:** Rotating an element around a specific origin coordinate using `rotate(angle cx cy)`.
*   **Scaling:** Resizing an element using `scale(...)`.
*   **Translation:** Moving an element using `translate(x y)`.

## Code Highlights

To enable native DOM transforms, `render_mode="svg"` is required during instantiation:
```python
sivo_app = Sivo.from_string(svg_string, render_mode="svg")
```

Transformations are passed as strings to the `transform` argument within `map()`:

```python
sivo_app.map(
    element_id="rectRotate",
    tooltip="Rotated 45 degrees",
    transform="rotate(45 100 100)" # rotate(angle cx cy)
)

sivo_app.map(
    element_id="circleScale",
    tooltip="Scaled by 1.25",
    transform="scale(1.25) translate(-50 -20)" # Implicitly translated during scale
)

sivo_app.map(
    element_id="polyTranslate",
    tooltip="Translated by (100, 50)",
    transform="translate(100 50)"
)
```

## Running the Example

Run this example from the root directory of the repository:

```bash
PYTHONPATH=src python3 examples/advanced/affine_transformations/main.py
```

This will output an `affine_transformations.html` file in the same directory, which you can open in a web browser to see the transformed elements hovering over their original "ghost" outlines.
