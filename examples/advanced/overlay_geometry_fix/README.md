# Overlay Geometry Fix

## Description
Create a clean directory Generate a simple SVG file with distinct shapes to test overlay alignment Initialize the App Add custom HTML overlays to perfectly anchor and SCALE to the SVG shapes. The JS runtime now applies exact width/height from the ECharts affine matrix, so 100% width fits the box perfectly. 1. Responsive Text Box Overlay It spans the full width of the box. 2. Figure/Image Overlay Scales exactly inside the bounding box. 3. Formatted Content Overlay Utilizing the flexible box dimensions to flow text Generate the output HTML

## Relevant Code
```python
app = Sivo.from_svg(
    svg_path,
    title="HTML Overlay Geometry Test",
    subtitle="The black HTML overlays should stay perfectly centered on the colored SVG rectangles, even when zooming or resizing the window on mobile.",
    theme="light"
)
app.add_overlay("box-1", text_html, scale_with_zoom=True)
app.add_overlay("box-2", figure_html, scale_with_zoom=True)
app.add_overlay("box-3", content_html, scale_with_zoom=True)
app.to_html(output_html)
```
