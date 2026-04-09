# Mobile Tiny Text

## Description
Set the slow zoom to 1500 ms as requested Tiny button uses the new default 500ms

## Relevant Code
```python
app = Sivo.from_string(
    svg_content,
    disable_zoom_controls=False,
    layout_size="99%",
    disable_panel=True
)
app.fill_template_zone(
    element_id="hidden_text",
    text="You found the secret! SVG vector text remains perfectly crisp, even when scaling from a 5x5 pixel dot to fullscreen.",
    color="#ffffff",
    auto_shrink=True,
    font_size="10%"
)
app.map(
    element_id="zoom_button",
    hover_color="#c0392b",
    tooltip="Click to glide into the microscopic message!"
)
app.map(
    element_id="tiny_button",
    hover_color="#2980b9",
    tooltip="You found it!",
    zoom_on_click=True,
    zoom_level=120.0
)
app.to_html(output_path)
```
