# Mobile Tiny Text 4 3

## Description
4:3 aspect ratio = 1200x900 Background image over SVG canvas. We use encode_base64=True so ECharts draws the image immediately on the first render, bypassing the browser's asynchronous external image loading which would leave it blank. Clip same image to tiny text area with 0.3 opacity. We set use_html_overlay=False because HTML CSS masking has precision issues when zooming natively to extreme microscopic levels (120x) on a 5px target. Setting it to False natively injects an <image> tag bounding box into the SVG. Set the slow zoom to 1500 ms as requested Tiny button uses the new default 500ms

## Relevant Code
```python
app = Sivo.from_string(
    svg_content,
    disable_zoom_controls=False,
    layout_size="99%",
    disable_panel=True,
    theme="dark"
)
app.add_svg_background_image(
    url=image_url,
    opacity=0.5,
    encode_base64=True
)
app.clip_image_to_shape(
    element_id="hidden_text",
    image_url=image_url,
    opacity=0.3,
    use_html_overlay=False,
    encode_base64=True
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
