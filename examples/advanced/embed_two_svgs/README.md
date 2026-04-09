# Embed Two Svgs

## Description
We will create a parent SVG with two tiny placeholder rectangles First embedded SVG Second embedded SVG 1. Initialize the Sivo app 2. Embed both SVGs into their respective tiny targets 3. Map Outer SVG Interactivity Map the start button to zoom into Location A 4. Map Inner SVG A Interactivity Map the button inside A to zoom across the map to Location B 5. Map Inner SVG B Interactivity Map the button inside B to zoom all the way back out to the main background 6. Export to HTML

## Relevant Code
```python
    app = Sivo.from_string(outer_svg, theme="light", disable_zoom_controls=False, layout_size="99%")
    app.embed_svg("target_a", svg_a, is_file=False, preserve_aspect_ratio=True, keep_target=False, scale_multiplier=2.0)
    app.embed_svg("target_b", svg_b, is_file=False, preserve_aspect_ratio=True, keep_target=False, scale_multiplier=2.0)
    app.map("background", tooltip="World Map")
    app.map(
        "start_btn",
        tooltip="Click to start",
        hover_color="#1d4ed8",
        zoom_to="bg_a",
        zoom_to_size="80%",
        zoom_duration_ms=1000
    )
    app.map("bg_a", tooltip="Location A (Yellow Area)")
    app.map(
        "btn_to_b",
        tooltip="Click to travel to B",
        hover_color="#ca8a04",
        zoom_to="bg_b",
        zoom_to_size="80%",
        zoom_duration_ms=1500
    )
    app.map("bg_b", tooltip="Location B (Green Area)")
    app.map(
        "btn_to_home",
        tooltip="Click to return home",
        hover_color="#047857",
        zoom_to="background",
        zoom_to_size="99%",
        zoom_duration_ms=1500
    )
    app.to_html(output_path)
```
