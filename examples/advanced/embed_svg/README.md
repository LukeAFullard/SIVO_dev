# Embed Svg

## Description
We will create a parent SVG with a tiny placeholder rectangle We will create an inner SVG with its own viewBox 1. Initialize the Sivo app with the outer SVG and layout_size 99% 2. Embed the inner SVG directly into the 'target_zone' We set preserve_aspect_ratio=True to uniformly scale the circle without stretching We also apply scale_multiplier=2.0 so the embedded SVG is embedded at twice the size of the target_zone. 3. Map interactivity on the main SVG elements Map the button to dynamically zoom into the "inner_bg" bounding box, fitting it to 99% of the viewport. 4. Map interactivity directly to the embedded inner SVG elements! Because Sivo parsed and injected them natively, their IDs work seamlessly. 5. Export to HTML

## Relevant Code
```python
    app = Sivo.from_string(outer_svg, theme="light", disable_zoom_controls=False, layout_size="99%")
    app.embed_svg("target_zone", inner_svg, is_file=False, preserve_aspect_ratio=True, keep_target=False, scale_multiplier=2.0)
    app.map(
        "background",
        tooltip="Main Canvas Background",
        html="<p>This is the outer SVG canvas.</p>"
    )
    app.map(
        "button",
        tooltip="Click to Zoom",
        html="<p>Navigating visually into the microscopic embedded SVG.</p>",
        hover_color="#2563eb",
        zoom_to="inner_bg",
        zoom_to_size="99%",
        zoom_duration_ms=1500
    )
    app.map(
        "inner_bg",
        tooltip="Embedded Canvas",
        html="<h3>Inner SVG</h3><p>This element was embedded dynamically into a microscopic 5x5 bounding box.</p>",
        hover_color="#fde047"
    )
    app.map(
        "inner_shape_1",
        tooltip="Inner Hexagon",
        html="<p>Red hexagon from inner.svg</p>",
        color="#f87171",
        hover_color="#dc2626",
        zoom_to="inner_shape_1",
        zoom_to_size="50%"
    )
    app.map(
        "inner_shape_2",
        tooltip="Micro Zoom Target",
        html="<p>Blue center dot from inner.svg.</p>",
        color="#60a5fa",
        hover_color="#2563eb",
        glow=True
    )
    app.to_html(output_path)
```
