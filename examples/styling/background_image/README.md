# Background Image Styling Example

This example demonstrates how to style a SIVO dashboard by adding an astronomical background image behind the SVG canvas. The background image sits behind the layout elements and gives the entire view a dramatic, atmospheric look.

## What is being tested/demonstrated
- `app.add_background_image()`: This method sets a background image for the SIVO canvas.
- Applying `opacity` to blend the background image seamlessly into the layout.
- Applying `grayscale` to stylize the background image.
- Assigning interactive elements using `app.map()` and configuring `panel_position` to show side panels and overlays when users interact with specific items in the SVG, such as right, left, bottom, and overlay panels.

## Steps Involved
1. A standard SVG template (`bento_grid_template.svg`) is loaded to create the layout structure.
2. We map several grid elements to interactive actions using `app.map()`, each featuring an HTML payload and explicit `panel_position` configurations (`right`, `left`, `bottom`, `overlay`) since the default panel position is `none`.
3. We define an external URL for a dramatic space background image from NASA/Unsplash.
4. We apply this background image using `add_background_image(bg_url, opacity=0.8, grayscale=True)`, allowing the grid elements to peer through the background with a stylized monochrome tone.
5. Finally, we export the configured application to a standalone interactive HTML file.

## Relevant Code

```python
import os
from sivo import Sivo

# 1. Initialize Sivo with a standard SVG template
app = Sivo.from_svg(
    os.path.join("src", "sivo", "templates", "3_2", "bento_grid_template.svg"),
    title="Bento Grid with Astronomical Background"
)

# 2. Add some interactions to demonstrate standard functionality and explicit panel positions
app.map("bento-hero-data", tooltip="Primary metric overview.", html="<h1>Hero Data</h1><p>More details here.</p>", panel_position="right")
app.map("bento-metric-1-data", tooltip="Secondary metric breakdown.", html="<h1>Metric 1</h1><p>Secondary metrics here.</p>", panel_position="left")
app.map("bento-sidebar-data", tooltip="Geospatial distribution.", html="<h1>Sidebar</h1><p>Geospatial analysis.</p>", panel_position="bottom")
app.map("bento-main-chart-data", tooltip="Performance analysis.", html="<h1>Main Chart</h1><p>Detailed performance analysis.</p>", panel_position="overlay")

# 3. Add the background image feature
bg_url = "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=2000&auto=format&fit=crop"

# We apply opacity to make it subtle and set grayscale=True for a styled look
app.add_background_image(bg_url, opacity=0.8, grayscale=True)

# 4. Save the interactive HTML
app.to_html("index.html")
```
