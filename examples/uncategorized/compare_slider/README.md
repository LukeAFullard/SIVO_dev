# Image Comparison Slider Example

This example demonstrates how to add an interactive image comparison slider to an SVG element using the SIVO `compare` property.

## Features Showcased
- Mapping an interactive side panel to an SVG element (`"sun"`).
- Providing HTML content and tooltips.
- Utilizing the `compare` keyword to embed a before-and-after image slider within the panel.

## Code Snippet
The core mapping uses the `compare` dictionary to define the images and labels:

```python
sivo_app.map(
    "sun",
    tooltip="Main Admin",
    compare={
        "before_image": "https://picsum.photos/id/10/800/600",
        "after_image": "https://picsum.photos/id/11/800/600",
        "label_before": "1990",
        "label_after": "2024"
    },
    html="<p>Slide to compare the old and new building designs.</p>",
    panel_position="left"
)
```

By ensuring `panel_position` is set (either locally or globally via `default_panel_position`), clicking the `"sun"` element opens the side panel displaying the HTML text and the comparison slider underneath.
