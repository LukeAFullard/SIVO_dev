# Clip Image to Shape

This example demonstrates how to use the `clip_image_to_shape` method in SIVO to dynamically mask images to the exact shapes of SVG elements.

## What is being tested/demonstrated
- Creating a base SVG string containing primitive shapes (`<circle>`, `<rect>`, and `<path>`).
- Initializing a Sivo instance directly from the SVG string using `Sivo.from_string()`.
- Explicitly setting `default_panel_position="none"` to prevent empty side panels from opening upon shape interaction.
- Using `clip_image_to_shape` to map remote images into different SVG elements.
- Demonstrating the configuration of `clip_image_to_shape` with properties such as:
  - `preserve_aspect_ratio`: How to fit the image (e.g. `xMidYMid slice`).
  - `scale`, `rotate`, `translate_x`, and `translate_y`: Adjusting the scale, rotation, and position of the image within the clipped region.
  - `opacity`: Modifying the image's opacity.
- Attaching interactions using `app.map()` to ensure elements with clipped images remain interactive, applying custom hover effects and tooltips.

## Relevant Code Snippets

**Initializing Sivo with `default_panel_position` set to `none`**
```python
# Initialize Sivo directly from the SVG string
# Using default_panel_position="none" so we don't open an empty side panel when shapes are clicked
app = Sivo.from_string(svg_content, default_panel_position="none", title="Image Clipping Example")
```

**Clipping an image to a `<circle>` element**
```python
# Clip a square image to the circular shape
app.clip_image_to_shape(
    element_id="my_circle",
    image_url="https://images.unsplash.com/photo-1579546929518-9e396f3cc809",
    preserve_aspect_ratio="xMidYMid slice"
)
```

**Clipping an image with transformations to a `<rect>` element**
```python
# Clip an image to the rectangle with scaling, rotation, and translation panning
app.clip_image_to_shape(
    element_id="my_rect",
    image_url="https://images.unsplash.com/photo-1557683316-973673baf926",
    scale=1.5,
    rotate=15, # Rotate 15 degrees
    translate_x=-30, # Pan the image 30 pixels left within the clipped region
    translate_y=20,  # Pan the image 20 pixels down within the clipped region
    opacity=0.8
)
```

**Mapping an interaction to a clipped shape**
```python
# Map an interaction to the rectangle
app.map(
    element_id="my_rect",
    tooltip="I am a rectangle with a scaled, rotated image!",
    hover_color="rgba(255, 255, 255, 0.3)" # Add a light tint on hover
)
```