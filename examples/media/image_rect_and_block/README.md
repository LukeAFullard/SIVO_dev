# Image Rect & Block Helpers

This example demonstrates how to use the `add_image_rect` and `add_image_block` helper methods to simplify injecting images into your applications.

*   `add_image_block` is used by the `SivoDashboard` to quickly place a responsive image into a grid cell without needing to write HTML and CSS boilerplate.
*   `add_image_rect` is used by the `Sivo` core library to dynamically inject native `<image>` SVG tags into the ECharts canvas, allowing you to place raster images at specific X/Y coordinates without needing an underlying template path to clip against.

## Run the example
```bash
python demo.py
```
Open `output.html` in your browser.
