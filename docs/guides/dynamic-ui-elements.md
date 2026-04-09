---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Guide: Dynamic UI Elements

SIVO provides a rich set of Python methods to programmatically inject dynamic user interface (UI) layers directly into your SVG maps and dashboards. These elements—such as cards, text, markers, and progress bars—automatically scale, pan, and integrate natively with your visualization without needing custom CSS or complex positioning math.

## 1. Introduction to UI Elements

When building dashboards, you often need to overlay information—like KPIs, labels, or images—on top of specific shapes or regions. SIVO's UI methods handle calculating the bounding boxes of target SVG elements (using lxml and cssselect under the hood) and precisely injecting these components so they resize perfectly across all devices.

## 2. Cards and Text

### Adding Information Cards (`add_card`)
The `add_card()` method dynamically generates and auto-scales native SVG cards (KPIs) relative to a target element's bounding box.

```python
# Anchor a KPI card to an SVG rectangle with ID 'kpi_container_1'
sivo.add_card(
    element_id="kpi_container_1",
    title="Total Revenue",
    value="$1.2M",
    subtitle="+15% vs last year",
    bg_color="#f8fafc",
    rx="8" # Border radius
)
```

### Injecting Scalable Text (`add_scalable_text` & `fill_template_zone`)
You can place perfectly scaled native SVG text relative to the bounding box of a target element.

```python
sivo.add_scalable_text(
    target_id="header_banner",
    text="Global Operations Overview",
    font_size="50%", # 50% of the banner's height
    font_weight="bold",
    color="#1e293b",
    align="center",
    auto_shrink=True # Prevent text overflow
)
```

For templates with placeholder shapes (e.g., a `<rect>`), you can completely replace the shape with perfectly scaled text using `fill_template_zone()`:

```python
sivo.fill_template_zone(
    element_id="title_placeholder_rect",
    text="Quarterly Report",
    font_size=32,
    align="center"
)
```

## 3. Overlays and Markers

### Custom HTML Overlays (`add_overlay`)
Sometimes you need standard HTML widgets (like a custom stylized div or interactive component). You can inject custom HTML that overlays an SVG element's center coordinate.

```python
custom_html = """
<div style="background: red; color: white; padding: 5px; border-radius: 5px;">
    Alert!
</div>
"""
sivo.add_overlay(element_id="factory_3", html=custom_html, scale_with_zoom=False)
```

### Pinning Markers (`add_marker`)
A convenience method to easily drop an icon and label at the exact center of a targeted shape.

```python
sivo.add_marker(
    element_id="store_location_nyc",
    icon="📍",
    label="NYC Hub",
    scale_with_zoom=True
)
```

## 4. Images and Clipping

### Image Overlays (`add_image_overlay`)
Easily embed responsive images within an SVG element's bounding box without writing custom HTML.

```python
sivo.add_image_overlay(
    element_id="profile_picture_zone",
    image_url="https://example.com/user123.jpg",
    object_fit="cover",
    border_radius="50%"
)
```

### Clipping Content to Shapes (`clip_image_to_shape` & `clip_html_to_shape`)
You can clip images or even raw HTML directly to the exact vector paths of an SVG element. The content perfectly scales and pans natively with the ECharts vector renderer.

```python
# Clip an image to the exact path of a map territory
sivo.clip_image_to_shape(
    element_id="territory_california",
    image_url="assets/california_terrain.jpg",
    opacity=0.8
)

# Clip a live Folium map (or any iframe) to an SVG path
iframe_html = '<iframe src="https://example.com/map" width="100%" height="100%"></iframe>'
sivo.clip_html_to_shape(
    element_id="hexbin_cell_45",
    html=iframe_html
)
```

## 5. Progress Bars

### Visual Indicators (`add_scalable_progress_bar`)
Automatically generate a perfectly scaled, native SVG progress bar relative to the bounding box of a target element.

```python
# Show 75% completion in a specific dashboard zone
sivo.add_scalable_progress_bar(
    element_id="project_alpha_status",
    progress=0.75,
    height="20%",
    fill_color="#10b981", # Emerald green
    bg_color="#e2e8f0"
)
```
