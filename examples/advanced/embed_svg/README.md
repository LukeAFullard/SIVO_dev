# Embed SVG

This example demonstrates how to dynamically embed an external SVG graphic directly into a specific bounding box (target element) within a parent SVG canvas using SIVO.

The inner SVG paths and shapes are injected natively, making them fully interactive with tooltips, click actions, hover effects, and zooming, just like elements of the parent SVG.

## What is being tested/shown

1. **Embedding an SVG into a target placeholder:** A tiny `5x5` rectangle acts as a placeholder (`target_zone`) inside a larger background.
2. **Preserving aspect ratio:** Uniformly scaling the embedded SVG (`inner_svg`) to fit without stretching, using `preserve_aspect_ratio=True`.
3. **Scaling the embedded SVG:** Embedding the SVG at twice the size of the target zone using `scale_multiplier=2.0`.
4. **Targeted navigation/Zooming:** Dynamically zooming to specific bounding boxes, both in the parent SVG and deep inside the embedded child SVG.
5. **Interactive Mapping to Embedded Elements:** Mapping tooltips, hover effects, colors, and glow to natively injected IDs like `inner_bg`, `inner_shape_1`, and `inner_shape_2`.

## Relevant Code

**Initializing Sivo:**
```python
# Create an outer SVG with a small placeholder target zone:
# <rect id="target_zone" x="500" y="500" width="5" height="5" fill="#e2e8f0" />
app = Sivo.from_string(outer_svg, theme="light", disable_zoom_controls=False, layout_size="99%", default_panel_position="right")
```

**Embedding the Inner SVG:**
```python
# Embed the inner SVG directly into the 'target_zone' placeholder.
app.embed_svg(
    "target_zone",
    inner_svg,
    is_file=False,
    preserve_aspect_ratio=True,
    keep_target=False,
    scale_multiplier=2.0
)
```

**Mapping Zoom Interactions to the Embed:**
```python
# Zoom from the parent canvas button into the embedded 'inner_bg' canvas.
app.map(
    "button",
    tooltip="Click to Zoom",
    html="<p>Navigating visually into the microscopic embedded SVG.</p>",
    hover_color="#2563eb",
    zoom_to="inner_bg",
    zoom_to_size="99%",
    zoom_duration_ms=1500
)
```

**Interacting Directly with Embedded Shapes:**
```python
# Since Sivo parses and injects the embedded SVG, its shapes can be mapped natively.
app.map(
    "inner_shape_1",
    tooltip="Inner Hexagon",
    html="<p>Red hexagon from inner.svg</p>",
    color="#f87171",
    hover_color="#dc2626",
    zoom_to="inner_shape_1",
    zoom_to_size="50%"
)
```
