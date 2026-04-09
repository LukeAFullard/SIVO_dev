# Zoom On Click

## Description
1. Map elements to zoom on click 3. Export to HTML

## Relevant Code
```python
    sivo_app = Sivo.from_svg(svg_path)
    sivo_app.map(
        element_id="TX",
        tooltip="Texas Region",
        html="<h3>Texas Region</h3><p>Zoomed in automatically to Texas.</p>",
        zoom_on_click=True,
        zoom_level=3.5
    )
    sivo_app.map(
        element_id="CA",
        tooltip="California Region",
        html="<h3>California Region</h3><p>Zoomed in automatically to California.</p>",
        zoom_on_click=True,
        zoom_level=3.5
    )
    sivo_app.to_html(output_path)
```
