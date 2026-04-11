# SIVO Example: HTML Overlay Geometry Alignment

## Purpose

This example demonstrates how SIVO precisely aligns native HTML element overlays with underlying SVG coordinates using the `add_overlay` method. It proves that HTML overlays (like `div` elements) can dynamically mirror the bounding geometry of any targeted SVG element while preserving their scale correctly during zooming and panning, without drifting across the canvas.

## Features Showcased

1. **`add_overlay(element_id, html, scale_with_zoom=True)`**
   - Renders absolute-positioned HTML DOM elements over native SVG shapes.
   - Ensures the injected HTML has dimensions reflecting the ECharts affine matrix so `width: 100%; height: 100%` aligns edge-to-edge.
   - Scaling logic (`scale_with_zoom=True`) ensures overlay size increases/decreases accurately in relation to canvas scale state.

## Steps Involved

1. Generates an `test_geometry.svg` file with three rounded rectangles positioned at different locations.
2. Initializes the app with `Sivo.from_svg()`.
3. Calls `add_overlay` for each rectangle using three distinct types of responsive HTML content:
   - A centered, full-width text layer.
   - An object-fit constrained figure/image layer.
   - A flexbox formatted data box layering dynamic content over the base shape.
4. Generates a self-contained output `index.html`.

## Key Code

```python
# Initialize the App
app = Sivo.from_svg(
    svg_path,
    title="HTML Overlay Geometry Test",
    subtitle="The black HTML overlays should stay perfectly centered on the colored SVG rectangles...",
    theme="light"
)

# 1. Responsive Text Box Overlay spanning the full width of the box.
text_html = '<div style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.2); border-radius: 12px;"><span style="color: #ffffff; font-weight: 800; font-family: sans-serif; font-size: 18px; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">BOX 1</span></div>'

# By targeting "box-1", the overlay positions itself perfectly over that SVG element's boundaries.
app.add_overlay("box-1", text_html, scale_with_zoom=True)

# Generate the output HTML
output_html = "examples/advanced/overlay_geometry_fix/index.html"
app.to_html(output_html)
```

To test alignment behavior, interactively scroll/zoom on the resulting `index.html` on both desktop and mobile viewports.
