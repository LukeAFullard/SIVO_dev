# Affine Transformations Example

This example demonstrates how to apply standard SVG affine transformations (like `rotate`, `scale`, `translate`) directly to native SVG DOM elements using SIVO.

## What is being tested/shown

SIVO allows you to configure interactive features mapped to your elements. One of these properties is the `transform` attribute, which maps directly to the standard SVG affine transformation strings.

For transformations to apply accurately using standard SVG syntax on native browser DOM elements rather than HTML5 Canvas paths, the application must be instantiated with the `render_mode="svg"` configuration.

## Relevant Code

The instantiation must use `render_mode="svg"`:

```python
# Native SVG rendering required to apply transforms to the DOM elements directly
sivo_app = Sivo.from_string(svg_string, render_mode="svg")
```

The transforms are applied inside the `.map()` method by passing a standard string to the `transform` argument.

```python
sivo_app.map(
    element_id="rectRotate",
    tooltip="Rotated 45 degrees",
    transform="rotate(45 100 100)" # rotate(angle cx cy)
)

sivo_app.map(
    element_id="circleScale",
    tooltip="Scaled by 1.25",
    transform="scale(1.25) translate(-50 -20)"
)

sivo_app.map(
    element_id="polyTranslate",
    tooltip="Translated by (100, 50)",
    transform="translate(100 50)"
)
```

The output file generated is an HTML file named `affine_transformations.html` which visualizes the applied transformations over ghost shapes of the original coordinates.