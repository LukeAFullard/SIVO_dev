# Masking and Clipping Example

This example demonstrates how to apply SVG masks and clip paths to native SVG elements using Sivo.

## What is being shown
- How to define a `<clipPath>` and `<mask>` in the native SVG `<defs>` section.
- How to apply the `clip_path` to an element dynamically using `sivo_app.map()`.
- How to apply the `mask` to another element using `sivo_app.map()`.

## Relevant Code

The `<clipPath>` and `<mask>` are defined directly in the SVG string:

```xml
<defs>
    <clipPath id="myClip">
        <circle cx="200" cy="200" r="100" />
    </clipPath>
    <mask id="myMask">
        <rect x="0" y="0" width="400" height="400" fill="white" />
        <circle cx="200" cy="200" r="100" fill="black" />
    </mask>
</defs>
```

Then they are mapped to specific SVG elements using Sivo:

```python
sivo_app.map(
    element_id="rectToClip",
    tooltip="This rectangle is clipped by a circle",
    clip_path="url(#myClip)"
)

sivo_app.map(
    element_id="rectToMask",
    tooltip="This rectangle is masked by a circle",
    mask="url(#myMask)"
)
```

In this example, no interactive side panel is used, so the `panel_position` parameter does not need to be explicitly set.
