# Mixed Features Dashboard

This example demonstrates how to create a complex dashboard in SIVO that integrates various types of content alongside interactive vector graphics.

### Features Demonstrated:
1. **Custom Grid Layouts:** Using `dashboard.set_grid_layout()` to define distinct responsive CSS Grid templates for `desktop` and `mobile` viewports.
2. **Background Image:** Applying a fixed background image to the dashboard using `background_image_url` during initialization. The dashboard handles making the block cards slightly translucent to showcase the background.
3. **HTML Blocks:** Embedding raw HTML content directly into grid slots using `add_html_block()`.
4. **Video Embeds:** Embedding a YouTube video via an `iframe` within an HTML block.
5. **Multiple SIVO Blocks:** Rendering multiple independent `Sivo` instances side-by-side in the dashboard layout.
