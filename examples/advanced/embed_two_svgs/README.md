# Embed Two SVGs Example

This example demonstrates how to use the `embed_svg` method in SIVO to inject multiple external SVG graphics directly into specific target elements (bounding boxes) within a parent SVG.

## What is being tested/shown

1.  **Multiple SVG Injections (`embed_svg`)**:
    We create a parent SVG that acts as a wide canvas (a "World Map" journey) containing two tiny placeholder rectangles (`target_a` and `target_b`). We then embed two distinct, smaller SVGs into those targets. The embeddings dynamically replace the targets, scaling up and preserving their respective coordinates and paths.

2.  **Sequential Camera Zoom (`zoom_to`)**:
    We test the ability to map elements to trigger smooth, cinematic camera panning and zooming (`zoom_to`).
    - The **Start** button in the main map zooms deeply into the bounding box of Location A (`zoom_to="bg_a"`).
    - A button **inside** embedded SVG A zooms across the vast map to Location B (`zoom_to="bg_b"`).
    - A button **inside** embedded SVG B zooms back out to the main map (`zoom_to="background"`).

3.  **Nested Interactivity**:
    This example proves that paths and shapes originating from *embedded* SVGs (such as `#btn_to_b` inside `svg_a` or `#btn_to_home` inside `svg_b`) become first-class citizens in the SIVO runtime. They can be fully mapped with tooltips, hover effects (`hover_color`), and interactions (zooming) just like native paths in the original parent SVG.

## Relevant Code

**Embedding SVGs:**
```python
# Embeds the string content of svg_a into the "target_a" rectangle.
# scale_multiplier=2.0 scales the embedded SVG to be twice the size of the target bounding box.
app.embed_svg("target_a", svg_a, is_file=False, preserve_aspect_ratio=True, keep_target=False, scale_multiplier=2.0)
app.embed_svg("target_b", svg_b, is_file=False, preserve_aspect_ratio=True, keep_target=False, scale_multiplier=2.0)
```

**Mapping Interactivity across Parent and Embedded Paths:**
```python
# Map button in Parent SVG to zoom into an element from Embedded SVG A
app.map(
    "start_btn",
    tooltip="Click to start",
    hover_color="#1d4ed8",
    zoom_to="bg_a", # This ID exists inside svg_a
    zoom_to_size="80%",
    zoom_duration_ms=1000
)

# Map button from Embedded SVG A to zoom into an element from Embedded SVG B
app.map(
    "btn_to_b",
    tooltip="Click to travel to B",
    hover_color="#ca8a04",
    zoom_to="bg_b", # This ID exists inside svg_b
    zoom_to_size="80%",
    zoom_duration_ms=1500
)
```

## Running the Example

Run this example from the root of the repository:

```bash
PYTHONPATH=src python3 examples/advanced/embed_two_svgs/main.py
```

This will generate an `output.html` file in the same directory which you can open in your browser to test the multi-SVG journey.