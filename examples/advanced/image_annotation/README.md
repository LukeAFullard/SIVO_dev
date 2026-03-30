This example demonstrates how to use the **SIVO Annotator Tool** to create interactive dashboards from static images (JPGs, PNGs, etc.).

Instead of converting an entire image into a massive SVG, this approach creates a lightweight, invisible SVG "template" that acts as an interactive overlay on top of your original image.

### Workflow

1. **Start the Annotator Tool**
   Run the following command in your terminal:
   ```bash
   sivo annotate
   ```
   This will open a local web tool in your browser.

2. **Load your Image**
   Click "Load Background Image" and select `factory_floor.png`.

3. **Draw Regions**
   Use the Polygon or Rectangle tools to trace over the machinery, conveyors, or any other area of interest. Name these regions in the sidebar (e.g., `generator_1`, `conveyor_belt`).

4. **Export the Template**
   Click "Generate SVG Template" and download the file. Save it in this directory as `annotated_template.svg`.

5. **Run SIVO**
   Once your template is ready, run this python script:
   ```bash
   python main.py
   ```
   SIVO will load your invisible template and then load the original image behind it using `app.add_background_image()`. Your drawn shapes are now fully interactive ECharts regions!