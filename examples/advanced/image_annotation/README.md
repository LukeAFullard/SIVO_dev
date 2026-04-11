# Image Annotation Example

This example demonstrates how to use the **SIVO Annotator Tool** to create interactive dashboards from static images (JPGs, PNGs, etc.).

Instead of converting an entire image into a massive SVG, this approach creates a lightweight, invisible SVG "template" that acts as an interactive overlay on top of your original image.

### Code Highlight
The most important part of the code is passing `svg_background_image_url`, `svg_background_image_opacity`, and `svg_background_image_insert_after` to `Sivo.from_svg`. This places your raster image as a background element on the SVG canvas, directly behind your interactive regions.

```python
app = Sivo.from_svg(
    svg_path,
    theme="dark",
    lock_zoom_out=True,
    svg_background_image_url=image_path,
    svg_background_image_opacity=1.0,
    svg_background_image_insert_after="background"
)
```

### Workflow

1. **Start the Annotator Tool**
   Run the following command in your terminal:
   ```bash
   sivo annotate
   ```
   This will open a local web tool in your browser.

2. **Load your Image**
   Click "Load Background Image" and select the image you want to annotate.

3. **Draw Regions**
   Use the Polygon or Rectangle tools to trace over the areas of interest in your image. Name these regions in the sidebar (e.g., `machine_a`, `conveyor_1`, `generator_zone`).

4. **Export the Template**
   Click "Generate SVG Template" and download the file. Save it in this directory as `annotated_template.svg`.

5. **Run SIVO**
   Once your template is ready, run the python script:
   ```bash
   PYTHONPATH=src python3 examples/advanced/image_annotation/main.py
   ```
   SIVO will load your invisible template and then load the original image behind it. Your drawn shapes are now fully interactive SIVO regions!
