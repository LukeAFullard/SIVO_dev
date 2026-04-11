# Mobile Tiny Text (4:3 Aspect Ratio)

This example demonstrates extreme automatic zooming into a microscopic message, specifically testing how SIVO handles these extreme native vector scalings on a 4:3 canvas (1200x900) while also applying background image clipping.

## What is being tested
- Extreme automatic zoom levels and native vector crispness using `zoom_to_size="auto"`.
- Aspect ratio (4:3) handling.
- Background image embedding (`app.add_svg_background_image`) combined with image clipping directly to the tiny text container.
- Setting `use_html_overlay=False` when using `clip_image_to_shape()`, which forces SIVO to natively inject an `<image>` bounding box instead of using HTML CSS masking. CSS masking suffers from precision errors at extreme scales.

## Relevant Code

We set up a 1200x900 aspect ratio canvas and include the tiny secret text box.
```xml
<svg viewBox="0 0 1200 900" xmlns="http://www.w3.org/2000/svg">
  <!-- ... -->
  <rect id="hidden_text" x="597.5" y="450" width="5" height="5" fill="transparent" pointer-events="none"></rect>
```

We add a background image to the canvas, explicitly encoding it to Base64 to ensure it renders immediately on the first tick in ECharts before external fetching completes.
```python
app.add_svg_background_image(
    url=image_url,
    opacity=0.5,
    encode_base64=True
)
```

We clip the same background image into our tiny 5x5 pixel area. We set `use_html_overlay=False` because HTML CSS clipping breaks precision when scaling extremely large.
```python
app.clip_image_to_shape(
    element_id="hidden_text",
    image_url=image_url,
    opacity=0.3,
    use_html_overlay=False,
    encode_base64=True
)
```

We map the zoom button to navigate deep into the canvas automatically.
```python
app.map(
    element_id="zoom_button",
    hover_color="#c0392b",
    tooltip="Click to glide into the microscopic message!",
    zoom_to="hidden_text",
    zoom_to_size="auto",
    zoom_duration_ms=1500
)
```

## Running the Example
```bash
PYTHONPATH=src python3 examples/advanced/mobile_tiny_text_4_3/example.py
```
This generates `output.html`. Open it in your browser to experience the extreme zoom effect over background images.
